const fs = require('fs');
const data = JSON.parse(fs.readFileSync('D:/applications/AI_files/sciomap/data/scientists.json', 'utf8'));

// Each scientist: array of {year, title, titleEn} — all verified
const verified = {
  'darwin': [{year:1839,title:'英国皇家学会院士',titleEn:'Fellow of the Royal Society'},{year:1864,title:'科普利奖章',titleEn:'Copley Medal'}],
  'pasteur': [{year:1874,title:'科普利奖章',titleEn:'Copley Medal'}],
  'mendeleev': [{year:1905,title:'科普利奖章',titleEn:'Copley Medal'}],
  'kelvin': [{year:1883,title:'科普利奖章',titleEn:'Copley Medal'}],
  'faraday': [{year:1832,title:'科普利奖章',titleEn:'Copley Medal'}],
  'gauss': [{year:1838,title:'科普利奖章',titleEn:'Copley Medal'}],
  'hawking': [{year:2006,title:'科普利奖章',titleEn:'Copley Medal'},{year:2009,title:'总统自由勋章',titleEn:'Presidential Medal of Freedom'}],
  'herschel': [{year:1781,title:'科普利奖章',titleEn:'Copley Medal'}],
  'huxley': [{year:1851,title:'英国皇家学会院士',titleEn:'Fellow of the Royal Society'},{year:1888,title:'科普利奖章',titleEn:'Copley Medal'}],
  'newton': [{year:1672,title:'英国皇家学会院士',titleEn:'Fellow of the Royal Society'},{year:1705,title:'爵士爵位',titleEn:'Knight Bachelor'}],
  'hooke': [{year:1663,title:'英国皇家学会院士',titleEn:'Fellow of the Royal Society'}],
  'boyle': [{year:1660,title:'英国皇家学会院士',titleEn:'Fellow of the Royal Society'}],
  'leibniz': [{year:1673,title:'英国皇家学会外籍院士',titleEn:'Foreign Member, Royal Society'}],
  'maxwell': [{year:1861,title:'英国皇家学会院士',titleEn:'Fellow of the Royal Society'}],
  'wallace': [{year:1893,title:'英国皇家学会院士',titleEn:'Fellow of the Royal Society'}],
  'lister': [{year:1860,title:'英国皇家学会院士',titleEn:'Fellow of the Royal Society'}],
  'babbage': [{year:1816,title:'英国皇家学会院士',titleEn:'Fellow of the Royal Society'}],
  'boltzmann': [{year:1899,title:'英国皇家学会外籍院士',titleEn:'Foreign Member, Royal Society'}],
  'turing': [{year:1945,title:'大英帝国勋章（OBE）',titleEn:'Officer of the Order of the British Empire'},{year:1951,title:'英国皇家学会院士',titleEn:'Fellow of the Royal Society'}],
  'shannon': [{year:1966,title:'美国国家科学奖章',titleEn:'National Medal of Science'}],
  'hubble': [{year:1938,title:'布鲁斯奖章',titleEn:'Bruce Medal'}],
  'sagan': [{year:1978,title:'普利策奖（非小说类）',titleEn:'Pulitzer Prize for General Non-Fiction'}],
  'deng-jiaxian': [{year:1999,title:'两弹一星功勋奖章',titleEn:'Two Bombs, One Satellite Meritorious Medal'}],
  'wang-xuan': [{year:2001,title:'国家最高科学技术奖',titleEn:'National Highest Science and Technology Award'}],
  'zhong-nanshan': [{year:2020,title:'共和国勋章',titleEn:'Medal of the Republic'}],
  'wu-wenjun': [{year:2000,title:'国家最高科学技术奖',titleEn:'National Highest Science and Technology Award'}],
  'xu-guangxian': [{year:2008,title:'国家最高科学技术奖',titleEn:'National Highest Science and Technology Award'}],
  'yuan-longping': [{year:2000,title:'国家最高科学技术奖',titleEn:'National Highest Science and Technology Award'}],
  'qian-xuesen': [{year:1991,title:'国家杰出贡献科学家',titleEn:'Distinguished Scientist of China'}],
  'shi-yigong': [{year:2017,title:'未来科学大奖',titleEn:'Future Science Prize'}],
  'nan-rendong': [{year:2019,title:'人民科学家',titleEn:"People's Scientist"}],
  'torvalds': [{year:2014,title:'IEEE计算机先锋奖',titleEn:'IEEE Computer Pioneer Award'}],
};

// Merge into existing data
data.scientists.forEach(s => {
  const more = verified[s.id];
  if (more) {
    if (!s.famousEvents) s.famousEvents = [];
    more.forEach(a => {
      const dup = s.famousEvents.some(e => e.title === a.title);
      if (!dup) s.famousEvents.push({title:a.title, titleEn:a.titleEn, year:a.year, desc:a.title, descEn:a.titleEn});
    });
  }
});

const json = JSON.stringify(data, null, 2);
fs.writeFileSync('D:/applications/AI_files/sciomap/data/scientists.json', json, 'utf8');
fs.writeFileSync('D:/applications/AI_files/sciomap/data/scientists.js', '_sciomapData = ' + json + ';', 'utf8');

const withAwards = data.scientists.filter(s => s.famousEvents && s.famousEvents.length > 0);
console.log('Scientists with awards:', withAwards.length, '/', data.scientists.length);
data.scientists.forEach(s => {
  if (s.famousEvents && s.famousEvents.length > 0) {
    s.famousEvents.forEach(e => console.log('  ' + s.id + ' (' + s.name + '): ' + e.title + ' (' + e.year + ')'));
  }
});
