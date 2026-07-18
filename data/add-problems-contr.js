const fs = require('fs');
const data = JSON.parse(fs.readFileSync('D:/applications/AI_files/sciomap/data/scientists.json', 'utf8'));

const problems = {
  'galileo': [{problem:'天体运动的地心说矛盾',problemEn:'Problems with Geocentric Model',breakthrough:'用天文观测证实日心说，发现木星卫星和金星的相位变化',breakthroughEn:'Confirmed heliocentrism through telescopic observations of Jupiter\'s moons and Venus phases'}],
  'kepler': [{problem:'火星轨道的精确计算',problemEn:'Precise Calculation of Mars Orbit',breakthrough:'放弃圆形轨道假设，发现行星沿椭圆轨道运动（开普勒第一定律）',breakthroughEn:'Abandoned circular orbits, discovered elliptical planetary orbits (Kepler\'s First Law)'}],
  'newton': [{problem:'天体运动与地面运动的统一解释',problemEn:'Unifying Celestial and Terrestrial Motion',breakthrough:'提出万有引力定律和三大运动定律，统一了天体和地面的物理学',breakthroughEn:'Proposed universal gravitation and three laws of motion, unifying celestial and terrestrial physics'}],
  'faraday': [{problem:'电与磁的关系之谜',problemEn:'The Relationship Between Electricity and Magnetism',breakthrough:'发现电磁感应现象，证明变化的磁场可以产生电流',breakthroughEn:'Discovered electromagnetic induction, proving changing magnetic fields produce electric current'}],
  'maxwell': [{problem:'电学、磁学与光学的统一',problemEn:'Unifying Electricity, Magnetism, and Optics',breakthrough:'建立麦克斯韦方程组，预言电磁波的存在并将光识别为电磁波',breakthroughEn:'Formulated Maxwell\'s equations, predicted electromagnetic waves, identified light as EM wave'}],
  'einstein': [{problem:'光在以太中的传播问题',problemEn:'The Light Ether Problem',breakthrough:'抛弃以太概念，提出光速不变原理和狭义相对论',breakthroughEn:'Abandoned the ether concept, proposed constant light speed and special relativity'},{problem:'光电效应的经典解释困境',problemEn:'The Photoelectric Effect Puzzle',breakthrough:'提出光量子假说，用光子概念成功解释光电效应',breakthroughEn:'Proposed light quantum hypothesis, successfully explained the photoelectric effect'}],
  'planck': [{problem:'黑体辐射的紫外灾难',problemEn:'The Ultraviolet Catastrophe',breakthrough:'提出能量量子化假说，E=nhν，开创量子物理学',breakthroughEn:'Proposed energy quantization, E=nhν, founding quantum physics'}],
  'bohr': [{problem:'卢瑟福原子模型的不稳定性',problemEn:'Instability of Rutherford\'s Atomic Model',breakthrough:'提出电子在固定能级轨道运行，量子跃迁解释原子光谱',breakthroughEn:'Proposed electrons in fixed energy orbits, quantum jumps explain atomic spectra'}],
  'rutherford': [{problem:'原子内部结构之谜',problemEn:'The Mystery of Atomic Structure',breakthrough:'通过α粒子散射实验发现原子核，提出行星式原子模型',breakthroughEn:'Discovered the atomic nucleus via alpha scattering, proposed planetary atomic model'}],
  'curie': [{problem:'放射性元素的分离与确认',problemEn:'Isolation and Identification of Radioactive Elements',breakthrough:'从沥青铀矿中分离出钋和镭两种新放射性元素',breakthroughEn:'Isolated polonium and radium from uranium ore'}],
  'heisenberg': [{problem:'量子世界中可观测量的界限',problemEn:'Limits of Observability in the Quantum World',breakthrough:'提出不确定性原理，指出位置和动量无法同时被精确测量',breakthroughEn:'Proposed the uncertainty principle—position and momentum cannot both be precisely measured'}],
  'schrodinger': [{problem:'微观粒子的波粒二象性的数学描述',problemEn:'Mathematical Description of Wave-Particle Duality',breakthrough:'建立薛定谔方程，用波函数描述量子系统的演化',breakthroughEn:'Formulated the Schrödinger equation, using wave functions to describe quantum evolution'}],
  'dirac': [{problem:'相对论与量子力学的统一',problemEn:'Unifying Relativity and Quantum Mechanics',breakthrough:'建立狄拉克方程，预言反物质（正电子）的存在',breakthroughEn:'Formulated the Dirac equation, predicted antimatter (positron)'}],
  'yang-zhenning': [{problem:'θ-τ之谜：同种粒子为何有不同的衰变方式',problemEn:'The θ-τ Puzzle',breakthrough:'提出弱相互作用中宇称不守恒，推翻物理学基本定律的对称性假设',breakthroughEn:'Proposed parity non-conservation in weak interactions, overturning a fundamental symmetry assumption'}],
  'li-zhengdao': [{problem:'θ-τ之谜：同种粒子为何有不同的衰变方式',problemEn:'The θ-τ Puzzle',breakthrough:'与杨振宁共同提出弱相互作用中宇称不守恒，获1957年诺贝尔奖',breakthroughEn:'With Yang, proposed parity non-conservation in weak interactions, won 1957 Nobel Prize'}],
  'wu-jianxiong': [{problem:'宇称守恒定律的实验验证',problemEn:'Experimental Test of Parity Conservation',breakthrough:'设计并执行钴-60实验，首次实验证实弱相互作用中宇称不守恒',breakthroughEn:'Designed and performed the cobalt-60 experiment, first experimental proof of parity non-conservation'}],
  'darwin': [{problem:'物种多样性的起源',problemEn:'The Origin of Species Diversity',breakthrough:'提出自然选择理论，揭示物种通过适应环境逐渐演化的机制',breakthroughEn:'Proposed natural selection, revealing how species evolve through environmental adaptation'}],
  'mendel': [{problem:'遗传规律的科学解释',problemEn:'Scientific Explanation of Inheritance',breakthrough:'通过豌豆杂交实验发现遗传的分离定律和自由组合定律',breakthroughEn:'Discovered laws of segregation and independent assortment through pea experiments'}],
  'pasteur': [{problem:'微生物自然发生说之争',problemEn:'The Spontaneous Generation Debate',breakthrough:'设计鹅颈瓶实验，证明微生物不会自然发生，推翻自然发生说',breakthroughEn:'Swan-neck flask experiment proved microorganisms do not spontaneously generate'}],
  'harvey': [{problem:'血液流动的路径与动力',problemEn:'The Path and Power of Blood Flow',breakthrough:'发现血液循环系统，证明心脏是血液流动的动力源',breakthroughEn:'Discovered blood circulation, proved the heart powers blood flow'}],
  'jenner': [{problem:'天花的预防',problemEn:'Prevention of Smallpox',breakthrough:'发明牛痘接种法，开创免疫学，最终在全球范围内消灭了天花',breakthroughEn:'Developed smallpox vaccination, founding immunology, leading to global smallpox eradication'}],
  'fleming': [{problem:'细菌感染的药物治疗',problemEn:'Drug Treatment for Bacterial Infections',breakthrough:'发现青霉素的杀菌作用，开启了抗生素时代',breakthroughEn:'Discovered penicillin\'s antibacterial effect, ushering in the antibiotic era'}],
  'watson': [{problem:'遗传信息的分子存储机制',problemEn:'Molecular Storage of Genetic Information',breakthrough:'与克里克共同发现DNA双螺旋结构，揭示遗传信息的分子基础',breakthroughEn:'With Crick, discovered the DNA double helix, revealing the molecular basis of heredity'}],
  'crick': [{problem:'遗传信息的分子存储机制',problemEn:'Molecular Storage of Genetic Information',breakthrough:'与沃森共同发现DNA双螺旋结构，揭示遗传信息的分子基础',breakthroughEn:'With Watson, discovered the DNA double helix, revealing the molecular basis of heredity'}],
  'turing': [{problem:'希尔伯特的可判定性问题（Entscheidungsproblem）',problemEn:'Hilbert\'s Decision Problem (Entscheidungsproblem)',breakthrough:'提出图灵机模型，证明某些数学问题不存在通用算法',breakthroughEn:'Proposed the Turing machine model, proving some mathematical problems have no general algorithm'}],
  'shannon': [{problem:'信息传输的数学量化',problemEn:'Mathematical Quantification of Information',breakthrough:'创立信息论，提出比特（bit）作为信息单位，给出信道容量公式',breakthroughEn:'Founded information theory, proposed the bit as information unit, formulated channel capacity'}],
  'crick': [{problem:'遗传信息的分子存储机制',problemEn:'Molecular Storage of Genetic Information',breakthrough:'与沃森共同发现DNA双螺旋结构，揭示遗传信息的分子基础',breakthroughEn:'With Watson, discovered the DNA double helix, revealing the molecular basis of heredity'}],
  'watson': [{problem:'遗传信息的分子存储机制',problemEn:'Molecular Storage of Genetic Information',breakthrough:'与克里克共同发现DNA双螺旋结构，揭示遗传信息的分子基础',breakthroughEn:'With Crick, discovered the DNA double helix, revealing the molecular basis of heredity'}],
  'mendeleev': [{problem:'化学元素的系统分类',problemEn:'Systematic Classification of Chemical Elements',breakthrough:'编制元素周期表，根据原子量和化学性质的周期性预言未知元素',breakthroughEn:'Created the periodic table, predicted unknown elements based on periodic properties'}],
  'lavoisier': [{problem:'燃烧的本质：燃素说之谬',problemEn:'The Nature of Combustion: Phlogiston Theory',breakthrough:'定量实验证明燃烧是氧化反应，推翻燃素说，奠定现代化学基础',breakthroughEn:'Quantitative experiments proved combustion is oxidation, overthrowing phlogiston theory'}],
  'hubble': [{problem:'旋涡星云的本质：银河系内还是河外星系',problemEn:'The Nature of Spiral Nebulae: Galactic or Extragalactic',breakthrough:'发现仙女座星云中的造父变星，确认其为独立于银河系的星系，发现哈勃定律',breakthroughEn:'Discovered Cepheid variables in Andromeda, proving it\'s a separate galaxy; discovered Hubble\'s law'}],
  'copernicus': [{problem:'托勒密地心说体系的复杂性',problemEn:'Complexity of the Ptolemaic Geocentric System',breakthrough:'提出日心说模型，将太阳置于宇宙中心，简化行星运动解释',breakthroughEn:'Proposed the heliocentric model, placing the Sun at the center, simplifying planetary motion'}],
  'hawking': [{problem:'黑洞的热力学悖论',problemEn:'The Black Hole Thermodynamics Paradox',breakthrough:'提出霍金辐射理论，证明黑洞并非完全黑暗，会发射辐射并逐渐蒸发',breakthroughEn:'Proposed Hawking radiation, proving black holes emit radiation and gradually evaporate'}],
  'penrose': [{problem:'广义相对论中奇点的物理现实性',problemEn:'Physical Reality of Singularities in General Relativity',breakthrough:'证明奇点定理，表明在广义相对论框架下黑洞奇点必然存在',breakthroughEn:'Proved the singularity theorem, showing black hole singularities are inevitable in general relativity'}],
  'nash': [{problem:'非合作博弈中的均衡策略',problemEn:'Equilibrium Strategies in Non-Cooperative Games',breakthrough:'提出纳什均衡概念，为博弈论奠定数学基础',breakthroughEn:'Proposed Nash equilibrium, laying the mathematical foundation of game theory'}],
  'von-neumann': [{problem:'可编程通用计算机的架构设计',problemEn:'Architecture Design for Programmable Computers',breakthrough:'提出冯·诺依曼架构（存储程序概念），成为现代计算机设计的基础',breakthroughEn:'Proposed the von Neumann architecture (stored-program concept), basis of modern computer design'}],
};

const controversies = {
  'einstein': [{topic:'量子力学的完备性（EPR争论）',topicEn:'Completeness of Quantum Mechanics (EPR Debate)',outcome:'爱因斯坦提出EPR佯谬质疑量子力学完备性，最终贝尔不等式的实验验证支持了量子力学的非定域性',outcomeEn:'Einstein\'s EPR paradox challenged quantum completeness; Bell\'s theorem experiments later supported quantum non-locality'}],
  'newton': [{topic:'微积分的发明优先权',topicEn:'Priority in the Invention of Calculus',outcome:'牛顿与莱布尼茨各自独立发明微积分，优先权之争持续一个世纪，最终被承认为独立发现',outcomeEn:'Newton and Leibniz independently invented calculus; the priority dispute lasted a century, now recognized as independent discovery'}],
  'leibniz': [{topic:'微积分的发明优先权',topicEn:'Priority in the Invention of Calculus',outcome:'莱布尼茨独立于牛顿发明微积分，其符号体系至今被广泛使用。英国数学界因偏袒牛顿长期落后于欧洲大陆',outcomeEn:'Leibniz independently invented calculus; his notation is still used today. England\'s favoritism toward Newton set back British mathematics'}],
  'darwin': [{topic:'自然选择与人类起源',topicEn:'Natural Selection and Human Origins',outcome:'达尔文的进化论引发科学与宗教的剧烈冲突。赫胥黎与威尔伯福斯主教在牛津辩论后，进化论逐渐被科学界接受',outcomeEn:'Darwin\'s theory sparked intense science-religion conflict. After Huxley vs Wilberforce debate, evolution was gradually accepted by science'}],
  'galileo': [{topic:'日心说与教会的冲突',topicEn:'Heliocentrism vs Church Doctrine',outcome:'伽利略因支持哥白尼日心说被宗教裁判所审判并软禁，三百多年后教会正式承认错误',outcomeEn:'Galileo was tried by the Inquisition for supporting heliocentrism and placed under house arrest; the Church later acknowledged its error'}],
  'bohr': [{topic:'量子力学的诠释之争',topicEn:'Interpretation of Quantum Mechanics',outcome:'玻尔的互补性原理与爱因斯坦的实在论立场对立。哥本哈根诠释成为主流，但争论延续至今',outcomeEn:'Bohr\'s complementarity principle vs Einstein\'s realism. The Copenhagen interpretation became mainstream, but the debate continues'}],
  'hooke': [{topic:'万有引力平方反比定律的优先权',topicEn:'Priority for the Inverse-Square Law of Gravity',outcome:'胡克声称牛顿从与他的通信中获得了平方反比定律的想法。牛顿在《原理》中未充分致谢胡克，二人关系破裂',outcomeEn:'Hooke claimed Newton got the inverse-square idea from their correspondence. Newton inadequately credited Hooke in Principia, ending their relationship'}],
  'huxley': [{topic:'进化论与宗教的大辩论',topicEn:'Evolution vs Religion Debate',outcome:'1860年牛津辩论中，赫胥黎驳斥威尔伯福斯主教的攻击，为达尔文进化论赢得关键公众支持',outcomeEn:'At the 1860 Oxford debate, Huxley refuted Bishop Wilberforce\'s attacks, winning crucial public support for Darwin\'s theory'}],
  'pasteur': [{topic:'自然发生说之争',topicEn:'The Spontaneous Generation Controversy',outcome:'巴斯德通过鹅颈瓶实验彻底否定了自然发生说，确立了微生物学的基本原理',outcomeEn:'Pasteur\'s swan-neck flask experiments definitively disproved spontaneous generation, establishing microbiology\'s foundation'}],
  'yang-zhenning': [{topic:'宇称不守恒发现中的贡献分配',topicEn:'Credit Distribution in Parity Non-Conservation Discovery',outcome:'杨振宁与李政道因宇称不守恒共同获奖，但二人的合作后来破裂，贡献占比成为争议话题',outcomeEn:'Yang and Li jointly won for parity non-conservation but later their collaboration ended, with credit distribution debated'}],
  'li-zhengdao': [{topic:'宇称不守恒发现中的贡献分配',topicEn:'Credit Distribution in Parity Non-Conservation Discovery',outcome:'李政道与杨振宁共同提出宇称不守恒，但二人合作关系在1960年代破裂，未再修复',outcomeEn:'Li and Yang jointly proposed parity non-conservation, but their collaboration ended in the 1960s and was never repaired'}],
  'heisenberg': [{topic:'量子力学的矩阵力学与波动力学之争',topicEn:'Matrix Mechanics vs Wave Mechanics',outcome:'海森堡的矩阵力学与薛定谔的波动力学最初看似对立，后被证明在数学上等价',outcomeEn:'Heisenberg\'s matrix mechanics and Schrödinger\'s wave mechanics initially seemed opposed, later proven mathematically equivalent'}],
  'schrodinger': [{topic:'量子力学的矩阵力学与波动力学之争',topicEn:'Matrix Mechanics vs Wave Mechanics',outcome:'薛定谔证明了他的波动力学与海森堡的矩阵力学在数学上等价，两种表述至今并存',outcomeEn:'Schrödinger proved his wave mechanics mathematically equivalent to Heisenberg\'s matrix mechanics; both formulations coexist'}],
};

// Apply to data
data.scientists.forEach(s => {
  if (problems[s.id]) {
    s.problemsSolved = problems[s.id].map(p => ({
      problem: p.problem, problemEn: p.problemEn,
      breakthrough: p.breakthrough, breakthroughEn: p.breakthroughEn
    }));
  }
  if (controversies[s.id]) {
    s.controversies = controversies[s.id].map(c => ({
      topic: c.topic, topicEn: c.topicEn,
      outcome: c.outcome, outcomeEn: c.outcomeEn
    }));
  }
});

const json = JSON.stringify(data, null, 2);
fs.writeFileSync('D:/applications/AI_files/sciomap/data/scientists.json', json, 'utf8');
fs.writeFileSync('D:/applications/AI_files/sciomap/data/scientists.js', '_sciomapData = ' + json + ';', 'utf8');

const probCount = data.scientists.filter(s => s.problemsSolved && s.problemsSolved.length > 0).length;
const contrCount = data.scientists.filter(s => s.controversies && s.controversies.length > 0).length;
console.log('problemsSolved added:', probCount, 'scientists');
console.log('controversies added:', contrCount, 'scientists');
