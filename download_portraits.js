/**
 * 一键下载科学家头像到本地 data/portraits/<id>.jpg
 * 运行环境：你本机（能访问 en.wikipedia.org / upload.wikimedia.org）
 * 用法：在本文件所在目录执行  node download_portraits.js
 * 说明：脚本会读取 data/scientists.js，把每位科学家的 portrait 改为本地相对路径，
 *       并下载图片到 data/portraits/。原文件自动备份为 data/scientists.js.bak。
 */
const fs = require('fs');
const https = require('https');
const path = require('path');

const dir = __dirname;
const dataFile = path.join(dir, 'data', 'scientists.js');
const outDir = path.join(dir, 'data', 'portraits');
fs.mkdirSync(outDir, { recursive: true });
fs.copyFileSync(dataFile, dataFile + '.bak');
console.log('已备份原数据 -> data/scientists.js.bak');

// 解析数据对象
let s = fs.readFileSync(dataFile, 'utf8');
const objSrc = s.replace(/^[^=]*=\s*/, '').replace(/;\s*$/, '');
const data = eval('(' + objSrc + ')');
const scientists = data.scientists || [];

function download(url) {
  return new Promise((resolve, reject) => {
    let redirects = 0;
    function go(u) {
      if (redirects++ > 6) return reject(new Error('重定向过多'));
      https.get(u, { headers: { 'User-Agent': 'Mozilla/5.0', Accept: 'image/*' } }, resp => {
        if (resp.statusCode >= 300 && resp.statusCode < 400 && resp.headers.location) {
          resp.resume();
          const next = resp.headers.location.startsWith('http')
            ? resp.headers.location
            : 'https://en.wikipedia.org' + resp.headers.location;
          return go(next);
        }
        if (resp.statusCode !== 200) { resp.resume(); return reject(new Error('HTTP ' + resp.statusCode)); }
        const chunks = [];
        resp.on('data', c => chunks.push(c));
        resp.on('end', () => resolve(Buffer.concat(chunks)));
      }).on('error', reject);
    }
    go(url);
  });
}

(async () => {
  let ok = 0, fail = 0;
  for (const p of scientists) {
    if (!p.portrait) continue;
    const dest = path.join(outDir, p.id + '.jpg');
    const newPath = 'data/portraits/' + p.id + '.jpg';
    if (fs.existsSync(dest)) { p._new = newPath; ok++; continue; }
    try {
      const buf = await download(p.portrait);
      if (buf.length < 500) throw new Error('文件过小，可能不是图片');
      fs.writeFileSync(dest, buf);
      p._new = newPath;
      ok++;
      console.log('OK  ', p.id, buf.length, 'bytes');
    } catch (e) {
      fail++;
      console.log('FAIL', p.id, e.message);
    }
    await new Promise(r => setTimeout(r, 120)); // 礼貌节流
  }
  // 写回：把 portrait 替换为本地路径
  let raw = fs.readFileSync(dataFile, 'utf8');
  for (const p of scientists) {
    if (p._new && raw.includes(p.portrait)) {
      raw = raw.split(p.portrait).join(p._new);
    }
  }
  fs.writeFileSync(dataFile, raw);
  console.log(`\n完成：成功 ${ok} 张，失败 ${fail} 张`);
  console.log('本地图片目录：' + outDir);
  if (fail > 0) console.log('失败的条目仍保留原外部链接，可在联网环境重试。');
})();
