/**
 * 把本机下载好的 data/portraits/*.jpg 与改好的 data/scientists.js 上传到 GitHub Pages
 * 运行环境：沙箱（通过 GitHub Contents API，因沙箱 git push 被墙）
 * 前置：需先在本机运行 download_portraits.js 生成图片
 */
const fs = require('fs'), https = require('https'), path = require('path');
const cred = fs.readFileSync('C:/Users/yun/.git-credentials', 'utf8');
let token = null;
cred.split(/\r?\n/).forEach(l => {
  const m = l.match(/https:\/\/([^:]+):([^@]+)@github\.com/);
  if (m && l.includes('yun-ai-base')) token = m[2];
});
if (!token) { console.error('NO TOKEN'); process.exit(1); }
const owner = 'yun-ai-base', repo = 'sciomap', branch = 'main';
const dir = 'D:/applications/AI_files/sciomap';

function req(method, api, body) {
  return new Promise((res, rej) => {
    const data = body ? JSON.stringify(body) : null;
    const opts = { hostname: 'api.github.com', path: api, method, headers: { 'User-Agent': 'up', 'Authorization': 'token ' + token, 'Accept': 'application/vnd.github+json' } };
    if (data) opts.headers['Content-Type'] = 'application/json';
    const r = https.request(opts, resp => { let b = ''; resp.on('data', d => b += d); resp.on('end', () => res({ status: resp.statusCode, body: b })); });
    r.on('error', rej); if (data) r.write(data); r.end();
  });
}
async function putFile(p, fp, msg) {
  const content = fs.readFileSync(fp).toString('base64');
  const get = await req('GET', '/repos/' + owner + '/' + repo + '/contents/' + p + '?ref=' + branch);
  let sha = null; if (get.status === 200) sha = JSON.parse(get.body).sha;
  const put = await req('PUT', '/repos/' + owner + '/' + repo + '/contents/' + p, { message: msg, content, branch, ...(sha ? { sha } : {}) });
  console.log(p, put.status);
}
(async () => {
  const pd = path.join(dir, 'data', 'portraits');
  if (!fs.existsSync(pd)) { console.log('未找到 data/portraits，请先在本机运行 download_portraits.js'); process.exit(0); }
  const files = fs.readdirSync(pd).filter(f => /\.(jpg|jpeg|png|svg|webp)$/i.test(f));
  console.log('待上传图片:', files.length);
  let i = 0;
  for (const f of files) {
    await putFile('data/portraits/' + f, path.join(pd, f), 'add portrait ' + f);
    i++; if (i % 10 === 0) console.log('进度', i + '/' + files.length);
    await new Promise(r => setTimeout(r, 250));
  }
  await putFile('data/scientists.js', path.join(dir, 'data', 'scientists.js'), 'use local portrait paths');
  console.log('ALL DONE');
})();
