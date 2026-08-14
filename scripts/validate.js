#!/usr/bin/env node
/**
 * Sciomap 数据校验脚本 validate.js
 * 职责：完整性 / 一致性 / 去重 三级校验，供 git pre-commit hook 与手动执行使用。
 *
 * 用法：
 *   node scripts/validate.js              # 校验 data/scientists.js
 *   node scripts/validate.js --report     # 输出 markdown 格式报告
 *
 * 退出码：0 = 通过（仅警告）；1 = 存在阻断性错误
 *
 * 版本：1.0.0（2026-08-14，配合数据扩增方案 v1.0）
 */
'use strict';

const fs = require('fs');
const path = require('path');

const DATA_PATH = path.join(__dirname, '..', 'data', 'scientists.js');
const SUPP_PATH = path.join(__dirname, '..', 'scientists-data.json');

/* ---------- 加载数据 ---------- */
function loadData(filePath) {
  const raw = fs.readFileSync(filePath, 'utf8');
  let text = raw.trim();
  if (text.startsWith('_sciomapData')) {
    text = text.slice(text.indexOf('=') + 1).trim();
  }
  if (text.endsWith(';')) text = text.slice(0, -1).trim();
  return JSON.parse(text);
}

let data;
let supplement;
try {
  data = loadData(DATA_PATH);
} catch (e) {
  console.error(`[FATAL] 无法解析 ${DATA_PATH}: ${e.message}`);
  process.exit(1);
}
try {
  supplement = loadData(SUPP_PATH);
} catch (e) {
  supplement = null; // 补充字段文件可选
}

const scientists = data.scientists || [];
const CULTURAL_TAGS = new Set((data.culturalTags || []).map(t => t.id));
const ERAS = new Set((data.eras || []).map(e => e.id));
const DISCIPLINES = new Set((data.disciplines || []).map(d => d.id));
const SUB_DISCIPLINES = new Map((data.subDisciplines || []).map(s => [s.id, s.discipline]));

/* ---------- 常量 ---------- */
const L1_FIELDS = [
  'id', 'name', 'nameEn', 'birth', 'death', 'nationality', 'nationalityEn',
  'discipline', 'subDiscipline', 'culturalTag', 'era', 'influence',
  'summary', 'summaryEn',
];
const NEW_REQUIRED = ['gender', 'awards']; // wikidataId 因网络受限暂列为警告项
const NOW_YEAR = new Date().getFullYear();
const ERRORS = [];
const WARNINGS = [];

function err(msg, s) { ERRORS.push(`${s ? `[${s.id}] ` : ''}${msg}`); }
function warn(msg, s) { WARNINGS.push(`${s ? `[${s.id}] ` : ''}${msg}`); }

/* ---------- 1. 去重 ---------- */
const seenIds = new Map();
const seenNameEn = new Map();
for (const s of scientists) {
  if (!s || typeof s !== 'object') { err('条目不是对象'); continue; }
  const id = s.id;
  if (seenIds.has(id)) err(`id 重复: ${id}`, s);
  else seenIds.set(id, s);
  const key = (s.nameEn || '').toLowerCase().trim();
  if (key) {
    if (seenNameEn.has(key)) err(`nameEn 归一化后重复: "${s.nameEn}" 与 "${seenNameEn.get(key)}"`, s);
    else seenNameEn.set(key, s.nameEn);
  }
}

/* ---------- 2. L1 必填 ---------- */
for (const s of scientists) {
  for (const f of L1_FIELDS) {
    // death 允许为 null（表示在世或未知），其余 L1 字段必须非空
    if (f === 'death') {
      if (s[f] === undefined) err(`L1 字段缺失: ${f}`, s);
      continue;
    }
    const v = s[f];
    if (v === undefined || v === null || v === '') err(`L1 字段缺失: ${f}`, s);
  }
  for (const f of NEW_REQUIRED) {
    if (s[f] === undefined) {
      // 存量回填完成后不应再出现；区分存量与新增
      err(`新增字段缺失: ${f}（存量数据需回填）`, s);
    }
  }
  if (s.wikidataId === undefined) warn(`缺少 wikidataId（网络受限待回填）`, s);
}

/* ---------- 3. 数值与取值一致性 ---------- */
for (const s of scientists) {
  const b = s.birth, d = s.death;

  if (typeof b === 'number') {
    if (b < -800 || b > NOW_YEAR) err(`birth 超出合理范围: ${b}`, s);
  } else if (b !== null && b !== undefined) {
    err(`birth 类型错误: ${JSON.stringify(b)}`, s);
  }

  if (typeof d === 'number') {
    if (d > NOW_YEAR + 2) err(`death 超出当前年份: ${d}`, s);
    if (typeof b === 'number' && d < b) err(`death(${d}) < birth(${b})`, s);
  } else if (d !== null && d !== undefined) {
    err(`death 类型错误: ${JSON.stringify(d)}`, s);
  }

  if (!CULTURAL_TAGS.has(s.culturalTag)) {
    err(`culturalTag "${s.culturalTag}" 不在定义表 ${JSON.stringify([...CULTURAL_TAGS])}`, s);
  }
  if (!ERAS.has(s.era)) err(`era "${s.era}" 不在定义表`, s);
  if (!DISCIPLINES.has(s.discipline)) err(`discipline "${s.discipline}" 不在定义表`, s);
  if (s.subDiscipline) {
    const parent = SUB_DISCIPLINES.get(s.subDiscipline);
    if (!parent) err(`subDiscipline "${s.subDiscipline}" 不在定义表`, s);
    else if (parent !== s.discipline) err(`subDiscipline "${s.subDiscipline}" 属于 ${parent}，与 discipline=${s.discipline} 不一致`, s);
  }
  if (typeof s.influence === 'number' && (s.influence < 1 || s.influence > 10)) {
    err(`influence 超出 1-10: ${s.influence}`, s);
  }

  // era 与出生年份一致性（用 eras 区间，允许边界 ±20 年容差）
  const eraDef = (data.eras || []).find(e => e.id === s.era);
  if (eraDef && typeof b === 'number' && typeof eraDef.start === 'number') {
    const lo = eraDef.start - 20, hi = eraDef.end + 20;
    if (b < lo || b > hi) {
      warn(`era=${s.era}(${eraDef.start}~${eraDef.end}) 与 birth=${b} 跨度较大，请人工确认`, s);
    }
  }

  // gender 取值
  if (s.gender && !['male', 'female', 'non-binary', 'unknown'].includes(s.gender)) {
    err(`gender 非法值: ${s.gender}`, s);
  }
}

/* ---------- 4. 嵌套结构 ---------- */
for (const s of scientists) {
  const checkNested = (arr, name, requiredFields, optionalFields = []) => {
    if (arr === undefined) return;
    if (!Array.isArray(arr)) { err(`${name} 应为数组`, s); return; }
    arr.forEach((item, i) => {
      if (!item || typeof item !== 'object') { err(`${name}[${i}] 应为对象`, s); return; }
      for (const f of requiredFields) {
        if (item[f] === undefined || item[f] === null || item[f] === '') {
          err(`${name}[${i}].${f} 缺失`, s);
        }
      }
      for (const f of optionalFields) {
        if (item[f] === undefined) warn(`${name}[${i}].${f} 缺失（可选）`, s);
      }
    });
  };
  checkNested(s.keyContributions, 'keyContributions', ['title', 'titleEn', 'desc'], ['year']);
  checkNested(s.famousEvents, 'famousEvents', ['title', 'titleEn', 'year']);
  checkNested(s.problemsSolved, 'problemsSolved', ['problem', 'problemEn', 'breakthrough', 'breakthroughEn']);
  checkNested(s.keyWorks, 'keyWorks', ['title', 'titleEn', 'year', 'type']);
  checkNested(s.awards, 'awards', ['name', 'nameEn', 'year', 'type']);
  checkNested(s.controversies, 'controversies', ['topic', 'topicEn', 'outcome', 'outcomeEn']);

  // relationships target 必须存在
  if (Array.isArray(s.relationships)) {
    s.relationships.forEach((r, i) => {
      if (!r || !r.target) { err(`relationships[${i}].target 缺失`, s); return; }
      if (!seenIds.has(r.target)) err(`relationships[${i}].target "${r.target}" 指向不存在的科学家`, s);
    });
  }
}

/* ---------- 5. 补充字段文件一致性（scientists-data.json） ---------- */
if (supplement) {
  for (const sid of Object.keys(supplement)) {
    if (!seenIds.has(sid)) warn(`scientists-data.json 中 "${sid}" 不在主数据中`, null);
  }
}

/* ---------- 输出 ---------- */
const reportMode = process.argv.includes('--report');
if (reportMode) {
  console.log('# Sciomap 数据校验报告\n');
  console.log(`- 数据量：${scientists.length} 位科学家`);
  console.log(`- 学科定义：${data.disciplines.length} 个；子学科：${data.subDisciplines.length} 个`);
  console.log(`- 错误：${ERRORS.length} ｜ 警告：${WARNINGS.length}\n`);
  if (ERRORS.length) {
    console.log('## 阻断性错误\n');
    ERRORS.forEach(e => console.log(`- [x] ${e}`));
    console.log('');
  }
  if (WARNINGS.length) {
    console.log('## 警告\n');
    WARNINGS.forEach(w => console.log(`- [!] ${w}`));
    console.log('');
  }
} else {
  console.log(`Sciomap validate: ${scientists.length} scientists, ${ERRORS.length} errors, ${WARNINGS.length} warnings`);
  ERRORS.forEach(e => console.log(`  [ERROR] ${e}`));
  WARNINGS.forEach(w => console.log(`  [WARN]  ${w}`));
}

process.exit(ERRORS.length ? 1 : 0);
