const fs = require('fs');
const data = JSON.parse(fs.readFileSync('D:/applications/AI_files/sciomap/data/scientists.json', 'utf8'));

const awards = {
  'einstein': [{year:1921,title:'诺贝尔物理学奖',titleEn:'Nobel Prize in Physics'}],
  'planck': [{year:1918,title:'诺贝尔物理学奖',titleEn:'Nobel Prize in Physics'}],
  'bohr': [{year:1922,title:'诺贝尔物理学奖',titleEn:'Nobel Prize in Physics'}],
  'heisenberg': [{year:1932,title:'诺贝尔物理学奖',titleEn:'Nobel Prize in Physics'}],
  'schrodinger': [{year:1933,title:'诺贝尔物理学奖',titleEn:'Nobel Prize in Physics'}],
  'dirac': [{year:1933,title:'诺贝尔物理学奖',titleEn:'Nobel Prize in Physics'}],
  'pauli': [{year:1945,title:'诺贝尔物理学奖',titleEn:'Nobel Prize in Physics'}],
  'fermi': [{year:1938,title:'诺贝尔物理学奖',titleEn:'Nobel Prize in Physics'}],
  'rutherford': [{year:1908,title:'诺贝尔化学奖',titleEn:'Nobel Prize in Chemistry'}],
  'curie': [{year:1903,title:'诺贝尔物理学奖',titleEn:'Nobel Prize in Physics'},{year:1911,title:'诺贝尔化学奖',titleEn:'Nobel Prize in Chemistry'}],
  'feynman': [{year:1965,title:'诺贝尔物理学奖',titleEn:'Nobel Prize in Physics'}],
  'yang-zhenning': [{year:1957,title:'诺贝尔物理学奖',titleEn:'Nobel Prize in Physics'}],
  'li-zhengdao': [{year:1957,title:'诺贝尔物理学奖',titleEn:'Nobel Prize in Physics'}],
  'wu-jianxiong': [{year:1978,title:'沃尔夫物理学奖',titleEn:'Wolf Prize in Physics'}],
  'ting': [{year:1976,title:'诺贝尔物理学奖',titleEn:'Nobel Prize in Physics'}],
  'chandrasekhar': [{year:1983,title:'诺贝尔物理学奖',titleEn:'Nobel Prize in Physics'}],
  'tsui-daniel': [{year:1998,title:'诺贝尔物理学奖',titleEn:'Nobel Prize in Physics'}],
  'kao-charles': [{year:2009,title:'诺贝尔物理学奖',titleEn:'Nobel Prize in Physics'}],
  'chu-steven': [{year:1997,title:'诺贝尔物理学奖',titleEn:'Nobel Prize in Physics'}],
  'penrose': [{year:2020,title:'诺贝尔物理学奖',titleEn:'Nobel Prize in Physics'}],
  'ding-zhaozhong': [{year:1976,title:'诺贝尔物理学奖',titleEn:'Nobel Prize in Physics'}],
  'yang': [{year:1957,title:'诺贝尔物理学奖',titleEn:'Nobel Prize in Physics'}],
  'li': [{year:1957,title:'诺贝尔物理学奖',titleEn:'Nobel Prize in Physics'}],
  'turing': [{year:1951,title:'英国皇家学会院士',titleEn:'Fellow of the Royal Society'}],
  'shannon': [{year:1940,title:'美国国家科学奖章',titleEn:'National Medal of Science'}],
  'von-neumann': [{year:1956,title:'美国国家科学奖章',titleEn:'National Medal of Science'}],
  'hinton': [{year:2018,title:'图灵奖',titleEn:'Turing Award'}],
  'li-feifei': [{year:2020,title:'ACM院士',titleEn:'ACM Fellow'}],
  'yao-qizhi': [{year:2000,title:'图灵奖',titleEn:'Turing Award'}],
  'knuth': [{year:1974,title:'图灵奖',titleEn:'Turing Award'}],
  'mccarthy': [{year:1971,title:'图灵奖',titleEn:'Turing Award'}],
  'dijkstra': [{year:1972,title:'图灵奖',titleEn:'Turing Award'}],
  'ritchie': [{year:1983,title:'图灵奖',titleEn:'Turing Award'}],
  'berners-lee': [{year:2016,title:'图灵奖',titleEn:'Turing Award'}],
  'nash': [{year:1994,title:'诺贝尔经济学奖',titleEn:'Nobel Prize in Economics'}],
  'mendeleev': [{year:1905,title:'科普利奖章',titleEn:'Copley Medal'}],
  'darwin': [{year:1864,title:'科普利奖章',titleEn:'Copley Medal'}],
  'pasteur': [{year:1874,title:'科普利奖章',titleEn:'Copley Medal'}],
  'fleming': [{year:1945,title:'诺贝尔生理学或医学奖',titleEn:'Nobel Prize in Medicine'}],
  'watson': [{year:1962,title:'诺贝尔生理学或医学奖',titleEn:'Nobel Prize in Medicine'}],
  'crick': [{year:1962,title:'诺贝尔生理学或医学奖',titleEn:'Nobel Prize in Medicine'}],
  'mcclintock': [{year:1983,title:'诺贝尔生理学或医学奖',titleEn:'Nobel Prize in Medicine'}],
  'tu-youyou': [{year:2015,title:'诺贝尔生理学或医学奖',titleEn:'Nobel Prize in Medicine'}],
  'chen-shengshen': [{year:1984,title:'沃尔夫数学奖',titleEn:'Wolf Prize in Mathematics'}],
  'qiu-chengtong': [{year:1982,title:'菲尔兹奖',titleEn:'Fields Medal'}],
  'tao-zhexuan': [{year:2006,title:'菲尔兹奖',titleEn:'Fields Medal'}],
  'nobel': [{year:1896,title:'设立诺贝尔奖',titleEn:'Established Nobel Prizes'}],
  'sagan': [{year:1978,title:'普利策奖',titleEn:'Pulitzer Prize'}],
  'hubble': [{year:1920,title:'英国皇家天文学会金质奖章',titleEn:'RAS Gold Medal'}],
  'wallace': [{year:1892,title:'皇家学会皇家奖章',titleEn:'Royal Medal'}],
  'huxley': [{year:1893,title:'皇家学会皇家奖章',titleEn:'Royal Medal'}],
  'newton': [{year:1705,title:'英国皇家学会院士',titleEn:'Fellow of the Royal Society'}],
  'faraday': [{year:1838,title:'英国皇家学会院士',titleEn:'Fellow of the Royal Society'}],
  'babbage': [{year:1816,title:'英国皇家学会院士',titleEn:'Fellow of the Royal Society'}],
  'lovelace': [{year:1843,title:'首位计算机程序员',titleEn:'First Computer Programmer'}],
  'maxwell': [{year:1871,title:'卡文迪什实验室首任主任',titleEn:'First Cavendish Professor'}],
  'gauss': [{year:1807,title:'哥廷根天文台台长',titleEn:'Director of Göttingen Observatory'}],
  'leibniz': [{year:1673,title:'英国皇家学会院士',titleEn:'Fellow of the Royal Society'}],
  'descartes': [{year:1641,title:'近代哲学之父',titleEn:'Father of Modern Philosophy'}],
  'fermat': [{year:1636,title:'数论之父',titleEn:'Father of Modern Number Theory'}],
  'pascal': [{year:1654,title:'概率论创始人',titleEn:'Founder of Probability Theory'}],
  'lagrange': [{year:1766,title:'法国科学院院士',titleEn:'French Academy of Sciences'}],
  'laplace': [{year:1799,title:'法国科学院院士',titleEn:'French Academy of Sciences'}],
  'cauchy': [{year:1816,title:'法国科学院院士',titleEn:'French Academy of Sciences'}],
  'galois': [{year:1831,title:'群论创始人',titleEn:'Founder of Group Theory'}],
  'cantor': [{year:1904,title:'皇家学会西尔维斯特奖章',titleEn:'Royal Society Sylvester Medal'}],
  'hilbert': [{year:1930,title:'柯尼斯堡荣誉公民',titleEn:'Honorary Citizen of Königsberg'}],
  'poincare': [{year:1887,title:'法国科学院院士',titleEn:'French Academy of Sciences'}],
  'godel': [{year:1951,title:'爱因斯坦奖',titleEn:'Einstein Award'}],
  'hooke': [{year:1663,title:'英国皇家学会院士',titleEn:'Fellow of the Royal Society'}],
  'hertz': [{year:1889,title:'赫兹（Hz）命名来源',titleEn:'Namesake of Hertz (Hz)'}],
  'boltzmann': [{year:1899,title:'玻尔兹曼常数命名来源',titleEn:'Namesake of Boltzmann Constant'}],
  'kelvin': [{year:1892,title:'开尔文男爵',titleEn:'Baron Kelvin'},{year:1883,title:'皇家学会皇家奖章',titleEn:'Royal Medal'}],
  'clausius': [{year:1870,title:'德国科学院院士',titleEn:'German Academy of Sciences'}],
  'dalton': [{year:1803,title:'近代化学之父',titleEn:'Father of Modern Chemistry'}],
  'avogadro': [{year:1811,title:'阿伏伽德罗定律命名来源',titleEn:'Namesake of Avogadro\'s Law'}],
  'arrhenius': [{year:1903,title:'诺贝尔化学奖',titleEn:'Nobel Prize in Chemistry'}],
  'pauling': [{year:1954,title:'诺贝尔化学奖',titleEn:'Nobel Prize in Chemistry'},{year:1962,title:'诺贝尔和平奖',titleEn:'Nobel Peace Prize'}],
  'ptolemy': [{year:150,title:'古代天文学集大成者',titleEn:'Greatest Ancient Astronomer'}],
  'tycho': [{year:1572,title:'第谷超新星发现者',titleEn:'Discoverer of Tycho\'s Supernova'}],
  'herschel': [{year:1781,title:'天王星发现者',titleEn:'Discoverer of Uranus'},{year:1821,title:'英国皇家天文学会首任主席',titleEn:'First President of RAS'}],
  'aristotle': [{year:-340,title:'百科全书式学者',titleEn:'Encyclopedic Scholar'}],
  'linnaeus': [{year:1753,title:'现代分类学之父',titleEn:'Father of Modern Taxonomy'}],
  'boyle': [{year:1660,title:'英国皇家学会创始人',titleEn:'Founder of the Royal Society'}],
  'vesalius': [{year:1543,title:'现代解剖学之父',titleEn:'Father of Modern Anatomy'}],
  'harvey': [{year:1628,title:'血液循环发现者',titleEn:'Discoverer of Blood Circulation'}],
  'jenner': [{year:1796,title:'疫苗之父',titleEn:'Father of Vaccination'}],
  'lister': [{year:1867,title:'现代无菌手术之父',titleEn:'Father of Antiseptic Surgery'}],
  'torvalds': [{year:2014,title:'IEEE计算机先锋奖',titleEn:'IEEE Computer Pioneer Award'}],
  'euclid': [{year:-300,title:'几何学之父',titleEn:'Father of Geometry'}],
  'hawking': [{year:1979,title:'阿尔伯特·爱因斯坦奖',titleEn:'Albert Einstein Award'},{year:2009,title:'总统自由勋章',titleEn:'Presidential Medal of Freedom'}],
  'qian-xuesen': [{year:1991,title:'国家杰出贡献科学家',titleEn:'Distinguished Scientist of China'}],
  'chen-jingrun': [{year:1982,title:'国家自然科学奖一等奖',titleEn:'National Natural Science Award'}],
  'zhang-heng': [{year:132,title:'地动仪发明者',titleEn:'Inventor of Seismoscope'}],
  'nan-rendong': [{year:2016,title:'中国天眼（FAST）总工程师',titleEn:'Chief Engineer of FAST'}],
  'hua-tuo': [{year:200,title:'外科手术鼻祖',titleEn:'Pioneer of Surgery'}],
  'zhang-zhongjing': [{year:210,title:'医圣',titleEn:'Saint of Medicine'}],
  'hou-debang': [{year:1943,title:'侯氏制碱法发明者',titleEn:'Inventor of Hou\'s Process'}],
  'deng-jiaxian': [{year:1999,title:'两弹一星功勋奖章',titleEn:'Two Bombs, One Satellite Meritorious Medal'}],
  'wang-xuan': [{year:2001,title:'国家最高科学技术奖',titleEn:'China National Science and Technology Award'}],
  'zhong-nanshan': [{year:2020,title:'共和国勋章',titleEn:'Medal of the Republic'}],
  'tan-jiazhen': [{year:1980,title:'中国科学院院士',titleEn:'Academician of CAS'}],
  'su-buqing': [{year:1948,title:'中央研究院院士',titleEn:'Academician of Academia Sinica'}],
  'wu-wenjun': [{year:2000,title:'国家最高科学技术奖',titleEn:'China National Science and Technology Award'}],
  'pan-jianwei': [{year:2017,title:'中国量子通信之父',titleEn:'Father of Quantum Communication in China'}],
  'xu-guangxian': [{year:2008,title:'国家最高科学技术奖',titleEn:'China National Science and Technology Award'}],
  'guo-shoujing': [{year:1281,title:'授时历编撰者',titleEn:'Compiler of the Shoushi Calendar'}],
  'tong-dizhou': [{year:1978,title:'中国科学院副院长',titleEn:'Vice President of CAS'}],
  'shi-yigong': [{year:2017,title:'未来科学大奖',titleEn:'Future Science Prize'}],
  'galen': [{year:170,title:'欧洲医学奠基人',titleEn:'Founder of European Medicine'}],
  'lin-qiaozhi': [{year:1983,title:'中国妇产科学奠基人',titleEn:'Founder of Chinese Obstetrics and Gynecology'}]
};

let added = 0;
data.scientists.forEach(s => {
  const aw = awards[s.id];
  if (aw) {
    if (!s.famousEvents) s.famousEvents = [];
    aw.forEach(a => {
      const exists = s.famousEvents.some(e => e.title === a.title || e.titleEn === a.titleEn);
      if (!exists) {
        s.famousEvents.push({
          title: a.title, titleEn: a.titleEn,
          year: a.year,
          desc: a.title, descEn: a.titleEn
        });
        added++;
      }
    });
  }
});

fs.writeFileSync('D:/applications/AI_files/sciomap/data/scientists.json', JSON.stringify(data, null, 2), 'utf8');
console.log('Added', added, 'awards');
const w = data.scientists.filter(s => s.famousEvents && s.famousEvents.length > 0);
console.log('Scientists with famousEvents:', w.length, '/', data.scientists.length);
