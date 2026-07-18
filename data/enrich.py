# -*- coding: utf-8 -*-
import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('D:/applications/AI_files/sciomap/data/scientists.json', encoding='utf-8') as f:
    data = json.load(f)

def enrich(sid, fields):
    for s in data['scientists']:
        if s['id'] == sid:
            s.update(fields)
            return True
    print("  [NOT FOUND]", sid)
    return False

# ═══════════════════════════════════════════
# Einstein
# ═══════════════════════════════════════════
enrich('einstein', {
  "summary": "爱因斯坦是20世纪最伟大的物理学家，提出了狭义和广义相对论，彻底改变了人类对时空、引力和宇宙的理解。他用量子概念解释了光电效应，为量子理论做出了奠基性贡献。他的质能方程E=mc²成为科学史上最著名的公式，深刻影响了核物理和宇宙学的发展方向。",
  "summaryEn": "Einstein was the greatest physicist of the 20th century. He proposed special and general relativity, fundamentally changing our understanding of space, time, gravity, and the universe.",
  "lifeStory": "爱因斯坦1879年出生于德国乌尔姆的一个犹太家庭，小时候并不显得特别聪明，但从小就对自然现象充满好奇。他在瑞士苏黎世联邦理工学院学习物理和数学，毕业后在伯尔尼的瑞士专利局担任技术员。正是在专利局工作的1905年，他发表了四篇改变物理学的论文——包括狭义相对论、光电效应、布朗运动和质能等价。此后他继续发展广义相对论（1915年），1919年日全食观测验证了其引力弯曲光线的预言，使他成为全球瞩目的科学明星。1933年因纳粹迫害移居美国，在普林斯顿高等研究院继续研究统一场论，直至1955年去世。",
  "lifeStoryEn": "Born in Germany in 1879, Einstein studied at ETH Zurich, worked as a patent clerk, and in his 'miracle year' 1905 published four groundbreaking papers. He emigrated to the US in 1933 and worked at Princeton until 1955.",
  "keyContributions": [
    { "title": "狭义相对论", "titleEn": "Special Relativity", "year": 1905, "desc": "提出所有物理定律在所有惯性参考系中形式相同，光速不变且是速度上限。统一了时间和空间为四维时空，推导出质能方程E=mc²——揭示了质量与能量的等价性，为核能利用提供了理论基础。", "descEn": "Proposed physical laws are the same in all inertial frames and light speed is constant, unifying time and space into 4D spacetime and deriving E=mc².", "type": "theory" },
    { "title": "广义相对论", "titleEn": "General Relativity", "year": 1915, "desc": "将引力解释为质量引起的时空弯曲，而非牛顿所说的'力'。预言了引力红移、光线在引力场中的弯曲以及引力波的存在。1919年日全食观测证实了星光经过太阳时的弯曲。广义相对论是现代宇宙学的基石。", "descEn": "Explained gravity as spacetime curvature by mass. Confirmed by the 1919 solar eclipse. Foundation of modern cosmology.", "type": "theory" },
    { "title": "光电效应与光量子假说", "titleEn": "Photoelectric Effect", "year": 1905, "desc": "提出光由离散的能量量子（光子）组成，成功解释了经典物理学无法解释的光电效应。因这一贡献获得1921年诺贝尔物理学奖。", "descEn": "Proposed light consists of photons, explaining the photoelectric effect. Won the 1921 Nobel Prize.", "type": "theory" }
  ],
  "famousEvents": [
    { "title": "1919年日全食验证广义相对论", "year": 1919, "desc": "英国天文学家爱丁顿率领考察队观测日全食，测量到星光经过太阳时的偏折角度与广义相对论的预言一致。爱因斯坦一夜之间成为世界级名人。", "titleEn": "1919 Solar Eclipse", "descEn": "Eddington's expedition confirmed general relativity, making Einstein a global celebrity." }
  ],
  "anecdote": "爱因斯坦小时候拿到父亲送的指南针，发现无论怎么转动指针总是指向同一个方向。他被这种'看不见的力量'深深震撼，多年后他说这件事让他第一次感受到'事物背后有某种深层的东西'。",
  "anecdoteEn": "As a child, Einstein was deeply impressed by a compass's consistent north-pointing, sensing 'something deeply hidden behind things.'",
  "aiReview": "爱因斯坦的伟大不仅在于他的具体发现，更在于他改变了科学本身的气质。他敢于追问：如果时间和空间不是绝对的会怎样？这种追问是对整个框架的重塑。最令人惊叹的是，他做出这些革命性思考时凭借的是思想实验而不是复杂设备——这是科学想象力的最高体现。他对量子力学概率解释的抗拒，虽然最终被主流抛弃，但推动了量子力学基础研究的深化，间接催生了量子信息学。",
  "aiReviewEn": "Einstein's greatness lies in reshaping scientific thinking itself. His thought experiments represent the highest scientific imagination. His resistance to quantum probability ironically deepened quantum foundations.",
  "furtherReading": [
    { "title": "《爱因斯坦传》", "type": "book", "desc": "沃尔特·艾萨克森著，最权威全面的爱因斯坦生平传记", "url": "" },
    { "title": "《相对论的意义》", "type": "book", "desc": "爱因斯坦本人的非技术性演讲集", "url": "" }
  ],
  "thoughtEvolution": "从狭义相对论到广义相对论再到统一场论，爱因斯坦的思想不断深化。他与玻尔的长期争论也推动了量子力学对自身基础的反思。"
})

# ═══════════════════════════════════════════
# Newton
# ═══════════════════════════════════════════
enrich('newton', {
  "summary": "牛顿是有史以来最具影响力的科学家之一，他的万有引力定律和运动三定律构成了经典物理学的完整框架。他与莱布尼茨分别独立发明了微积分。其著作《自然哲学的数学原理》被公认为科学史上最重要的著作——首次用数学语言系统描述了宇宙的运行规律。",
  "summaryEn": "Newton is one of the most influential scientists in history. His laws of motion and universal gravitation formed classical physics. His 'Principia' is the most important work in scientific history.",
  "lifeStory": "牛顿1643年出生于英格兰伍尔索普的一个农民家庭，是个遗腹子。1661年进入剑桥大学三一学院。1665年伦敦大瘟疫期间学校关闭，他回到家乡度过了科学史上著名的奇迹年——在此期间奠定了微积分、万有引力和光学色彩理论的基础。1669年成为剑桥大学卢卡斯数学教授。1687年出版了《自然哲学的数学原理》。晚年担任皇家学会会长，1727年去世后被安葬在威斯敏斯特大教堂。",
  "lifeStoryEn": "Born in 1643 in England, Newton had a 'miracle year' during the 1665 plague, laying foundations for calculus, gravity, and optics. He published the 'Principia' in 1687.",
  "keyContributions": [
    { "title": "万有引力定律", "titleEn": "Universal Gravitation", "year": 1687, "desc": "任何两个物体之间都存在引力，力的大小与两物体质量的乘积成正比，与距离的平方成反比。首次将天上和地下的物理现象统一在同一理论框架中，是人类思想史上最伟大的综合之一。", "descEn": "Every particle attracts every other with force proportional to mass product and inversely proportional to distance squared. Unified celestial and terrestrial physics.", "type": "theory" },
    { "title": "牛顿三定律", "titleEn": "Three Laws of Motion", "year": 1687, "desc": "惯性定律、F=ma和作用力与反作用力定律。这三条定律奠定了经典力学的完整基础。", "descEn": "The three laws of inertia, F=ma, and action-reaction form the foundation of classical mechanics.", "type": "theory" },
    { "title": "微积分", "titleEn": "Calculus", "year": 1666, "desc": "与莱布尼茨分别独立发明了微积分。牛顿的流数法侧重于物理直观，莱布尼茨的符号体系更便于运算。", "descEn": "Independently invented calculus with Leibniz.", "type": "theory" }
  ],
  "famousEvents": [
    { "title": "苹果落地的启示", "year": 1666, "desc": "牛顿在躲避瘟疫时看到苹果从树上落下，开始思考为什么苹果垂直落地而月亮不会掉下来，最终引导他提出了万有引力定律。", "titleEn": "The Apple Anecdote", "descEn": "Seeing an apple fall led Newton to contemplate gravity, eventually formulating the law of universal gravitation." }
  ],
  "anecdote": "牛顿在剑桥期间自学了欧几里得和笛卡尔的著作后，发现这些内容对他来说太平淡，直接挑战最困难的问题。在奇迹年中，他独自完成了三大发现——任何一个都足以让他名垂青史。",
  "aiReview": "牛顿同时完成了三件不同层面的工作：提出全新的物理概念、发明描述这些概念的数学工具、通过精密实验验证理论。这种三位一体的能力在科学史上极为罕见。他的绝对时空观统治物理学两百年，直到爱因斯坦才将其打破。",
  "thoughtEvolution": "牛顿的工作统一了伽利略的地面力学和开普勒的天体力学，这是科学史上第一次伟大的统一。他的方法论为后世科学家树立了范本。"
})

# ═══════════════════════════════════════════
# Darwin
# ═══════════════════════════════════════════
enrich('darwin', {
  "summary": "达尔文提出了自然选择进化论，用大量证据改变了人类对生命起源和演化的理解。《物种起源》是科学史上最重要的著作之一——它提出所有生物由共同祖先逐渐演化而来，自然选择是演化的主要机制。这一理论不仅改变了生物学，也深刻影响了哲学、社会学和人类对自身位置的认知。",
  "summaryEn": "Darwin proposed evolution by natural selection, fundamentally changing humanity's understanding of life's origins. 'On the Origin of Species' is one of the most important works in science history.",
  "lifeStory": "达尔文1809年出生于英国什鲁斯伯里的一个医生家庭。他年轻时在剑桥学习神学，但对自然科学的热爱远胜于神学。1831年他随贝格尔号开始了为期五年的环球考察——这次旅程成为他人生和科学事业的转折点。在南美、加拉帕戈斯群岛等地收集的化石和生物标本使他开始质疑物种不变论。回到英国后历经二十多年的研究和思考，1859年终于发表了《物种起源》。这本书首次出版即售罄，引起了巨大的社会反响和争议。",
  "lifeStoryEn": "Born in 1809 in England, Darwin's five-year voyage on the Beagle (1831-1836) transformed his thinking. After 20 years of research, he published 'On the Origin of Species' in 1859, sparking enormous debate.",
  "keyContributions": [
    { "title": "自然选择进化论", "titleEn": "Evolution by Natural Selection", "year": 1859, "desc": "提出所有物种通过自然选择逐渐演化：个体之间存在差异，对生存和繁殖有利的差异会在后代中积累，经过漫长的时间最终形成新物种。这一理论的核心洞见在于——复杂的生命形式不需要超自然的设计者，自然过程本身就能产生适应性。", "descEn": "Species evolve through natural selection: variations that aid survival accumulate over generations, creating new species without need for supernatural design.", "type": "theory" },
    { "title": "《物种起源》", "titleEn": "On the Origin of Species", "year": 1859, "desc": "用化石记录、地理分布、比较解剖学和胚胎学等大量证据系统阐述了进化论。这本书不仅改变了生物学，也从根本上挑战了人类在宇宙中的特殊地位。", "descEn": "Systematically presented evolution with evidence from fossils, geography, anatomy, and embryology. Changed biology and humanity's view of itself.", "type": "work" }
  ],
  "famousEvents": [
    { "title": "贝格尔号环球航行", "year": 1831, "desc": "22岁的达尔文以博物学家身份登上英国皇家海军贝格尔号，开始了历时五年的环球科学考察。他在南美洲的化石发现和加拉帕戈斯群岛上的雀鸟差异，成为他后来进化论的关键证据来源。", "titleEn": "Voyage of the Beagle", "descEn": "Darwin's five-year global voyage provided the key evidence for his theory of evolution, including fossil finds and Galapagos finches." }
  ],
  "anecdote": "达尔文是一个极其谨慎的人。他在1838年就读到了马尔萨斯的人口论并从中悟出了自然选择的机制，但他花了二十多年收集证据才敢发表。《物种起源》出版前夕，他收到了华莱士的论文——后者独立提出了几乎一模一样的理论。达尔文面临被抢发的危机，好友们安排了两篇论文同时在林奈学会宣读。",
  "anecdoteEn": "Darwin was extraordinarily cautious: he developed natural selection in 1838 but spent 20+ years gathering evidence before publishing, nearly being scooped by Wallace.",
  "aiReview": "达尔文进化论真正的革命性不在于'人是从猴子变的'（这是大众的误解），而在于它提供了一个完全自然主义的生命解释框架——不需要设计者，不需要目的，复杂的生物结构可以经由变异和选择的积累逐步形成。这一思想的影响力远远超出了生物学：它改变了我们对生命意义、人类道德和社会组织的理解方式。",
  "thoughtEvolution": "达尔文的思想建立在地质学家赖尔的均变论和林奈分类学的基础之上，经华莱士的独立发现推动而发表。孟德尔遗传学和后来的现代综合进化论弥补了达尔文不了解遗传机制的不足。"
})

# ═══════════════════════════════════════════
# Turing
# ═══════════════════════════════════════════
enrich('turing', {
  "summary": "图灵是计算机科学和人工智能之父。他提出的图灵机模型奠定了理论计算机科学的基础，成为现代计算理论的起点。二战期间他破译了德国恩尼格玛密码，对战局产生了重大影响。他还提出了图灵测试来探讨机器是否能思考的问题，开创了人工智能这一领域。",
  "summaryEn": "Turing is the father of computer science and AI. His Turing machine laid the foundation of computation theory. He broke the Enigma code during WWII and proposed the Turing test for machine intelligence.",
  "lifeStory": "图灵1912年出生于伦敦一个公务员家庭。他从小就展现出非凡的数学天赋，1931年进入剑桥大学国王学院。1936年发表了划时代的论文《论可计算数》，提出了通用图灵机概念。二战期间他在英国布莱切利园领导密码破译工作，研制了Bombe密码破译机，成功破解了德国的恩尼格玛密码。战后他设计了自动计算引擎（ACE）的蓝图，并提出了著名的图灵测试。1952年因同性恋被定罪，接受化学阉割。1954年去世，年仅41岁。2009年英国政府正式道歉，2013年获女王特赦。",
  "lifeStoryEn": "Born in 1912 in London, Turing published his landmark paper on computability in 1936. He led Enigma codebreaking at Bletchley Park during WWII. Post-war he proposed the Turing test. He was tragically persecuted for homosexuality and died in 1954.",
  "keyContributions": [
    { "title": "图灵机与可计算性理论", "titleEn": "Turing Machine", "year": 1936, "desc": "提出了一种极其简单的抽象计算模型（图灵机），证明了这种简单机器可以计算出任何可计算的问题。同时证明了停机问题的不可判定性——不存在一种通用算法能判断任意程序是否会终止。这一结果揭示了计算的本质和数学推理的内在界限。", "descEn": "Proposed an abstract computation model and proved the undecidability of the halting problem, revealing the fundamental limits of computation.", "type": "theory" },
    { "title": "破译恩尼格玛密码", "titleEn": "Breaking the Enigma Code", "year": 1943, "desc": "领导研制了Bombe密码破译机，成功破解了德军的恩尼格玛密码。据估计这项工作将二战缩短了至少两年，挽救了数百万人的生命。", "descEn": "Led the development of the Bombe codebreaking machine, breaking the Enigma code. Estimated to have shortened WWII by at least two years.", "type": "invention" },
    { "title": "图灵测试与人工智能", "titleEn": "Turing Test & AI", "year": 1950, "desc": "提出了一个著名问题：机器能思考吗？并设计了图灵测试作为判断标准——如果一台机器在对话中让人类无法分辨它是人还是机器，就应认为它具有智能。这篇论文开创了人工智能领域。", "descEn": "Proposed the Turing test as a criterion for machine intelligence, founding the field of artificial intelligence.", "type": "theory" }
  ],
  "famousEvents": [
    { "title": "布莱切利园的密码战", "year": 1943, "desc": "图灵在布莱切利园领导Hut 8团队，成功破译了德国海军的恩尼格玛密码。他的工作对战局产生了决定性影响——丘吉尔曾说图灵对二战胜利的贡献超过了任何一个人。", "titleEn": "Bletchley Park", "descEn": "Turing led Hut 8 at Bletchley Park, breaking the naval Enigma code. Churchill said his contribution to WWII exceeded anyone else's." }
  ],
  "anecdote": "图灵有个奇怪的习惯——在大瘟疫期间，他把自己的茶杯用链条锁在暖气片上以防被同事误用。他在布莱切利园骑自行车上班时，会因为花粉症戴上防毒面具——同事们早已见怪不怪。他还曾用跑步换得思考的时间，后来成为世界级的马拉松选手，最好成绩2小时46分。",
  "aiReview": "图灵的故事是科学天才与社会偏见冲突的最悲剧性案例。他对计算本质的洞察超前了他的时代几十年——通用图灵机的概念为所有现代计算机奠定了基础，而那时电子计算机还没有诞生。他用数学证明了有些问题是永远无法用算法解决的，这是对人类理性边界的深刻洞察。他因同性恋而遭受的迫害是一个民族的耻辱。幸运的是历史最终还给了他公正——2014年电影《模仿游戏》让新一代人认识了这位被辜负的天才。",
  "thoughtEvolution": "图灵的思想从数学基础（可计算性）出发，延伸到物理实现（计算机设计），再扩展到认知哲学（机器能否思考），展示了一个纯粹的理论家如何将其思想应用于现实世界。"
})

# ═══════════════════════════════════════════
# Yang Zhenning
# ═══════════════════════════════════════════
enrich('yang-zhenning', {
  "summary": "杨振宁是当代最伟大的理论物理学家之一，他与李政道因提出弱相互作用中宇称不守恒而获诺贝尔奖。但他对物理学最深远的影响是杨-米尔斯规范场论——这一理论是现代粒子物理标准模型的基石，被誉为20世纪最重要的理论物理贡献之一。",
  "summaryEn": "Yang is one of the greatest theoretical physicists of our time. He won the Nobel Prize for parity non-conservation with Lee, but his Yang-Mills theory is his most profound contribution — a cornerstone of the Standard Model.",
  "lifeStory": "杨振宁1922年出生于安徽合肥，父亲杨武之是数学家。他1938年考入西南联大，1945年赴美留学，师从费米和泰勒。1949年进入普林斯顿高等研究院，与李政道开始了长达十余年的合作。1954年与米尔斯提出了非阿贝尔规范场理论（杨-米尔斯理论）。1956年与李政道提出宇称不守恒，次年即获诺贝尔奖。1966年加入纽约州立大学石溪分校创建理论物理研究所。晚年回到中国，推动了中国科学事业的发展。",
  "lifeStoryEn": "Born in 1922 in Hefei, China, Yang studied at Southwest Associated University, went to the US in 1945, studied under Fermi. He proposed Yang-Mills theory in 1954 and won the Nobel Prize in 1957 for parity non-conservation.",
  "keyContributions": [
    { "title": "杨-米尔斯规范场论", "titleEn": "Yang-Mills Theory", "year": 1954, "desc": "与米尔斯合作提出了非阿贝尔规范场理论，将规范对称性提升为理解基本相互作用的核心原理。这一理论后来成为粒子物理标准模型的数学骨架——电磁力、弱力和强力都基于杨-米尔斯的规范原理。它被认为是20世纪继广义相对论之后最深刻的理论物理贡献。", "descEn": "With Mills, proposed non-abelian gauge field theory, making gauge symmetry the core principle for understanding fundamental forces. The foundation of the Standard Model.", "type": "theory" },
    { "title": "宇称不守恒", "titleEn": "Parity Non-conservation", "year": 1956, "desc": "与李政道共同提出，在弱相互作用中宇称不守恒——一个在长期以来被物理学界视为天经地义的对称性被打破。这个发现震惊了物理学界，次年即获诺贝尔奖，是诺奖史上最快从发现到获奖的案例之一。吴健雄用精密实验证实了这一理论。", "descEn": "With Lee, proposed that parity is not conserved in weak interactions, overturning a long-held assumption. Confirmed by Wu's experiment. Won the Nobel Prize the following year.", "type": "theory" }
  ],
  "anecdote": "杨振宁和米尔斯提出规范场理论时，两人都还是年轻的博士后。他们的论文最初被《物理评论》拒绝，理由是大过数学化、缺乏物理预测。但正是这种深刻的数学结构使它后来成为整个粒子物理的基石。杨振宁曾说这是他一生中最重要的贡献，远超诺贝尔奖的工作。",
  "aiReview": "杨振宁的科学成就呈现了一个有趣的对比：他获得诺贝尔奖的工作（宇称不守恒）是一个'即时的革命'——从一个大胆的假设到实验证实再到诺贝尔奖只用了不到两年；而杨-米尔斯理论则是一个'缓慢的革新'——提出时无人问津，经过二十多年才被逐渐认识到其深远意义。后者对物理学的影响更为深刻。这种对比提醒我们，真正伟大的科学贡献有时需要时间来显现其价值。"
})

# ═══════════════════════════════════════════
# Copernicus
# ═══════════════════════════════════════════
enrich('copernicus', {
  "summary": "哥白尼提出了日心说，推翻了统治西方一千多年的地心说体系。他的《天体运行论》引发了科学革命，从根本上改变了人类在宇宙中的位置认知。哥白尼的工作不仅是天文学的革新，更是人类思想史上的一次范式转换——它标志着人类开始用理性怀疑代替盲目接受传统权威。",
  "summaryEn": "Copernicus proposed the heliocentric model, overthrowing the geocentric system that had dominated for over a millennium. His work sparked the Scientific Revolution and changed humanity's place in the cosmos.",
  "lifeStory": "哥白尼1473年出生于波兰托伦的一个富商家庭。他在克拉科夫大学、博洛尼亚大学和帕多瓦大学学习天文学、数学和医学，接受了全面的文艺复兴教育。回到波兰后，他大部分时间在弗龙堡大教堂担任教士，利用业余时间进行天文观测和计算。他花了近三十年时间完善日心说理论，但一直犹豫是否发表——担心教会反对。1543年临终前，他的学生将《天体运行论》送到他手中，据说他在去世当天才看到了出版的样书。",
  "lifeStoryEn": "Born in 1473 in Poland, Copernicus studied astronomy and mathematics in Krakow and Italy. He worked on heliocentrism for nearly 30 years while serving as a church canon. His book was published in 1543, the year of his death.",
  "keyContributions": [
    { "title": "日心说理论", "titleEn": "Heliocentric Theory", "year": 1543, "desc": "提出太阳是宇宙的中心，地球和其他行星绕太阳旋转，同时地球每日自转一周。这一理论简洁地解释了行星的逆行运动——一个在地心说中需要借用复杂本轮系统才能解释的现象。哥白尼的日心说虽然仍保留了圆形轨道（后被开普勒修正为椭圆），但其核心思想——地球不是宇宙的中心——是人类自我认知的一次根本性颠覆。", "descEn": "Proposed the Sun as the center of the universe, with Earth rotating daily and orbiting the Sun annually. This fundamentally displaced humanity from the center of the cosmos.", "type": "theory" }
  ],
  "famousEvents": [
    { "title": "《天体运行论》的出版", "year": 1543, "desc": "哥白尼在临终前终于同意出版《天体运行论》。传说他拿到印刷好的书时已经处于弥留之际，摸了摸封面后平静地去世了。这本书的出版被视为科学革命的开端。", "titleEn": "Publication of De Revolutionibus", "descEn": "Copernicus saw the first printed copy on his deathbed in 1543. The book's publication marks the beginning of the Scientific Revolution." }
  ],
  "anecdote": "哥白尼其实不是第一个提出日心说的人——古希腊的阿里斯塔克斯早在公元前三世纪就提出了太阳中心的想法。但阿里斯塔克斯的说法没有被接受，因为当时缺乏支持它的数学和观测证据。哥白尼的伟大在于他拿出了完整的数学论证。",
  "aiReview": "哥白尼革命的意义远远超出了天文学。他的日心说引发了一个'去中心化'的思想过程：哥白尼把地球从宇宙中心移开了，达尔文把人类从生物中心移开了，弗洛伊德把自我意识从心理中心移开了。这三步环环相扣，一步步消解了人类自以为是宇宙中心的自恋心态。哥白尼革命的另一层意义在于：它证明了有时候多数人的共识（地心说已流传两千年）可以被一个人的理性论证推翻——这是科学精神最核心的价值。"
})

# ═══════════════════════════════════════════
# Mendeleev
# ═══════════════════════════════════════════
enrich('mendeleev', {
  "summary": "门捷列夫发现了元素周期律，编制了元素周期表，这是化学史上最重要的成就之一。他大胆地预言的多种元素（镓、钪、锗等）在后来逐一被发现，而且性质与他的预言高度吻合，奠定了他在科学史上的不朽地位。",
  "summaryEn": "Mendeleev discovered the periodic law and created the periodic table. He boldly predicted undiscovered elements whose properties matched his predictions almost perfectly.",
  "lifeStory": "门捷列夫1834年出生于西伯利亚托博尔斯克，是家中最小的孩子。他母亲在他父亲失明后独自经营玻璃厂支撑家庭，对他的教育极为重视。他先后在圣彼得堡大学和海德堡大学学习。1869年当他试图撰写化学教科书时，发现现有的元素知识杂乱无章，于是开始探索元素之间的规律。据说他在梦中看到了元素周期表的排列方式——醒来后立即记下，只修改了一处。他预言的三种元素（镓、钪、锗）在他在世时就被发现，全部命中。",
  "lifeStoryEn": "Born in 1834 in Siberia, Mendeleev created the periodic table in 1869 when writing a chemistry textbook. He reportedly saw the arrangement in a dream. All three elements he predicted were discovered during his lifetime.",
  "keyContributions": [
    { "title": "元素周期表与周期律", "titleEn": "Periodic Table", "year": 1869, "desc": "发现元素性质随原子量增加呈现周期性变化，将已知元素按此规律排列成表格。更令人惊叹的是，他为尚未发现的元素留下了空位，并精确预言了它们的性质和原子量。后来发现的镓、钪、锗的物理和化学性质与他的预言惊人一致——这是他理论正确性的最有力证明。", "descEn": "Discovered periodic patterns in element properties, created the periodic table with gaps for undiscovered elements. His predictions for gallium, scandium, and germanium proved remarkably accurate.", "type": "theory" }
  ],
  "anecdote": "门捷列夫是一个特立独行的人——他留着标志性的长发和胡须，据说一年只剪一次头发。他最喜欢做的事情是装订自己的书和制作手提箱。虽然他在科学上追求秩序，生活却很随意。他还有一种奇特的能力：能在长篇大论的演讲中突然停下来，在脑海中完成复杂的计算。",
  "aiReview": "门捷列夫的元素周期表是科学中'预见之美'的典范。当时许多元素尚未被发现，但他根据周期规律留下的空位和预言，就像一幅未完成拼图的轮廓——明确的、精确的、可验证的。当这些元素逐一被发现且性质与预言相符时，周期律的正确性就无可辩驳了。周期表的另一个美妙之处在于它揭示了看似杂乱无章的自然界背后隐藏着简洁的数学规律。"
})

# ═══════════════════════════════════════════
# Yuan Longping
# ═══════════════════════════════════════════
enrich('yuan-longping', {
  "summary": "袁隆平是中国杂交水稻之父，成功培育出高产杂交水稻，为解决中国和世界的粮食安全问题做出了卓越贡献。他的研究使中国水稻产量大幅提升，养活了数以亿计的人口。他一生扎根田间，被誉为'把论文写在大地上'的科学家。",
  "summaryEn": "Yuan Longping is the father of hybrid rice. He developed high-yield hybrid rice varieties that significantly increased rice production, helping feed hundreds of millions and making China food-secure.",
  "lifeStory": "袁隆平1930年出生于北京一个知识分子家庭。1949年考入西南农学院农学系。1960年代中国遭遇严重粮食短缺，袁隆平亲眼目睹了饥饿的苦难，决心从事水稻增产研究。当时遗传学界主流认为水稻是自花授粉作物，没有杂交优势。袁隆平不迷信权威，经过多年寻找，1970年在海南发现了天然雄性不育野生稻（野败），为杂交水稻研究打开了突破口。1973年成功培育出三系杂交水稻，1976年开始在全国大面积推广，使中国水稻亩产从300公斤提高到600公斤以上。",
  "lifeStoryEn": "Born in 1930 in Beijing, Yuan witnessed devastating famine in the 1960s, inspiring his life mission. He discovered a wild male-sterile rice in Hainan in 1970, leading to the first hybrid rice in 1973, doubling China's rice yields.",
  "keyContributions": [
    { "title": "杂交水稻技术", "titleEn": "Hybrid Rice Technology", "year": 1973, "desc": "在发现天然雄性不育野生稻（野败）的基础上，成功培育出三系杂交水稻。这项技术使水稻亩产从300公斤提升到600公斤以上，在中国累计推广超过6亿公顷，增产稻谷近8亿吨。杂交水稻随后在越南、印度、菲律宾等几十个国家推广。", "descEn": "Based on a wild male-sterile rice, developed three-line hybrid rice, doubling yields from 300 to 600+ kg per mu. Planted across 600+ million hectares, producing 800 million extra tons of rice.", "type": "invention" }
  ],
  "famousEvents": [
    { "title": "发现野败", "year": 1970, "desc": "袁隆平的助手李必湖在海南三亚的野生稻丛中发现了一株天然雄性不育株——被称为'野败'。这是杂交水稻研究的关键转折点，所有后续的三系杂交水稻都源于这株野生稻的基因。", "titleEn": "Discovery of Wild Abortive Rice", "descEn": "A wild male-sterile rice plant was discovered in Hainan in 1970, becoming the key that unlocked hybrid rice technology." }
  ],
  "anecdote": "袁隆平有两个著名爱好：游泳和拉小提琴。他年轻时曾在游泳比赛中获得武汉市第一名。即使在最艰苦的研究岁月里，他也会在田间休息时拉小提琴——这是他排解压力的方式。他还有一个著名的自嘲：'我这个人不属于官场，也不属于商场，只属于田头。'",
  "aiReview": "袁隆平的伟大在于他把科学研究与国计民生直接相连。在全球科学界越来越追求论文发表和影响因子的时代，袁隆平始终坚持一个朴素的信念：科学家的成就应该用实际效果来衡量。他的杂交水稻养活了数千万人，这种'生命的价值'是任何学术奖项都无法衡量的。他不是那种在实验室里推导公式的理论家，而是脚踩泥土、手捧稻穗的实干者——他证明了最伟大的科学创新可以来自最朴素的问题：怎样让人吃饱饭。"
})

# ═══════════════════════════════════════════
# Gauss
# ═══════════════════════════════════════════
enrich('gauss', {
  "summary": "高斯被誉为'数学王子'，是历史上最伟大的数学家之一。他在数论、代数、统计、几何和物理学等多个领域做出了奠基性贡献。他的《算术研究》开创了现代数论，他在微分几何、正态分布和非欧几何方面的发现深刻影响了现代科学的走向。",
  "summaryEn": "Known as the 'Prince of Mathematicians', Gauss made foundational contributions to number theory, algebra, statistics, geometry, and physics. His work shaped the course of modern science.",
  "lifeStory": "高斯1777年出生于德国不伦瑞克的一个贫穷家庭。他从小就展现出惊人的数学天赋——三岁纠正父亲的账本错误，小学时迅速解出1到100的求和问题（5050），让老师惊叹不已。在公爵的资助下进入哥廷根大学学习。18岁时发明了最小二乘法，19岁时用尺规作图解决了正十七边形的作图问题——这是两千多年来正多边形作图问题的首次突破。24岁出版了《算术研究》，树立了数论领域的里程碑。他一生在多个领域交替工作，每进入一个领域就留下深刻的贡献，然后转向下一个。",
  "lifeStoryEn": "Born in 1777 in poor family in Germany, Gauss was a child prodigy. By age 24 he published 'Disquisitiones Arithmeticae'. He worked across multiple fields, making deep contributions in each before moving to the next.",
  "keyContributions": [
    { "title": "《算术研究》", "titleEn": "Disquisitiones Arithmeticae", "year": 1801, "desc": "高斯24岁时出版的巨著，系统总结了数论的已有成果并将其推进到全新高度。这本书确立了现代数论的基本框架，其中很多概念和方法至今仍是数论研究的核心工具。", "descEn": "At age 24, Gauss published this masterpiece systematizing and advancing number theory, establishing its modern framework.", "type": "work" },
    { "title": "正态分布（高斯分布）", "titleEn": "Gaussian Distribution", "year": 1809, "desc": "在误差理论研究中发现了正态分布（也称高斯分布），给出了描述测量误差的概率分布函数。这一发现不仅是测量科学的基础，后来被广泛应用到自然科学、社会科学、金融等几乎一切涉及统计的领域，是科学史上应用最广泛的数学工具之一。", "descEn": "Discovered the normal distribution in error analysis, now the most widely used probability distribution across all of science and social science.", "type": "theory" },
    { "title": "非欧几何的先驱", "titleEn": "Non-Euclidean Geometry Pioneer", "year": 1820, "desc": "高斯独立发现了非欧几何的基本思想——即欧几里得第五公设不成立时同样可以建立自洽的几何体系。但他没有发表这项发现，因为担心保守派学者的攻击。后来罗巴切夫斯基和鲍耶独立发表了同样的结果。", "descEn": "Independently discovered non-Euclidean geometry but did not publish for fear of controversy. Lobachevsky and Bolyai later published independently.", "type": "theory" }
  ],
  "anecdote": "高斯是一个非常追求'完美'的人，他宁愿不发表也不愿发表不完美的成果。他曾有一句名言：'房子建好时脚手架应该被拆除。'这意味着他的论文中只呈现完美的推理，不愿展示探索的过程。这也导致了他在非欧几何方面的优先权被罗巴切夫斯基等人抢走——因为他一直觉得自己的研究还不够完善。",
  "aiReview": "高斯代表了数学史上一种罕见的天才类型：他不仅在一两个领域做出开创性贡献，而是横跨数论、代数、几何、分析、统计、物理等众多分支，在每个领域都留下了不可磨灭的印记。更令人惊叹的是他的工作往往超前于时代——最小二乘法、非欧几何的思想、正态分布——这些发现在他手中就已经成熟，但它们的真正价值要等到几十年甚至上百年后才被充分认识。"
})

# ═══════════════════════════════════════════
# Zhang Heng
# ═══════════════════════════════════════════
enrich('zhang-heng', {
  "summary": "张衡是中国古代最伟大的天文学家和发明家。他发明的浑天仪用水力驱动模拟天体运行，地动仪则是世界上第一台地震检测仪器。他还在数学、地理、文学和绘画方面卓有成就，是东汉时期百科全书式的天才。",
  "summaryEn": "Zhang Heng was ancient China's greatest astronomer. He invented the water-powered armillary sphere and the world's first seismoscope. He was a true Renaissance man of the Eastern Han dynasty.",
  "lifeStory": "张衡78年出生于南阳西鄂（今河南南阳），少年时即善写文章。他先后游历长安和洛阳，对天文、数学、机械产生浓厚兴趣。111年被召入朝廷担任郎中，后来两度担任太史令——负责天文历法和史书记载。正是在太史令任上，他设计制造了浑天仪（117年）和地动仪（132年）。他还精确测定了一年的长度为365.25天，并绘制了详细的天体图。张衡在文学上也有很高造诣，他的《二京赋》和《归田赋》是汉赋名篇。",
  "lifeStoryEn": "Born in 78 AD in Nanyang, Zhang Heng served as Chief Astronomer for the Eastern Han court. He built the armillary sphere (117 AD) and the seismoscope (132 AD), the world's first earthquake detector.",
  "keyContributions": [
    { "title": "浑天仪", "titleEn": "Armillary Sphere", "year": 117, "desc": "一个用水力驱动的天球模型，通过复杂的齿轮系统自动模拟日、月、星辰的运行轨迹。这是世界上最早的水动力天文仪器，展现了汉朝惊人的机械工程水平。", "descEn": "A water-powered celestial model that automatically simulated the movements of the sun, moon, and stars — the world's first hydro-powered astronomical instrument.", "type": "invention" },
    { "title": "地动仪", "titleEn": "Seismoscope", "year": 132, "desc": "世界上第一台地震检测仪器。它以铜铸成，内部设有精密的杠杆机构。当地震发生时，相应方向的龙嘴中的铜球会落入蟾蜍口中，发出声响，指示地震方向。据记载，地动仪曾成功检测到陇西地震（距洛阳约700公里），而当时洛阳毫无震感。", "descEn": "The world's first earthquake detection instrument. When an earthquake occurred, a bronze ball would drop from a dragon's mouth into a toad's mouth, indicating the quake's direction.", "type": "invention" }
  ],
  "anecdote": "张衡对机械的热爱从小就开始——他十岁时就能自己制作各种精巧的木制器械。他的地动仪在制成后第六年成功检测到陇西地震，而身在洛阳的皇帝和大臣们毫无感觉，看到铜球掉落都感到困惑，直到几天后驿站送来地震的报告。这是人类历史上第一次用仪器检测到地震。",
  "aiReview": "张衡在西方的知名度远不及他在中国的地位，这主要是因为东西方科学史叙事的不对称。然而他的成就放在世界范围内比较毫不逊色——他的浑天仪运用了当时最先进的齿轮技术，比欧洲同类仪器早了上千年；他的地动仪在原理上看是真正的科学仪器而非巫术装置。张衡的独特之处在于他不是一个纯理论家，而是一个将天文理论、数学计算和机械制造融为一体的实践天才。"
})

# ═══════════════════════════════════════════
# Save
# ═══════════════════════════════════════════
with open('D:/applications/AI_files/sciomap/data/scientists.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# ═══════════════════════════════════════════
# Galileo
# ═══════════════════════════════════════════
enrich('galileo', {
  "summary": "伽利略是现代科学的奠基人之一。他通过实验和数学方法结合的方式开创了近代物理学，用望远镜的天文发现动摇了地心说的根基。他发现了自由落体定律、惯性原理，研究了摆的等时性，被誉为'观测天文学之父'和'现代物理学之父'。",
  "summaryEn": "Galileo is one of the founders of modern science. He pioneered the experimental-mathematical method, discovered laws of free fall and inertia, and used the telescope to challenge the geocentric worldview.",
  "lifeStory": "伽利略1564年出生于意大利比萨，父亲是音乐家和数学家。他最初在比萨大学学医，但很快转向数学和自然科学。据说他在比萨斜塔上进行落体实验（真实性有争议），推翻了亚里士多德'重的物体下落更快'的论断。他发明了改进的望远镜，发现了木星的四颗卫星、金星的相位变化和月球的环形山——这些发现为哥白尼日心说提供了强有力的观测证据。他因支持日心说而触怒了教会，1633年被宗教裁判所审判并判处软禁，直到去世。三百多年后，教会才正式为他平反。",
  "lifeStoryEn": "Born in 1564 in Pisa, Galileo turned from medicine to mathematics. His telescope discoveries supported Copernican heliocentrism. He was tried by the Inquisition in 1633 and spent his final years under house arrest.",
  "keyContributions": [
    { "title": "实验科学方法", "titleEn": "Scientific Method", "year": 1600, "desc": "伽利略是第一个系统地将实验、数学推理和理论建构结合起来的人。他通过斜面实验测量物体运动，用数学公式描述观察结果，再用实验验证推导——这种'假设-演绎'方法成为现代科学的标准操作程序。他因此被公认为'科学方法之父'。", "descEn": "Galileo was the first to systematically combine experiment, mathematical reasoning, and theory — the 'hypothetico-deductive' method that became modern science's standard procedure.", "type": "theory" },
    { "title": "自由落体与惯性原理", "titleEn": "Free Fall & Inertia", "year": 1638, "desc": "通过斜面实验证明：在忽略空气阻力的情况下，所有物体无论轻重都以相同加速度下落。他还接近提出了惯性原理——物体在没有外力作用时保持匀速直线运动。这些发现为牛顿第一定律铺平了道路。", "descEn": "Proved all objects fall at the same acceleration regardless of weight, and approached the principle of inertia, paving the way for Newton's first law.", "type": "theory" },
    { "title": "天文望远镜的重大发现", "titleEn": "Telescopic Discoveries", "year": 1610, "desc": "他改进的望远镜使放大倍数达到30倍。他用望远镜发现了木星的四颗卫星（证明并非所有天体都绕地球转）、金星相位变化（支持日心说）、月球表面环形山和太阳黑子。这些发现彻底改变了人类对宇宙的认识。", "descEn": "Discovered Jupiter's moons, Venus phases, lunar craters, and sunspots with his improved telescope, fundamentally changing humanity's view of the cosmos.", "type": "discovery" }
  ],
  "famousEvents": [
    { "title": "宗教审判与被迫悔改", "year": 1633, "desc": "伽利略因支持日心说被罗马宗教裁判所审判。在酷刑威胁下，他被迫公开宣布放弃自己的学说。据传他低声说了一句'但它（地球）确实在转动'（E pur si muove）——虽然这个故事的可靠性存疑，但它完美地概括了真理在强权面前的坚韧。他被判处终身软禁，直到去世。", "titleEn": "Trial by the Inquisition", "descEn": "Galileo was forced to renounce heliocentrism under threat of torture. He spent his remaining years under house arrest." }
  ],
  "anecdote": "伽利略在比萨大学学医时，一次在教堂里观察一盏吊灯的摆动，发现无论摆动幅度大小，每次摆动的时间似乎相同。他用自己的脉搏计时，确认了摆的等时性——后来他用这一原理设计了脉搏计用于医学测量。又是一个从日常观察中产生重大科学发现的经典案例。",
  "anecdoteEn": "While in medical school, Galileo observed a swinging chandelier in a cathedral and discovered the isochronism of pendulums, later designing a pulse-meter for medical use.",
  "aiReview": "伽利略的悲剧性审判常常被视为科学与宗教的对抗象征，但这个故事比表面更复杂。伽利略的对手不仅仅是教会的保守势力，还包括当时的学术体制——那些固守亚里士多德教条的大学教授们。伽利略的深刻之处在于他改变了'什么是科学证据'的标准：从前的人们满足于引证权威（亚里士多德说），而伽利略坚持用实验和数学来说话。这个方法论革命的影响远远超出了天文学——它定义了现代科学之所以'现代'的本质特征。",
  "thoughtEvolution": "伽利略的工作连接了阿基米德的实验数学传统和牛顿的经典力学体系。他的方法论革命（实验+数学）和天文发现为科学革命提供了双重动力。"
})

# ═══════════════════════════════════════════
# Maxwell
# ═══════════════════════════════════════════
enrich('maxwell', {
  "summary": "麦克斯韦用一组优美方程统一了电学和磁学，预言了电磁波的存在并指出光本身就是电磁波。他的麦克斯韦方程组被爱因斯坦称为'自牛顿以来物理学最深刻、最丰硕的变革'。他在统计力学方面也做出了奠基性贡献。",
  "summaryEn": "Maxwell unified electricity and magnetism with a set of elegant equations, predicted electromagnetic waves, and showed light is an electromagnetic wave. Einstein called his work 'the most profound change in physics since Newton.'",
  "lifeStory": "麦克斯韦1831年出生于苏格兰爱丁堡的一个地主家庭。他从小就展现出惊人的科学天赋——14岁时就写了一篇关于椭圆曲线的论文在爱丁堡皇家学会宣读。他先后在爱丁堡大学和剑桥大学学习。1856年成为阿伯丁大学自然哲学教授。1871年成为剑桥大学首位实验物理学教授，负责筹建卡文迪什实验室。他的两大成就——电磁理论和气体动力学理论——都是在前人（法拉第、玻尔兹曼）工作的基础上，用数学完成了关键的'最后一跃'。他1879年因胃癌去世，年仅48岁，与爱因斯坦出生在同一年。",
  "lifeStoryEn": "Born in 1831 in Scotland, Maxwell was a child prodigy. He became Cambridge's first experimental physics professor and founded the Cavendish Laboratory. He died of cancer at 48, the same year Einstein was born.",
  "keyContributions": [
    { "title": "麦克斯韦方程组", "titleEn": "Maxwell's Equations", "year": 1865, "desc": "四个简洁的微分方程将电学、磁学和光学统一在一个理论框架中。他通过引入'位移电流'的概念补全了安培定律，并由此推导出电磁波的存在——波速恰等于光速，从而揭示光本身就是电磁波。这一理论被爱因斯坦称为'自牛顿以来物理学最深刻的变革'。", "descEn": "Four differential equations unifying electricity, magnetism, and optics. Predicted electromagnetic waves travel at light speed, revealing light as an electromagnetic wave.", "type": "theory" },
    { "title": "麦克斯韦-玻尔兹曼统计", "titleEn": "Maxwell-Boltzmann Statistics", "year": 1860, "desc": "给出了气体分子速度的统计分布数学表达式。这一工作是统计力学的开端，用概率方法描述了大量分子的集体行为——温度不再是神秘的'热质'，而是分子平均动能的度量。", "descEn": "Gave the mathematical expression for molecular speed distribution in gases, founding statistical mechanics and explaining temperature as average molecular kinetic energy.", "type": "theory" }
  ],
  "anecdote": "麦克斯韦有一个独特的习惯：他喜欢把正在思考的问题用诗句写下来。他的电磁理论中的一些关键洞见最初是以打油诗的形式记录在笔记本中的。他还养了一只宠物狗，据说这只狗擅长在学生们做实验时'协助'——它的尾巴曾扫翻了麦克斯韦的一个重要实验设备。",
  "anecdoteEn": "Maxwell had a unique habit of writing his scientific insights in verse. His pet dog was known to 'assist' students in the lab by occasionally knocking over experimental apparatus.",
  "aiReview": "麦克斯韦方程组的美在于其对称性和完整性——四个方程用数学语言完美描述了电和磁如何相互转化、如何产生和传播。这种'数学美'本身成为理论物理学家判断一个理论是否正确的重要标准。爱因斯坦之所以坚信相对论是正确的，部分原因正是因为它的数学形式太优美了。从这个意义上说，麦克斯韦不仅统一了电磁学，还塑造了理论物理学家的审美标准。",
  "thoughtEvolution": "麦克斯韦的理论建立在法拉第的场概念基础之上，将法拉第的物理直觉转化为精确的数学语言。他的电磁理论是后来爱因斯坦狭义相对论和现代量子场论的出发点。"
})

# ═══════════════════════════════════════════
# Archimedes
# ═══════════════════════════════════════════
enrich('archimedes', {
  "summary": "阿基米德是古代最伟大的数学家和物理学家。他在几何学方面做出了超越时代的贡献，在静力学和流体力学方面奠定了学科基础。他的许多工作（如用穷竭法计算面积和体积）在两千年后发展成为微积分，堪称古代的'牛顿'。",
  "summaryEn": "Archimedes was the greatest mathematician and physicist of antiquity. His work on geometry, statics, and hydrostatics was centuries ahead of its time. His 'method of exhaustion' foreshadowed calculus by two millennia.",
  "lifeStory": "阿基米德公元前287年出生于西西里岛的叙拉古（今意大利），是希腊化时代最伟大的科学家。他曾在亚历山大里亚求学（师从欧几里得的弟子），之后返回叙拉古专心研究。他一生沉迷于几何证明，经常在沙地上画图研究，甚至在洗澡时也不停止思考。他发明了许多实用的机械装置——螺旋提水器、复合滑轮、投石机等，但他认为这些'实用'的发明远不如纯几何理论高贵。公元前212年罗马军队攻陷叙拉古时，正在沙地上研究几何图形的阿基米德被一名罗马士兵杀死。",
  "lifeStoryEn": "Born in 287 BC in Syracuse, Archimedes studied in Alexandria and returned to Syracuse to pursue pure mathematics. He was killed by a Roman soldier in 212 BC while drawing geometric figures in the sand.",
  "keyContributions": [
    { "title": "阿基米德浮力定律", "titleEn": "Archimedes' Principle", "year": -250, "desc": "浸在流体中的物体受到向上的浮力，浮力大小等于物体排开流体的重量。传说他发现这个定律是因为在浴缸中看到了溢出的水，赤身裸体跑到街上大喊'尤里卡！'（我找到了！）。这个定律不仅是流体静力学的基础，更重要的它展示了一种关键的科学研究方法：从日常观察中抽象出普遍的数学规律。", "descEn": "The buoyant force on a submerged object equals the weight of displaced fluid. The discovery is said to have inspired his famous 'Eureka!' moment in a bathtub.", "type": "theory" },
    { "title": "杠杆原理", "titleEn": "Law of the Lever", "year": -250, "desc": "阿基米德系统阐述了杠杆平衡的数学原理：力×力臂 = 重×重臂。他有一句名言：'给我一个支点，我能撬起整个地球。'他利用复杂的滑轮系统，曾用一艘船演示了单人就能拉动满载货物的巨船。", "descEn": "Systematically described the mathematical principle of lever balance. His claim 'Give me a place to stand and I shall move the earth' captures the power of mechanical advantage.", "type": "theory" },
    { "title": "穷竭法与几何体积计算", "titleEn": "Method of Exhaustion", "year": -250, "desc": "阿基米德用穷竭法精确计算了球体、抛物面体和螺旋体的体积和表面积。他的方法本质上就是微积分中积分思想的雏形——用无穷多个小片段的累加求取整体。这项工作比牛顿和莱布尼茨早了近两千年。", "descEn": "Used the method of exhaustion to precisely calculate volumes and areas of curved shapes. This essentially foreshadowed integral calculus by nearly 2,000 years.", "type": "theory" }
  ],
  "famousEvents": [
    { "title": "阿基米德之死", "year": -212, "desc": "罗马军队攻破叙拉古时，一名士兵发现阿基米德正在沙地上画几何图形。阿基米德抬头说了一句'别踩我的圆！'——士兵一剑杀死了他。罗马统帅马塞拉斯曾下令保阿基米德性命，得知他的死讯后非常愤怒，处死了那名士兵并厚葬了阿基米德。", "titleEn": "Death of Archimedes", "descEn": "When a Roman soldier found Archimedes drawing geometric figures in the sand, he said 'Don't disturb my circles!' and was killed. The Roman general had him buried with honor." }
  ],
  "anecdote": "叙拉古国王希耶罗二世做了一顶金王冠，怀疑工匠掺了银但无法验证，请阿基米德帮忙。阿基米德在浴缸里洗澡时，看到身体入水排出了水，突然有了灵感——他跳出浴缸，赤身裸体跑上大街高喊'尤里卡！'（我找到了！）。他用等重的金子和王冠分别放入水中比较排出的水量，从而判断王冠是否掺假。这个故事虽然可能被添油加醋，但'尤里卡时刻'已成为科学突破瞬间的代名词。",
  "anecdoteEn": "The famous 'Eureka' story: while bathing, Archimedes realized he could test the purity of a gold crown by comparing water displacement. He ran naked through the streets shouting 'Eureka!'",
  "aiReview": "阿基米德最令人震惊的是他思想的超前性。他在没有微积分、没有代数符号的情况下，仅凭几何推理就达到了需要微积分才能完成的精密计算。他的'方法'（Method）一书直到1906年才被发现——在这本书中他揭示了如何用平衡法和穷竭法发现这些结果。如果古希腊的数学传统没有在黑暗时代中断，如果阿基米德'穷竭法'的思路得到延续和发展，人类可能早一千多年就发明了微积分。这提醒我们，科学的进步不仅取决于天才的思想，还取决于文明传承的连续性。"
})

# ═══════════════════════════════════════════
# Kepler
# ═══════════════════════════════════════════
enrich('kepler', {
  "summary": "开普勒提出了行星运动三大定律，精确描述了行星绕太阳运动的轨迹和速度变化。他的工作打破了'天体必须沿完美圆周运动'的古老信念，为牛顿的万有引力理论提供了关键基础。",
  "summaryEn": "Kepler formulated the three laws of planetary motion, breaking the ancient belief that celestial bodies must move in perfect circles and providing the key foundation for Newton's theory of gravitation.",
  "lifeStory": "开普勒1571年出生于德国魏尔，家境贫寒。他曾在图宾根大学学习神学和天文学，接受了哥白尼日心说的思想。1600年受邀成为第谷·布拉赫的助手——这成为他职业生涯的转折点。第谷拥有当时最精确的行星观测数据，但不愿与开普勒分享。第谷1601年去世后，开普勒利用他多年积累的数据研究火星轨道，经过长达数年的反复计算，终于在1605年发现火星的轨道是椭圆而非圆形。他先后在1609年和1619年发表了行星运动三大定律。",
  "lifeStoryEn": "Born in 1571 in Germany, Kepler became assistant to Tycho Brahe in 1600. Using Tycho's precise observations, he discovered Mars' elliptical orbit after years of calculation, formulating his three laws between 1609-1619.",
  "keyContributions": [
    { "title": "开普勒行星运动三定律", "titleEn": "Kepler's Laws", "year": 1619, "desc": "第一定律（椭圆轨道定律）：行星沿椭圆轨道绕太阳运行，太阳位于椭圆的一个焦点上。第二定律（面积定律）：行星和太阳的连线在相等时间内扫过相等的面积——即行星近日点速度快、远日点速度慢。第三定律（周期定律）：行星公转周期的平方与轨道半长轴的立方成正比。这三条定律精确描述了行星运动的几何规律，但开普勒无法解释'为什么'——这个任务留给了牛顿。", "descEn": "First law: planets move in elliptical orbits. Second: equal areas in equal times. Third: period squared proportional to semi-major axis cubed. These precisely described planetary motion, leaving 'why' for Newton.", "type": "theory" }
  ],
  "famousEvents": [
    { "title": "与第谷·布拉赫的合作", "year": 1600, "desc": "开普勒受邀成为第谷的助手。第谷是当时最杰出的观测天文学家，拥有无与伦比的精确数据。两人关系紧张——第谷不愿完全分享他的数据。第谷1601年突然去世后，开普勒接替了他的职位，并最终获得了那些珍贵的数据，在此基础上发现了行星运动定律。", "titleEn": "Collaboration with Tycho Brahe", "descEn": "Kepler worked with Tycho, the era's greatest observational astronomer. After Tycho's sudden death, Kepler inherited his precise data and derived his laws of planetary motion." }
  ],
  "anecdote": "开普勒花了四年时间计算火星的轨道，尝试了70多种不同的圆形轨道组合，每个都和第谷的观测数据有8角分的误差。最终他意识到一个革命性的可能：行星轨道可能不是圆形的。他说这8角分的误差'足以让他把整个天文学推翻重来'——他保留了第谷的数据，放弃了圆形轨道的古老教条，接受了椭圆轨道，从而发现了行星运动第一定律。",
  "anecdoteEn": "After 4 years and 70+ circular orbit calculations, each with 8 arc-minutes error, Kepler realized orbits might not be circles. He kept Tycho's data and abandoned the ancient dogma of circular motion.",
  "aiReview": "开普勒的故事是科学史上关于'精确数据如何推翻古老教条'的最佳案例。他面对的第谷观测数据与圆形轨道假设之间的8角分误差——仅相当于满月直径的四分之一——是致命的。如果第谷的观测不够精确，这个误差可能被忽略，开普勒就无法发现椭圆轨道。如果开普勒不够诚实，他可能会伪造数据来匹配圆形轨道。正是精确的数据和诚实的科学态度共同导致了革命性的发现。开普勒的三大定律是牛顿万有引力的'地面上的另一半'——后者为前者提供了动力学解释。"
})

# ═══════════════════════════════════════════
# Lavoisier
# ═══════════════════════════════════════════
enrich('lavoisier', {
  "summary": "拉瓦锡推翻了统治化学近百年的燃素说，建立了氧化学说，提出了质量守恒定律。他引入定量实验方法和系统命名法，将化学从炼金术的传统中解放出来，被誉为现代化学之父。",
  "summaryEn": "Lavoisier overthrew the phlogiston theory, established the oxidation theory, and proposed the law of conservation of mass. He introduced quantitative methods and systematic nomenclature, founding modern chemistry.",
  "lifeStory": "拉瓦锡1743年出生于巴黎一个富裕的律师家庭。他接受了当时最好的教育，很早就对科学产生兴趣。23岁时就因一篇城市照明方案获得法国科学院的金奖。他利用继承的巨额财富建立了一个当时最先进的私人实验室，装备了精密的天平和其他仪器。他在1789年发表《化学基础论》，确立了现代化学的框架。但在法国大革命期间，他因为曾是包税官的背景被革命政府逮捕，1794年5月8日被送上断头台。数学家拉格朗日感叹：'砍下他的头颅只需要一秒钟，但法国要等一百年才能再出现这样一位天才。'",
  "lifeStoryEn": "Born in 1743 in Paris, Lavoisier built an advanced private laboratory. He established modern chemistry but was executed during the French Revolution in 1794 for his tax-collector background.",
  "keyContributions": [
    { "title": "推翻燃素说，建立氧化学说", "titleEn": "Oxygen Theory", "year": 1778, "desc": "拉瓦锡通过精确的定量实验证明：燃烧不是物质释放燃素，而是物质与空气中的氧发生化合反应。他用天平称量了锡和铅在密闭容器中燃烧前后的总质量——发现总质量不变，但金属质量增加，同时容器中空气的质量减少，且减少的质量恰好等于金属增加的质量。这个实验完美地证明了质量守恒和氧化反应的实质。", "descEn": "Through precise quantitative experiments, Lavoisier proved combustion is a reaction with oxygen, not the release of phlogiston. He showed matter is neither created nor destroyed in chemical reactions.", "type": "theory" },
    { "title": "质量守恒定律", "titleEn": "Law of Conservation of Mass", "year": 1789, "desc": "拉瓦锡首次明确表述：在化学反应中，物质的总质量保持不变。这一原理看似简单，但它将化学从一门定性描述的科学转变为定量分析的科学。有了质量守恒这个锚点，化学家才能开始精确研究反应方程式和物质的组成。", "descEn": "Stated that the total mass remains constant in chemical reactions. This transformed chemistry from qualitative description to quantitative analysis.", "type": "theory" },
    { "title": "现代化学命名法", "titleEn": "Chemical Nomenclature", "year": 1787, "desc": "拉瓦锡与其他化学家合作建立了第一个系统的化学命名体系——从此化学物质有了清晰、统一的名字规则。旧时代那种随意命名（如'矾油'、'绿矾'）被系统化的名称（如硫酸、硫酸亚铁）取代，化学家们终于能使用共同的语言交流。", "descEn": "Co-created the first systematic chemical nomenclature, replacing arbitrary names like 'oil of vitriol' with systematic names like 'sulfuric acid'.", "type": "work" }
  ],
  "famousEvents": [
    { "title": "被送上断头台", "year": 1794, "desc": "拉瓦锡在大革命期间被以'反对人民的罪行'判处死刑。法庭拒绝了科学家们请求赦免的请愿。1794年5月8日被送上断头台。数学家拉格朗日说：'砍下他的头颅只需要一秒钟，但法国要等一百年才能再出现这样一位天才。'", "titleEn": "Execution", "descEn": "Lavoisier was executed during the Reign of Terror. Lagrange lamented: 'It took a second to cut off his head, but France may not produce another such mind in a century.'" }
  ],
  "anecdote": "拉瓦锡的实验室是当时欧洲最先进的科学设施——不仅配有精密天平、大型透镜和各种化学设备，还经常举办科学演示会，邀请各界名流观看他做实验。他的妻子玛丽-安娜·拉瓦锡是他最重要的合作者——她不仅协助实验，还绘制了所有实验装置的精美插图，并将英文科学文献翻译成法文供丈夫参考。",
  "anecdoteEn": "Lavoisier's laboratory was Europe's finest. His wife Marie-Anne was his crucial collaborator — she illustrated his experiments, translated scientific papers, and managed his correspondence.",
  "aiReview": "拉瓦锡的悲剧在于他一方面用科学为人类创造了知识，另一方面他作为包税官的身份让他卷入了吸血的社会制度。革命不分青红皂白地消灭了他，而在他死后不到几年，法国又需要他的化学体系来指导火药和染料的生产。拉瓦锡的历史地位犹如化学界的哥白尼——他把化学从炼金术的世界观中解放出来，引入了精确测量的方法。他的一句话至今仍是科学的座右铭：'我们从不偏离事实，即使是最微小的事实。'"
})

# ═══════════════════════════════════════════
# Curie
# ═══════════════════════════════════════════
enrich('curie', {
  "summary": "居里夫人是放射性研究的先驱，也是历史上第一位两次获得诺贝尔奖的科学家（物理奖和化学奖）。她发现了钋和镭两种放射性元素，开创了核物理和放射化学的新领域。她在男性主导的科学界以非凡的毅力和才华打破了性别壁垒。",
  "summaryEn": "Marie Curie was a pioneer of radioactivity research, the first person to win two Nobel Prizes (Physics and Chemistry). She discovered polonium and radium, opening new fields of nuclear physics and radiochemistry.",
  "lifeStory": "居里夫人1867年出生于波兰华沙一个教师家庭，原名玛丽亚·斯克沃多夫斯卡。当时波兰处于俄国统治下，女性上大学受到严格限制。她与姐姐约定先工作支持姐姐学医，等姐姐毕业后反过来帮她。1891年她移居巴黎，进入索邦大学学习物理和化学。她在简陋的条件下刻苦学习，经常因营养不良而昏倒。1894年结识皮埃尔·居里，次年结婚。夫妇二人共同研究放射性现象，1898年发现钋和镭。1903年共同获得诺贝尔物理学奖。1911年她因分离纯镭获诺贝尔化学奖。一战期间她亲自驾驶X光车到前线救治伤员。她因长期接触放射性物质，1934年因再生障碍性贫血去世。",
  "lifeStoryEn": "Born in 1867 in Warsaw, Curie moved to Paris in 1891 to study at the Sorbonne. She married Pierre Curie in 1895. Together they discovered polonium and radium. She won Nobel Prizes in 1903 (Physics) and 1911 (Chemistry).",
  "keyContributions": [
    { "title": "放射性研究", "titleEn": "Radioactivity Research", "year": 1903, "desc": "居里夫人系统研究了当时刚被贝克勒尔发现的'铀射线'现象，首次提出了'放射性'这一术语。她发现放射性是原子本身的属性（而非化学反应），这一发现动摇了'原子不可分'的传统观念，为后来揭示原子内部结构打开了大门。", "descEn": "Systematically studied uranium rays, first used the term 'radioactivity', and showed it is an atomic property — shaking the foundation of the 'indivisible atom' concept.", "type": "discovery" },
    { "title": "发现钋和镭", "titleEn": "Discovery of Polonium & Radium", "year": 1898, "desc": "从数吨沥青铀矿中奇迹般地分离出两种新放射性元素——钋（为纪念她的祖国波兰命名）和镭。她和丈夫在简陋的棚户实验室里工作了四年，处理了八吨铀矿残渣，才提取了十分之一克的纯镭。她拒绝为镭的提纯技术申请专利，将其无偿提供给全世界使用。", "descEn": "Isolated two new elements from tons of pitchblende in a crude shed laboratory. She refused to patent the radium extraction process, giving it freely to the world.", "type": "discovery" }
  ],
  "famousEvents": [
    { "title": "两次诺贝尔奖", "year": 1911, "desc": "居里夫人1903年与丈夫皮埃尔·居里和贝克勒尔共同获得诺贝尔物理学奖，1911年独自获得诺贝尔化学奖。她是历史上第一位两次获得诺贝尔奖的科学家。但她的成就也曾被性别歧视阴影笼罩——1903年提名时法国科学院甚至没有将她列入候选人名单，是皮埃尔坚持才将她加入。", "titleEn": "Two Nobel Prizes", "descEn": "Curie won the 1903 Nobel in Physics (with Pierre Curie and Becquerel) and the 1911 Nobel in Chemistry, the first person to win two Nobel Prizes." }
  ],
  "anecdote": "居里夫人的实验室条件极为简陋——她工作的'实验室'原本是一个废弃的解剖室，屋顶漏雨，温度冬天只有6°C。她就在这个棚屋里处理成吨的沥青铀矿，用一根几乎和自己一样高的铁棒搅拌沸腾的化学溶液，同时忍受着刺鼻的烟雾。她后来回忆说：'有时我不得不中断工作，跑到外面去喘口气。'但在她的日记里，她称那段岁月是'我生命中最美好、最快乐的时光'。",
  "anecdoteEn": "Curie worked in a abandoned dissecting room that leaked rain, had no ventilation, and reached 6°C in winter. She processed tons of pitchblende there by hand, later calling it 'the best and happiest time of my life.'",
  "aiReview": "居里夫人的一生充满了矛盾与超越：她出身被压迫的波兰，在异国他乡以女性身份闯入了最精英的科学殿堂；她发现了放射性（这个词也是她创造的），却因长期接触放射性物质而去世；她获得了至高无上的科学荣誉，却仍然被科学界主流边缘化——1911年她申请法国科学院院士被拒，因为她是女性。她的伟大不仅在于科学成就，更在于她用行动证明了：科学的能力与性别无关，真理的追求不分国界。"
})

# ═══════════════════════════════════════════
# Mendel
# ═══════════════════════════════════════════
enrich('mendel', {
  "summary": "孟德尔通过豌豆杂交实验发现了遗传学的基本定律，成为现代遗传学的奠基人。他揭示了生物的性状由离散的遗传因子（基因）控制，并提出了分离定律和自由组合定律。他的工作在生前被完全忽视，去世16年后才被重新发现。",
  "summaryEn": "Mendel discovered the fundamental laws of heredity through pea experiments, founding modern genetics. He revealed that traits are controlled by discrete hereditary factors (genes) through the laws of segregation and independent assortment.",
  "lifeStory": "孟德尔1822年出生于奥地利的一个农民家庭。他曾在奥尔米茨大学学习哲学和物理学，后因经济原因进入布尔诺的圣托马斯修道院成为修道士。1851年被派往维也纳大学学习自然科学——这四年是他科学思想形成的关键时期。1856年起他在修道院的花园里开始豌豆杂交实验，到1863年共研究了约28,000株豌豆植株，系统记录了7对性状的遗传规律。1865年他在布尔诺自然历史学会上宣读了他的发现，但听众反应冷淡。1866年论文发表后几乎无人问津。孟德尔1884年去世时，他的工作几乎完全被世界遗忘。直到1900年，三位科学家（德弗里斯、科伦斯、切尔马克）各自独立得到了相同的结果，才重新发现了孟德尔的论文——这时世界才意识到这份工作的革命性意义。",
  "lifeStoryEn": "Born in 1822 in Austria, Mendel became an Augustinian monk. He conducted pea experiments from 1856-1863, studying ~28,000 plants. His 1865 findings were ignored. Rediscovered in 1900 by three scientists independently, posthumously recognized as the father of genetics.",
  "keyContributions": [
    { "title": "孟德尔遗传定律", "titleEn": "Mendelian Inheritance", "year": 1866, "desc": "孟德尔通过精心设计的豌豆杂交实验，揭示了两个基本遗传规律：分离定律（每个个体携带一对遗传因子，配子形成时成对的因子分离，每个配子只携带其中的一个）和自由组合定律（不同性状的遗传因子独立分配到配子中）。这些简洁的数学比例关系——3:1、9:3:3:1——证明了遗传是离散粒子的传递而非融合式的混合。", "descEn": "Through careful pea experiments, Mendel revealed the laws of segregation and independent assortment. The discrete 3:1 and 9:3:3:1 ratios proved heredity is particulate, not blending.", "type": "theory" }
  ],
  "famousEvents": [
    { "title": "孟德尔论文的重新发现", "year": 1900, "desc": "孟德尔的论文被埋没了34年后，1900年荷兰的德弗里斯、德国的科伦斯和奥地利的切尔马克三位植物学家在各自独立研究中都得出了与孟德尔相同的结论。当他们在查阅文献时惊讶地发现了孟德尔35年前的论文——这位默默无闻的修道士早已给出了他们辛苦得到的全部答案。", "titleEn": "Rediscovery of Mendel's Work", "descEn": "In 1900, three scientists independently rediscovered Mendel's laws while searching literature, realizing the humble monk had already provided all the answers 35 years earlier." }
  ],
  "anecdote": "孟德尔选择豌豆作为实验材料是经过深思熟虑的——豌豆有清晰的性状（如圆粒/皱粒、黄子叶/绿子叶）、严格的自花授粉、世代周期短。他研究的第一步并不是种豌豆，而是花了两年时间筛选了34个品种，确保它们都是'纯种'。他在修道院花园里种了那块著名的3米×35米的实验田，这个面积恰好够他种植和统计数万株植株——不多不少，完美匹配他需要的数据量。",
  "anecdoteEn": "Mendel spent 2 years selecting 34 pea varieties to ensure pure lines. His experimental plot was exactly 3m x 35m — just the right size to grow and count the thousands of plants he needed.",
  "aiReview": "孟德尔的故事是科学史上'超前于时代'的最典型悲剧。他的实验设计之精巧、数据分析之严谨、论文写作之清晰，即使在今天看来也是高质量的科学研究。但当时的生物学界还没有准备好接受'用数学描述生命'——人们普遍认为生物过于复杂，不可能有数学规律。孟德尔的同时代人说他是'修道士在花园里的消遣'，而不知道这个消遣奠定了一门新学科的基础。他的重新发现是科学史上最激动人心的'迟到正义'——将近半个世纪后，世界终于追上了这位孤独修道士的视野。"
})

# ═══════════════════════════════════════════
# Von Neumann
# ═══════════════════════════════════════════
enrich('von-neumann', {
  "summary": "冯·诺依曼是20世纪最全面的天才之一。他在计算机架构（冯·诺依曼架构）、博弈论、量子力学、核物理和数学等多个领域都做出了开创性贡献。他的思想速度之快和领域之广，让所有认识他的人都叹为观止。",
  "summaryEn": "Von Neumann was one of the most versatile geniuses of the 20th century, making pioneering contributions to computer architecture, game theory, quantum mechanics, nuclear physics, and mathematics.",
  "lifeStory": "冯·诺依曼1903年出生于匈牙利布达佩斯的一个犹太银行家家庭。他从小就展现出惊人的智力——6岁就能心算八位数除法，8岁掌握微积分，不到20岁就发表了多篇重要数学论文。他先后在柏林大学和汉堡大学任教，1930年受邀到普林斯顿大学，成为普林斯顿高等研究院最早的六位教授之一（与爱因斯坦同事）。二战期间他参与了曼哈顿计划，为原子弹研制提供了关键计算。战后他提出了存储程序计算机的架构设计（冯·诺依曼架构），这一概念奠定了所有现代计算机的基础。他还创立了博弈论和细胞自动机理论。1957年因癌症去世。",
  "lifeStoryEn": "Born in 1903 in Budapest, von Neumann was a child prodigy. He joined Princeton's Institute for Advanced Study, worked on the Manhattan Project, proposed the stored-program computer architecture (von Neumann architecture), and founded game theory.",
  "keyContributions": [
    { "title": "冯·诺依曼架构", "titleEn": "von Neumann Architecture", "year": 1945, "desc": "提出了存储程序计算机的设计思想：程序和数据以同样的方式存储在内存中，CPU依次从内存中取出指令并执行。这种'程序存储'的概念使计算机变得通用而灵活——只需改变内存中的程序而不必更改硬件，即可执行不同的任务。今天几乎所有计算机（从手机到超级计算机）都基于这一架构。", "descEn": "Proposed the stored-program computer design: programs and data share the same memory. This made computers general-purpose — change the program, not the hardware. Still the basis of virtually all computers today.", "type": "invention" },
    { "title": "博弈论", "titleEn": "Game Theory", "year": 1944, "desc": "与奥斯卡·摩根斯坦合著《博弈论与经济行为》，系统建立了博弈论的数学框架。他们定义了零和博弈、最小最大定理等核心概念，证明了在零和博弈中总存在一个最优混合策略。博弈论后来广泛应用于经济学、政治学、生物学和计算机科学。", "descEn": "With Morgenstern, wrote 'Theory of Games and Economic Behavior', establishing game theory's mathematical framework including the minimax theorem.", "type": "theory" },
    { "title": "曼哈顿计划的数学贡献", "titleEn": "Manhattan Project Contributions", "year": 1945, "desc": "冯·诺依曼为原子弹研制解决了关键的数学问题——如何用数学模拟内爆式核反应。他提出用聚焦的炸药透镜来压缩钚核心，这一设计直接用于'胖子'原子弹（投在长崎）。他还用早期的计算机进行了大量核反应模拟计算。", "descEn": "Solved critical mathematical problems for the atomic bomb, including the implosion lens design used in the 'Fat Man' bomb dropped on Nagasaki.", "type": "theory" }
  ],
  "famousEvents": [
    { "title": "普林斯顿的智力魔王", "year": 1940, "desc": "冯·诺依曼的智力在普林斯顿是传奇级别的。他曾受邀在同事家的聚会上讲笑话，但讲完之后补充说:'我刚才那个笑话的数学公式其实是这样的…'然后拿出纸笔开始推导。在曼哈顿计划期间，他能在脑子里完成复杂的核反应计算，而其他人需要花几天来验算。物理学家贝特曾说:'我有时觉得冯·诺依曼的大脑根本不是人类的大脑，而是超人的。'", "titleEn": "The Genius of Princeton", "descEn": "Von Neumann's intellect was legendary. Colleagues at the Manhattan Project said he could perform complex nuclear calculations entirely mentally while others took days." }
  ],
  "anecdote": "冯·诺依曼的驾驶技术和他的数学能力形成鲜明反差——他出过无数次车祸，每次都在同一地点。他的妻子建议他在那个路口减速时，他说:'不，问题不是我需要减速，而是那个弯道本身设计不合理，让我来算算最佳转弯半径应该是多少。'——然后他真的拿出纸笔计算了起来。",
  "anecdoteEn": "Von Neumann was famously a terrible driver who crashed repeatedly at the same curve. When his wife suggested slowing down, he instead calculated the optimal turning radius mathematically.",
  "aiReview": "冯·诺依曼的独特之处在于他的思维速度——不是'快一点点'，而是快到让周围人觉得他来自另一个星球。他在完全不同的领域中切换时不需要'热身'，可以在讨论了10分钟量子力学后立刻转向博弈论，再用10分钟解决一个工程问题。他的同事乌拉姆曾评价:'冯·诺依曼是所有认识他的人之中唯一一个让我确信他拥有超人的智力的——不是比你聪明一点点，而是完全另一个级别。'然而他的悲剧在于，他清楚地看到了核武器竞争的方向，1940年代就开始担忧人类会毁于自己发明的技术——这种担忧在他后期的言论中越来越频繁。"
})

# ═══════════════════════════════════════════
# Chen Shengshen
# ═══════════════════════════════════════════
enrich('chen-shengshen', {
  "summary": "陈省身是20世纪最杰出的微分几何学家之一，被誉为'微分几何之父'。他提出的陈类和陈-韦伊理论深刻影响了现代数学和理论物理，在代数拓扑和规范场论中有着基础性作用。他是首位获得沃尔夫数学奖的华人数学家。",
  "summaryEn": "Chern was one of the greatest differential geometers of the 20th century, known as the 'father of differential geometry.' His Chern classes and Chern-Weil theory profoundly influenced modern mathematics and theoretical physics.",
  "lifeStory": "陈省身1911年出生于浙江嘉兴。他1926年考入南开大学数学系，师从姜立夫。1930年进入清华大学研究院，1934年赴德国汉堡大学攻读博士，师从著名几何学家布拉施克。1936年完成关于微分几何的博士论文，随后赴巴黎跟随嘉当深造——嘉当是当时最伟大的微分几何学家。1943年受邀到普林斯顿高等研究院，在那里完成了陈类的奠基性工作。1949年赴美，先后在芝加哥大学和加州大学伯克利分校任教，将伯克利打造成世界微分几何研究中心。1984年退休后回到中国，创办南开数学研究所。2004年去世。",
  "lifeStoryEn": "Born in 1911 in Jiaxing, China, Chern studied at Nankai and Tsinghua, earned his PhD at Hamburg, studied under Cartan in Paris. He did his landmark work at Princeton in 1943, later built Berkeley into a geometry powerhouse, and founded Nankai Institute in China.",
  "keyContributions": [
    { "title": "陈类", "titleEn": "Chern Classes", "year": 1944, "desc": "陈类是一种拓扑不变量——它刻画了向量丛的'扭曲程度'，是微分几何和代数拓扑中的基本工具。陈类不仅在现代数学中无处不在（从代数几何到微分拓扑），还意外地成为了理论物理的强大工具——杨-米尔斯规范场论中规范场的拓扑性质正好用陈类来描述。陈省身本人曾幽默地说:'我做了多年的微分几何，没想到被物理学家用上了。'", "descEn": "Chern classes are topological invariants describing how vector bundles are twisted. They are fundamental in modern mathematics and unexpectedly became crucial tools in Yang-Mills gauge theory physics.", "type": "theory" },
    { "title": "陈-韦伊理论", "titleEn": "Chern-Weil Theory", "year": 1950, "desc": "与韦伊合作建立了微分几何中曲率与拓扑之间的深刻联系。这一理论用曲率形式来刻画拓扑不变量，将局部的几何量（曲率）与全局的拓扑结构联系了起来。它统一了几何、拓扑和代数的若干分支，是20世纪数学最有影响力的成果之一。", "descEn": "With Weil, established a deep connection between curvature and topology, using local geometric data (curvature) to compute global topological invariants.", "type": "theory" }
  ],
  "famousEvents": [
    { "title": "普林斯顿的突破", "year": 1943, "desc": "陈省身在普林斯顿高等研究院工作期间，发表了关于'闭流形上高斯-博内定理的内蕴证明'的论文——这正是陈类概念的出发点。在普林斯顿期间他与爱因斯坦有过交谈——爱因斯坦对微分几何很感兴趣，因为那是广义相对论的数学语言。陈省身后来说，与爱因斯坦的对话让他看到几何学在物理学中的巨大潜力。", "titleEn": "Breakthrough at Princeton", "descEn": "At Princeton's IAS, Chern published his intrinsic proof of the Gauss-Bonnet theorem, the starting point for Chern classes. He discussed geometry with Einstein, seeing geometry's potential in physics." }
  ],
  "anecdote": "陈省身对'数学之美'有独到的感悟。他曾说学数学就像读一首诗——表面上看到的是符号和公式，但真正感受到的是其中蕴藏的韵律和结构。他在普林斯顿期间经常与爱因斯坦交流，爱因斯坦赞叹'数学的简洁是物理真理的标志'，陈省身则回答说: '几何的简洁是自然之美在数学中的投影。'他的南开数学研究所在成立时，他题写了'数学好玩'四个字——这朴素的口号中蕴含了他终生的数学哲学。",
  "anecdoteEn": "Chern saw mathematics as poetry. He discussed geometry with Einstein at Princeton and later inscribed 'Mathematics is fun' at Nankai Institute — a simple motto reflecting his lifelong philosophy.",
  "aiReview": "陈省身是华人数学家在世界数学殿堂达到最高地位的象征。陈类概念像一粒种子——最初看起来纯粹是深奥的几何理论，后来却在粒子物理和弦论中长成了参天大树。这深刻揭示了'纯数学'与'应用'之间不定期的美妙关系：最抽象、最无用的数学往往在几十年后成为描述物理世界最根本的语言。陈省身说:'数学没有诺贝尔奖，但数学的价值不需要诺贝尔奖来证明。'"
})

# ═══════════════════════════════════════════
# Li Shizhen
# ═══════════════════════════════════════════
enrich('li-shi-zhen', {
  "summary": "李时珍是中国古代最伟大的药物学家和博物学家。他历时27年编纂的《本草纲目》收录1892种药物、11096个药方，是中国古代医学和博物学的集大成之作，被誉为'东方药物学巨典'。",
  "summaryEn": "Li Shizhen was ancient China's greatest pharmacologist and naturalist. His 27-year work 'Compendium of Materia Medica' catalogued 1,892 drugs and 11,096 prescriptions, a monumental achievement in Eastern medicine.",
  "lifeStory": "李时珍1518年出生于湖北蕲春的一个医生世家。他14岁考中秀才，但后来三次乡试落榜，遂放弃科举专心学医。他在行医过程中发现当时的本草书（药物学著作）存在大量错误和混乱——有些药物名称相同但功效不同，有些同名异药，有些分类错误。他决心重新编纂一部准确的本草著作。1552年开始编写《本草纲目》，为了获取准确的第一手资料，他远涉深山田野进行实地考察，亲自采摘、尝试验证各种药材。他走遍了湖北、江西、安徽、江苏等地，向农民、樵夫、渔夫和猎人请教。经过三次大修改，1578年终于在61岁时完成了这部190万字的巨著。但直到他去世后的1596年才得以出版。",
  "lifeStoryEn": "Born in 1518 in Qichun, Li failed the imperial exams three times and turned to medicine. Noticing errors in existing herbals, he spent 27 years traveling China to personally verify medicinal materials, completing the 1.9-million-word Compendium in 1578.",
  "keyContributions": [
    { "title": "《本草纲目》", "titleEn": "Compendium of Materia Medica", "year": 1578, "desc": "全书52卷，收录药物1892种（其中新增药物374种），附方11096个，配有精美插图1160幅。李时珍对药物进行了科学分类——按照'从贱到贵'的原则，分为水、火、土、金石、草、谷、菜、果、木、服器、虫、鳞、介、禽、兽、人共16部60类。这种分类方法比西方林奈的分类体系早了近200年。书中还纠正了前人著作中的大量错误。", "descEn": "52 volumes, 1,892 drugs (374 newly added), 11,096 prescriptions, 1,160 illustrations. His classification system preceded Linnaeus by nearly 200 years. Corrected numerous errors in earlier herbals.", "type": "work" }
  ],
  "famousEvents": [
    { "title": "二十七年的修书之路", "year": 1578, "desc": "李时珍1552年立下修书之志时年仅34岁。他一方面行医养家，一方面利用一切空闲时间搜集资料。为了核实一种药物，他可能要走几百里山路。他的笔记和标本堆满了书房。三次大规模修改——第一次完成时发现分类不够合理，第二次完成时发现遗漏了大量民间偏方，第三次才最终定稿。这27年间他经历了丧父之痛、贫困之困、疾病之苦，但始终没有放弃。", "titleEn": "27 Years of Dedication", "descEn": "Li spent 27 years writing the Compendium, enduring poverty, illness, and family loss. He personally verified every herb, traveling thousands of miles and revising the entire work three times." }
  ],
  "anecdote": "李时珍为了验证曼陀罗花的麻醉效果，亲自服用后进行试验。他在服下曼陀罗花后，记录了自己失去痛觉的过程和恢复后的感受，并详细描述了不同剂量下的效果差异。这种'自身试药'的精神在当时的中国极为罕见——更接近于现代药物临床试验的基本理念。",
  "anecdoteEn": "Li personally tested the anesthetic properties of Datura flowers by ingesting them, carefully recording the dose-dependent effects, a rare example of self-experimentation in medical history.",
  "aiReview": "李时珍的伟大在于他打破了古代学者'重文轻实'的传统——他不是满足于在书房里翻阅古籍、抄写前人的说法，而是亲自走进山野，去核实每一条记载。他的工作方法是真正的科学精神：观察、采集、验证、分类、记录。在西方，直到文艺复兴之后才逐渐建立起这种实证传统。李时珍与欧洲文艺复兴几乎是同时代的——他1518年出生时，哥白尼还是5岁的孩子；他去世时，伽利略已经22岁。东西方在地球两端各自进行着知识体系的革命。"
})

# ═══════════════════════════════════════════
# Euclid
# ═══════════════════════════════════════════
enrich('euclid', {
  "summary": "欧几里得是几何学之父，其《几何原本》以公理化的方法系统整理了古希腊的几何知识。这部著作在两千多年间一直是西方数学教育的标准教科书，其公理化的思想方法深刻影响了整个科学的发展。",
  "summaryEn": "Euclid is the father of geometry. His 'Elements' systematized Greek geometry through the axiomatic method, serving as the standard mathematics textbook for over 2,000 years.",
  "lifeStory": "欧几里得约公元前325年出生于古希腊，活跃于亚历山大里亚——当时希腊世界的学术中心。关于他的生平我们知之甚少——他可能在雅典受柏拉图的弟子们教育，后来应托勒密一世之邀在亚历山大里亚从事教学和研究。他的《几何原本》共13卷，包含了465个命题，全部从5条公设和5条公理出发推导而来。据说托勒密一世曾问欧几里得是否有更简便的学习几何的方法，欧几里得回答：'几何无王者之路。'这部著作在西方手抄流传了上千年，其印刷版本的数量仅次于《圣经》。",
  "lifeStoryEn": "Euclid lived around 325 BC in Alexandria. Almost nothing is known of his personal life. His 'Elements' derived 465 propositions from just 5 postulates and 5 axioms. It was second only to the Bible in number of printed editions.",
  "keyContributions": [
    { "title": "《几何原本》", "titleEn": "Elements", "year": -300, "desc": "13卷巨著，从5条公设和5条公理出发，用严格的逻辑推理推导出465个几何命题。这种公理化方法——从少数不证自明的公理出发，通过纯逻辑推理建构整个知识体系——成为后世一切科学理论的范本。爱因斯坦曾说：'如果欧几里得未能点燃你少年时代的热情，那你天生就不是科学思想家。'", "descEn": "13 books deriving 465 propositions from 5 postulates and 5 axioms. This axiomatic method became the template for all scientific theories. Einstein: 'If Euclid didn't kindle your youthful enthusiasm, you were not born to be a scientific thinker.'", "type": "work" },
    { "title": "公理化方法", "titleEn": "Axiomatic Method", "year": -300, "desc": "欧几里得的最大贡献不在于具体的几何定理（大多由前人发现），而在于他首创的公理化方法——从一个简洁的公理体系出发，严谨地推导出整个理论大厦。这种方法后来被牛顿（《自然哲学的数学原理》）、斯宾诺莎（《伦理学》）乃至现代数学（希尔伯特的公理化纲领）所继承，是科学思维的基石。", "descEn": "Euclid's greatest contribution was not specific theorems but the axiomatic method: deriving an entire system from a compact set of axioms. This method shaped Newton, Spinoza, and all of modern mathematics.", "type": "theory" }
  ],
  "anecdote": "欧几里得最有名的轶事来自他对托勒密一世说的那句'几何无王者之路'——意思是学习几何没有捷径，无论你是国王还是平民，都必须一步步走完证明的逻辑链条。还有一个故事说，一个学生刚背下第一个定理就问欧几里得：'学这个能赚多少钱？'欧几里得生气地对仆人说：'给他三枚钱币，因为他想在学习中获得实际利益。'",
  "anecdoteEn": "Euclid told King Ptolemy I: 'There is no royal road to geometry.' When a student asked what profit geometry would bring, Euclid gave him coins and dismissed him.",
  "aiReview": "欧几里得的《几何原本》在科学史上的地位怎么强调都不为过。它不仅是一本几何教材——它是人类文明中第一个完整的、自洽的、从基本原理出发演绎出来的知识体系。这种'欧几里得式建构'定义了什么叫'科学的证明'。爱因斯坦将广义相对论建立在非欧几何之上时，他使用的依然是欧几里得式的公理化语言。直到今天，数学家们证明定理时，潜意识里遵循的还是欧几里得在两千三百年前设定的范式。"
})

# ═══════════════════════════════════════════
# Bohr
# ═══════════════════════════════════════════
enrich('bohr', {
  "summary": "玻尔是量子力学的核心奠基人之一，提出了原子结构模型和互补原理。他是哥本哈根学派的领袖，围绕量子力学的解释问题与爱因斯坦展开了科学史上最著名的哲学争论。",
  "summaryEn": "Bohr was a central founder of quantum mechanics. He proposed the atomic model and complementarity principle, led the Copenhagen school, and engaged in the famous debate with Einstein on quantum interpretation.",
  "lifeStory": "玻尔1885年出生于丹麦哥本哈根的一个教授家庭。1911年在剑桥大学卡文迪什实验室和曼彻斯特大学卢瑟福指导下研究原子结构。1913年提出了玻尔原子模型——电子在分立的能级轨道上绕核运动，跃迁时发射或吸收特定频率的光。这个模型成功解释了氢原子光谱的里德伯公式，是量子理论的早期重大胜利。1921年在哥本哈根创建了理论物理研究所（后更名尼尔斯·玻尔研究所），吸引了世界各地最优秀的年轻物理学家。他提出了互补原理——粒子的波动性和粒子性是互补、互斥的描述。1927年起与爱因斯坦就量子力学的完备性展开长期争论。二战期间他从纳粹占领的丹麦逃往美国，参与了原子弹的研制，但战后公开呼吁和平控制核武器。",
  "lifeStoryEn": "Born in 1885 in Copenhagen, Bohr proposed his atomic model in 1913. He founded the Copenhagen Institute, which became the world center for quantum physics. His famous debates with Einstein on quantum mechanics spanned decades.",
  "keyContributions": [
    { "title": "玻尔原子模型", "titleEn": "Bohr Model", "year": 1913, "desc": "提出电子在离散的能级轨道上绕原子核运动，当电子从一个能级跃迁到另一个能级时发射或吸收对应能量的光子。这个模型成功解释了氢原子的光谱线系——当时的实验光谱学数据突然有了一个完美的理论解释。虽然这个模型后来被更完备的量子力学取代，但它率先引入了'量子化条件'的概念，是经典向量子过渡的关键一歩。", "descEn": "Proposed electrons occupy discrete energy levels; jumping between levels emits/absorbs photons. Explained hydrogen's spectrum. It was the crucial bridge from classical to quantum physics.", "type": "theory" },
    { "title": "互补原理", "titleEn": "Complementarity Principle", "year": 1927, "desc": "玻尔提出，微观世界的粒子表现出波和粒子两种互斥但互补的图像。根据实验设置的不同，光可以是波（干涉实验）或粒子（光电效应），两者不能同时被观察到，但都是对同一实在的完整描述所必需的。这一原理是量子力学哥本哈根诠释的核心哲学思想。", "descEn": "Microscopic objects exhibit mutually exclusive yet complementary wave and particle behaviors. Both are necessary for a complete description, forming the philosophical core of the Copenhagen interpretation.", "type": "theory" }
  ],
  "famousEvents": [
    { "title": "与爱因斯坦的世纪争论", "year": 1930, "desc": "从1927年索尔维会议开始，玻尔和爱因斯坦就量子力学的解释展开了长达数十年的争辩。爱因斯坦不断设计思想实验试图证明量子力学不完备，玻尔每次都能指出其中的漏洞。最有名的是1930年索尔维会议上爱因斯坦设计的'光子盒'实验——玻尔彻夜未眠，最终用爱因斯坦自己的广义相对论反驳了他。这段争论没有赢家，但深刻加深了对量子理论的理解。", "titleEn": "The Bohr-Einstein Debate", "descEn": "Bohr and Einstein's decades-long debate on quantum mechanics became legendary. Einstein designed thought experiments to show quantum incompleteness; Bohr always found the flaw, once using Einstein's own general relativity." }
  ],
  "anecdote": "玻尔是一个说话声音很小、但思维极其深刻的人。他的学生形容他说话时经常含糊不清，句子拖着长长的尾音——但他说的每一句都是经过深思熟虑的。他最著名的特点是写文章和修改文章——他会反复修改同一段话数十遍，直到每个词都精确表达了意思。他的一个合作者说:'和玻尔讨论一个问题，你会觉得自己在和一座山交谈。'",
  "anecdoteEn": "Bohr spoke softly and thoughtfully, often revising a single paragraph dozens of times for precision. A colleague said: 'Discussing with Bohr felt like talking to a mountain.'",
  "aiReview": "玻尔-爱因斯坦争论是科学史上最精彩的思想交锋。爱因斯坦说'上帝不掷骰子'，玻尔回应'不要告诉上帝该怎么做'。两人互相敬重又寸步不让。玻尔的哥本哈根诠释最终成为了量子力学的主流解释，但爱因斯坦的质疑也推动了量子力学基础的发展——EPR佯谬最终导致了贝尔定理和量子信息学的诞生。这场争论最美妙之处在于：双方都无法完全说服对方，但争论本身推动了科学的进步。"
})

# ═══════════════════════════════════════════
# Feynman
# ═══════════════════════════════════════════
enrich('feynman', {
  "summary": "费曼是20世纪最富创造力的理论物理学家之一，在量子电动力学方面做出了革命性贡献。他发明的费曼图将粒子相互作用可视化，彻底改变了理论物理的计算方式。他也是无与伦比的科学教育家，以深入浅出的讲解和对科学的热情影响了无数人。",
  "summaryEn": "Feynman was one of the most creative theoretical physicists of the 20th century. His Feynman diagrams revolutionized quantum electrodynamics calculations. He was also an unparalleled science educator.",
  "lifeStory": "费曼1918年出生于纽约一个犹太家庭，父亲是军需品推销员。他从小就对科学、修理收音机和破解密码充满热情。1939年从麻省理工学院毕业，1942年在普林斯顿大学获博士学位。二战期间被招入曼哈顿计划，年仅24岁就担任了理论计算组负责人之一。战后在康奈尔大学和加州理工学院任教。1948年他创立了费曼图——一种用线条和顶点表示粒子相互作用的图示法，彻底简化了量子电动力学的计算。1965年因量子电动力学研究获诺贝尔奖。他1986年参与了挑战者号航天飞机爆炸事故的调查——在电视直播中用一杯冰水演示了O型密封圈在低温下失效的过程，成为科学传播的经典画面。",
  "lifeStoryEn": "Born in 1918 in New York, Feynman worked on the Manhattan Project at age 24. He invented Feynman diagrams in 1948, revolutionizing quantum calculations. He won the Nobel Prize in 1965 and famously demonstrated the Challenger disaster cause with a glass of ice water.",
  "keyContributions": [
    { "title": "费曼图", "titleEn": "Feynman Diagrams", "year": 1948, "desc": "一种用简单的图形表示粒子相互作用的工具——时间轴上的线条代表粒子的运动轨迹，顶点代表相互作用。费曼图将复杂的量子场论计算变成了一套直观的'涂鸦'，每个图形对应一个数学表达式。物理学家不再需要面对成千上万令人头晕的数学项，只需画出费曼图就可以直接写出计算结果。", "descEn": "A graphical tool representing particle interactions: lines for particle paths, vertices for interactions. Transformed complex quantum field calculations into intuitive diagrams with corresponding mathematical expressions.", "type": "theory" },
    { "title": "量子电动力学", "titleEn": "Quantum Electrodynamics", "year": 1948, "desc": "费曼与施温格、朝永振一郎各自独立建立了量子电动力学(QED)——描述光与物质相互作用的精确量子理论。QED的预言与实验的吻合程度达到了令人震惊的十亿分之一级别，是物理学中最精确的理论。", "descEn": "Independently developed QED with Schwinger and Tomonaga, describing light-matter interaction with unprecedented precision — predictions match experiment to one part in a billion.", "type": "theory" }
  ],
  "famousEvents": [
    { "title": "挑战者号调查的冰水实验", "year": 1986, "desc": "挑战者号航天飞机爆炸后，费曼被任命为调查委员会成员。他用一个极其简单的实验向全世界解释了爆炸原因：他将O型密封圈材料放入一杯冰水中，展示它在低温下失去弹性——航天飞机发射时当天气温极低，密封圈失效导致燃料泄漏。这个'桌上实验'比数百页技术报告更有说服力。", "titleEn": "Challenger Investigation", "descEn": "Feynman dramatically demonstrated the Challenger disaster cause on live TV: placing O-ring material in ice water showed it lost elasticity at low temperatures — a simple tabletop experiment more powerful than technical reports." }
  ],
  "anecdote": "费曼的传奇故事数不胜数：他在曼哈顿计划期间专门学习撬锁，打开了所有同事的保险柜并留下恶作剧纸条；他在酒吧里和普通人讨论物理比在学术会议上更开心；他曾研究蚂蚁的行走路径并写了一篇严肃的论文；他喜欢去脱衣舞俱乐部画速写——并声称从那里的鼓手身上学到了节奏感。他的自传《别逗了，费曼先生》本身就是一部科学版的'一千零一夜'。",
  "anecdoteEn": "Feynman learned to crack safes at Los Alamos for fun, loved explaining physics in bars, studied ant trail patterns seriously, and wrote an autobiography full of adventures titled 'Surely You're Joking, Mr. Feynman!'",
  "aiReview": "费曼的独特之处在于他对科学本质有极其清醒的认知。他反复强调'不懂不是一件可耻的事'——科学的美恰恰在于承认自己不知道。他曾说:'科学最大的价值在于它让人类学会了如何不被自己欺骗——学会了如何诚实地面对不确定性。'在物理学家们沉迷于弦论和其他无法验证的假设时，费曼的'我不能相信没人验证过的假设'的态度就像一剂清醒剂。他对教育的信念是：如果你不能用简单的语言向一个普通人解释一个物理概念，你就还没有真正理解它。"
})

# ═══════════════════════════════════════════
# Euler
# ═══════════════════════════════════════════
enrich('euler', {
  "summary": "欧拉是历史上最高产的数学家，其著作量超过任何同行。他在分析学、图论、数论、力学和光学等领域都做出了奠基性贡献。他引入了大量至今通用的数学符号（如π、e、f(x)等），被誉为'分析的化身'。",
  "summaryEn": "Euler is the most prolific mathematician in history. He made foundational contributions to analysis, graph theory, number theory, mechanics, and optics. He introduced many still-used symbols including π, e, and f(x).",
  "lifeStory": "欧拉1707年出生于瑞士巴塞尔的一个牧师家庭。13岁进入巴塞尔大学，师从约翰·伯努利。19岁时就因一篇关于船帆的论文获得巴黎科学院奖。1727年应叶卡捷琳娜一世的邀请前往圣彼得堡科学院。1741年应腓特烈大帝邀请移居柏林。1766年返回圣彼得堡，不久后完全失明——但惊人的是，他失明后的17年是他最多产的时期，依靠超强的记忆力和心算能力，在脑海中完成复杂的计算然后口述给助手记录。他一生发表了886篇论文和著作，去世后他的论文在圣彼得堡科学院持续发表了近50年。",
  "lifeStoryEn": "Born in 1707 in Basel, Euler entered university at 13. He worked in St. Petersburg and Berlin. Despite losing his eyesight completely, his most productive period was the 17 years after blindness, dictating complex mathematics to assistants.",
  "keyContributions": [
    { "title": "欧拉公式", "titleEn": "Euler's Formula", "year": 1748, "desc": "e^(iπ) + 1 = 0——这个公式将数学中五个最基本的常数（e、i、π、1、0）用一个等号联系在了一起，被誉为'数学中最美的公式'。它同时也是连接代数、几何、三角学和复分析的桥梁。费曼称它为'数学中最卓越的公式'和'我们的宝石'。", "descEn": "e^(iπ) + 1 = 0 — connects the five most fundamental constants in a single equation. Called 'the most beautiful formula in mathematics' and 'our jewel' by Feynman.", "type": "theory" },
    { "title": "图论奠基：柯尼斯堡七桥问题", "titleEn": "Graph Theory Foundation", "year": 1736, "desc": "欧拉解决了柯尼斯堡（今加里宁格勒）的七桥问题：是否可能一次走过所有七座桥而不重复？欧拉不仅给出了'不可能'的答案，更重要的是他将实际问题抽象成了点和线的数学结构——图论由此诞生。这篇论文通常被认为是图论和拓扑学的开端。", "descEn": "Solved the Königsberg bridge problem (proved it's impossible to cross all seven bridges once without repeating). More importantly, abstracted it into points and lines — founding graph theory and topology.", "type": "theory" },
    { "title": "数学符号体系", "titleEn": "Mathematical Notation", "year": 1750, "desc": "欧拉引进或推广了大量至今使用的数学符号：f(x)表示函数、e表示自然对数的底、Σ表示求和、π表示圆周率、i表示虚数单位、sin/cos/tg等三角函数简写。他的《无穷分析引论》和《微分学原理》是数学分析的经典教材。", "descEn": "Introduced or popularized symbols still used today: f(x), e, Σ, π, i, sin, cos. His textbooks on analysis and calculus remain classics.", "type": "work" }
  ],
  "famousEvents": [
    { "title": "失明后的高产岁月", "year": 1771, "desc": "欧拉在1766年返回圣彼得堡后不久即完全失明，但他以惊人的方式继续工作。他依靠超强的记忆力将整个数学体系存在脑中，口述给助手欧拉·克劳斯记录。失明期间他发表了超过400篇论文，占他总著作量的一半。他曾说:'我失明了，但看东西其实没什么用。思考才是理解数学的关键。'", "titleEn": "Productivity After Blindness", "descEn": "After losing his sight in 1766, Euler dictated over 400 papers to assistants — half his total output. He said: 'Being blind is no obstacle. Thinking, not seeing, is what matters in mathematics.'" }
  ],
  "anecdote": "欧拉计算能力的传奇之一：他曾经需要计算两个天文学家关于某颗彗星轨道进入时间的争论，两人各自给出了不同的计算结果。欧拉在脑海里进行了全部计算，然后给出了答案——他的结果和后来实际观测到的彗星位置只差了一点点，而两位天文学家的计算反而误差更大。另一个故事：他在失明后的一天口述了一篇论文，助手记录完后，欧拉说:'我忘记加入其中一个项了，它应该是…'然后修改了公式——实际上他在脑海中已经完成了全部推导。",
  "anecdoteEn": "Euler once computed a comet's orbit entirely in his head, matching observations better than two astronomers' competing calculations. After going blind, he could mentally complete complex proofs and correct errors from memory alone.",
  "aiReview": "欧拉是人类历史上最多产的数学家，但更令人惊讶的不是数量而是质量。他的每一篇论文几乎都有实质性贡献——发现新定理、发明新方法或解决棘手问题。他还有一种罕见的天赋：将复杂问题化简。无论是七桥问题还是欧拉公式，他都有能力看到问题的本质并将其用最优雅的方式表达出来。如果数学史上有'最高效的头脑'的评选，欧拉当之无愧。"
})

# ═══════════════════════════════════════════
# Riemann
# ═══════════════════════════════════════════
enrich('riemann', {
  "summary": "黎曼是19世纪最具原创力的数学家之一。他开创的黎曼几何为爱因斯坦的广义相对论提供了数学框架，黎曼猜想至今仍是数学界最重要的未解难题之一。他的工作以极少的论文数量但极高的思想密度著称。",
  "summaryEn": "Riemann was one of the most original mathematicians of the 19th century. His Riemannian geometry provided the mathematical framework for Einstein's general relativity, and the Riemann Hypothesis remains one of the most important unsolved problems.",
  "lifeStory": "黎曼1826年出生于德国汉诺威的一个牧师家庭。他生性羞怯，但数学天赋极高。在哥廷根大学求学期间，他旁听了高斯的课程，深受影响。1851年在高斯指导下完成了博士论文《复变函数论的基础》，高斯评价为'完全令人满意的作品'——他对任何人都是极为严苛的，这是极高的赞誉。1854年为了获得讲师职位，他做了任职演讲《关于几何基础的假设》——这篇演讲被认为是有史以来最重要的数学演讲之一，它彻底改变了人们对几何本质的理解。1866年因肺结核去世，年仅39岁，留下的论文数量不多但篇篇都是开创性的。",
  "lifeStoryEn": "Born in 1826 in Germany, Riemann was a shy genius. His PhD was praised by the famously strict Gauss. His 1854 lecture on geometry foundations revolutionized mathematics. He died of tuberculosis at 39, leaving few papers but each groundbreaking.",
  "keyContributions": [
    { "title": "黎曼几何", "titleEn": "Riemannian Geometry", "year": 1854, "desc": "黎曼在1854年的任职演讲中提出了一种全新的几何观：不再局限于欧几里得的平坦空间，而是研究一般的'弯曲空间'。他引入了度规张量的概念来测量弯曲空间中的距离和角度。60年后，爱因斯坦发现广义相对论中的四维弯曲时空正好可以用黎曼几何来描述。爱因斯坦说:'没有黎曼几何，就没有广义相对论。'", "descEn": "Proposed a radically new view of geometry: instead of flat Euclidean space, study curved spaces using the metric tensor. Sixty years later, it became the mathematical foundation of Einstein's general relativity.", "type": "theory" },
    { "title": "黎曼猜想", "titleEn": "Riemann Hypothesis", "year": 1859, "desc": "黎曼在关于素数分布的论文中提出了一个猜想：黎曼ζ函数的所有非平凡零点的实部都等于1/2。这个看似简单的断言，160多年来无人能证明也无人能否证。它是希尔伯特的23个问题之一，也是克雷数学研究所的千禧年七大难题之一（悬赏一百万美元）。大量数学定理都建立在'如果黎曼猜想成立'的前提之上。", "descEn": "A conjecture about the zeros of the Riemann zeta function: all non-trivial zeros have real part 1/2. Unsolved for 160+ years, it's one of the Millennium Problems with a $1M prize. Many theorems depend on its assumed truth.", "type": "theory" },
    { "title": "黎曼积分与复变函数", "titleEn": "Riemann Integral & Complex Analysis", "year": 1854, "desc": "黎曼给出了函数可积性的精确定义（黎曼积分），并在复变函数领域证明了柯西-黎曼方程、黎曼映射定理等系列结果。他对复变函数的几何化处理使得这个领域的发展大大加速。", "descEn": "Gave the precise definition of integrability (Riemann integral). In complex analysis, proved Cauchy-Riemann equations and the Riemann mapping theorem, greatly accelerating the field.", "type": "theory" }
  ],
  "famousEvents": [
    { "title": "任职演讲——改变数学的一小时", "year": 1854, "desc": "黎曼为了获得哥廷根大学的讲师资格，需要做一次任职演讲。他提交了三个题目，让人意外的是高斯选中了他认为最难的一个——关于几何基础。黎曼的演讲只有不到一小时，但在这段时间里他彻底重构了人们对空间的认知。在场的包括年迈的高斯——据说高斯在听完后激动不已，这是高斯第一次也是唯一一次公开对新数学表现出热情。", "titleEn": "The Lecture That Changed Mathematics", "descEn": "Riemann's hour-long 1854 lecture on geometry foundations completely reshaped humanity's understanding of space. Gauss, famously hard to impress, was visibly excited — the only known occasion he showed such enthusiasm." }
  ],
  "anecdote": "黎曼是一个极度腼腆的人——他有严重的舞台恐惧症。他的1854年任职演讲是在巨大的心理压力下完成的。但他对数学的信念战胜了恐惧——他知道自己要说的是全新的东西。他的博士答辩会上，向来严厉的高斯问他为什么要研究这么难的问题，黎曼紧张得几乎说不出完整的句子，但他的回答条理清晰、内容深刻。高斯后来对同事说:'这个年轻人有远大的前程。'",
  "anecdoteEn": "Riemann was extremely shy with stage fright. His historic 1854 lecture was delivered under intense anxiety, but his passion for mathematics overcame his fear. Gauss called him 'a young man with great prospects.'",
  "aiReview": "黎曼的工作方式具有一种特别的'密度'——他是数学史上'论文最少但影响最大'的数学家之一。他39年生命中发表的论文数量大概只有欧拉的百分之一，但每一篇都开启了一个新的方向。黎曼几何改变了空间的观念，黎曼猜想刺激了数论和复分析的发展，黎曼映射定理是复变函数的基石。这就像一个人只射出了几支箭，但每一支都正中靶心。他的早逝是数学史上最大的'如果'——如果黎曼活到了正常寿命，他还会带来多少革命性的思想？"
})

# ═══════════════════════════════════════════
# Pasteur
# ═══════════════════════════════════════════
enrich('pasteur', {
  "summary": "巴斯德奠定了微生物学的基础，提出了疾病的细菌学说。他发明的巴氏消毒法至今广泛使用，研制的狂犬病疫苗和炭疽疫苗开创了现代免疫学。他彻底改变了医学和公共卫生的面貌。",
  "summaryEn": "Pasteur founded microbiology and proposed the germ theory of disease. He invented pasteurization and developed rabies and anthrax vaccines, revolutionizing medicine and public health.",
  "lifeStory": "巴斯德1822年出生于法国多勒的一个制革匠家庭。他在中学时并非特别出众，但在巴黎高等师范学院学习时展现出在化学方面的才华。最初从事化学研究（发现了分子的旋光异构现象），1860年代转向发酵和微生物研究。他通过精巧的实验证明：发酵是由活的微生物引起的；空气中有微生物存在，但并非自然发生的——这些实验彻底推翻了'自然发生说'。1885年他成功在一位被疯狗严重咬伤的孩子身上应用了狂犬病疫苗——这个孩子存活了，巴斯德成为国际英雄。他在巴黎建立了巴斯德研究所（1887年），至今仍是世界顶级的生物医学研究机构。",
  "lifeStoryEn": "Born in 1822 in Dole, France, Pasteur started as a chemist but turned to microbiology in the 1860s. He disproved spontaneous generation, developed pasteurization and vaccines. His 1885 rabies vaccine success made him an international hero.",
  "keyContributions": [
    { "title": "细菌学说", "titleEn": "Germ Theory of Disease", "year": 1860, "desc": "巴斯德通过一系列经典实验证明了疾病由微生物引起。他最著名的实验是使用曲颈瓶——将一个装有肉汤的长颈瓶拉成S形弯曲的长管，空气可以进入但灰尘和微生物被截留在弯曲处。结果肉汤没有腐败——证明腐败来自空气中的微生物而非'自然发生'。这一发现将医学从'瘴气理论'等错误观念中解放出来。", "descEn": "Proved diseases are caused by microorganisms through elegant experiments. His swan-neck flask experiment demonstrated that spoilage comes from airborne microbes, not spontaneous generation.", "type": "theory" },
    { "title": "巴氏消毒法", "titleEn": "Pasteurization", "year": 1862, "desc": "发明了用加热杀死有害微生物但不破坏食物品质的方法。原本是为了解决葡萄酒变酸的问题——将葡萄酒加热到60°C左右保持一段时间，即可杀灭导致变酸的微生物。这一方法后来被广泛应用到牛奶、啤酒等食品的保存中，极大地减少了食源性疾病。", "descEn": "Invented heating liquids to 60°C to kill harmful microbes without ruining flavor. Originally developed for wine, later applied to milk and beer, dramatically reducing foodborne illness.", "type": "invention" },
    { "title": "狂犬病疫苗", "titleEn": "Rabies Vaccine", "year": 1885, "desc": "巴斯德在没有任何病毒学知识（当时还不知道病毒的存在）的情况下，成功研制出狂犬病疫苗。他将狂犬病病毒在兔脑中连续传代使其减弱毒性，制成疫苗。1885年成功救治了被疯狗严重咬伤的9岁男孩约瑟夫·迈斯特。这个案例标志着现代免疫学的诞生。", "descEn": "Developed the rabies vaccine without even knowing viruses existed. Successfully treated a 9-year-old boy severely bitten by a rabid dog in 1885, marking the birth of modern immunology.", "type": "invention" }
  ],
  "famousEvents": [
    { "title": "狂犬病疫苗首个人体试验", "year": 1885, "desc": "1885年7月6日，一个被疯狗严重咬伤的9岁男孩约瑟夫·迈斯特被送到巴斯德面前。巴斯德不是医生（没有行医执照），而且他的疫苗只在动物身上测试过。在巨大压力下，他决定冒险注射——因为不注射男孩必死无疑。经过12次注射后，男孩奇迹般康复。巴斯德一夜之间成为全球英雄，世界各地的人们纷纷捐款支持他的研究。", "titleEn": "First Human Rabies Vaccine", "descEn": "A 9-year-old boy bitten by a rabid dog was brought to Pasteur. With no medical license and only animal-tested vaccine, Pasteur took the risk — 12 injections later, the boy survived. Pasteur became a global hero." }
  ],
  "anecdote": "巴斯德那句名言'机遇只偏爱有准备的头脑'来自他职业生涯中最重要的一次'偶然发现'——在研究发酵时，他发现放置了一段时间的甜菜汁变成了酸液，显微镜下看到的是乳酸杆菌而非酵母菌。这个观察让他意识到不同微生物引起不同发酵过程——从而确立了他的微生物学基础。他的合作者说:'其他人看到这样的变化可能会忽略它，但巴斯德不会。'",
  "anecdoteEn": "Pasteur's famous 'chance favors the prepared mind' came from noticing that soured beet juice contained different microbes than fermenting juice — leading to his foundational insight that specific microbes cause specific processes.",
  "aiReview": "巴斯德将人类平均寿命延长了数十年的贡献怎么评价都不为过。在巴斯德之前，人们不知道疾病是怎么传播的——外科手术后的感染被认为是必然的，分娩后的败血症夺走了无数产妇的生命，狂犬病等于必死无疑。巴斯德的细菌学说就像一道光，照亮了黑暗的中世纪医学。他的对手和怀疑者很多，因为他的理论要求医生们洗手、消毒器械——这被当时许多资深医生视为侮辱。他的一生证明了：科学的进步不仅是知识的进步，更是对人类习惯和偏见的改造。"
})

# ═══════════════════════════════════════════
# Hubble
# ═══════════════════════════════════════════
enrich('hubble', {
  "summary": "哈勃证明了银河系之外存在其他星系，并发现了星系退行速度与距离成正比的哈勃定律——这是宇宙膨胀的第一个观测证据。他的工作彻底改变了人类对宇宙大小和演化的认知，为大爆炸理论奠定了观测基础。",
  "summaryEn": "Hubble proved there are galaxies beyond the Milky Way and discovered Hubble's Law — the proportionality between galaxy recession speed and distance. This provided the first observational evidence for the expanding universe.",
  "lifeStory": "哈勃1889年出生于美国密苏里州的一个律师家庭。他在芝加哥大学学习天文学和数学，之后赴牛津大学学习法律——但最终放弃了律师职业回归天文。1917年获得博士学位，1919年加入威尔逊山天文台（在那里可以用当时世界最大的胡克2.5米望远镜）。1923-1924年他在仙女座星云中发现了造父变星，测出其距离远超银河系范围——证明了它是另一个独立的星系。1929年他发表了里程碑式的论文，指出星系退行速度与其距离成正比（哈勃常数）。这个发现让爱因斯坦放弃了他曾引入的宇宙常数——爱因斯坦在访问威尔逊山天文台时亲自向哈勃表示了祝贺。",
  "lifeStoryEn": "Born in 1889 in Missouri, Hubble initially studied law but returned to astronomy. Using the world's largest telescope at Mt. Wilson, he proved Andromeda is a separate galaxy in 1924 and announced Hubble's Law in 1929, showing the universe is expanding.",
  "keyContributions": [
    { "title": "哈勃定律", "titleEn": "Hubble's Law", "year": 1929, "desc": "哈勃通过观测24个临近星系的退行速度（由光谱红移测定）和距离，发现两者之间存在精确的线性关系——星系越远，退行越快，这个比例常数被称为哈勃常数。这个发现意味着宇宙正在膨胀——就像气球上画的斑点，气球充气时所有斑点都彼此远离。这是大爆炸理论最直接的观测证据。", "descEn": "Discovered a linear relationship between galaxy recession velocity and distance — the farther a galaxy, the faster it recedes. This proved the universe is expanding, providing direct evidence for the Big Bang.", "type": "discovery" },
    { "title": "河外星系发现", "titleEn": "Extragalactic Galaxies", "year": 1924, "desc": "哈勃在仙女座星云中找到了造父变星——一种可以通过其亮度变化周期精确测定距离的标准烛光。他计算出仙女座距离我们约90万光年（现代修正后为250万光年），远超我们银河系的直径。这一发现彻底改变了人类的宇宙图景——原来银河系只是宇宙中无数星系中的一个普通成员。", "descEn": "Using Cepheid variable stars in Andromeda, Hubble calculated its distance far beyond the Milky Way's boundaries. This proved the Milky Way is just one of countless galaxies, fundamentally changing humanity's cosmic perspective.", "type": "discovery" }
  ],
  "famousEvents": [
    { "title": "爱因斯坦的认错", "year": 1931, "desc": "1917年爱因斯坦发现广义相对论方程要求宇宙要么膨胀要么收缩，但他固守宇宙是静止的传统观念，于是引入了'宇宙常数'来维持静态宇宙。哈勃的发现证明宇宙在膨胀后，爱因斯坦在访问威尔逊山天文台时面对哈勃的数据，坦率地承认：'这是我所犯过的最大的错误。'他放弃了宇宙常数，并衷心感谢哈勃。", "titleEn": "Einstein's 'Biggest Blunder'", "descEn": "Einstein had added a 'cosmological constant' to his equations to keep the universe static. After Hubble proved the universe is expanding, Einstein visited Mt. Wilson, saw the evidence, and called it his 'biggest mistake.'" }
  ],
  "anecdote": "哈勃曾获得牛津大学的法律学位，并在肯塔基州短暂从事律师工作。他说自己作为律师的唯一成就是赢得了一个关于'鸡能不能在铁轨上行走'的案件——他的理由是'鸡是家禽，不是交通工具，不受交通法规限制'。他后来放弃了法律，因为他发现'晚上看星星比白天为鸡辩护有趣得多'。在威尔逊山天文台工作时，他经常穿着花呢西装和领带进行观测——他认为科学家应该穿得像个绅士。",
  "anecdoteEn": "Hubble practiced law briefly and once defended a case about whether chickens could walk on train tracks (his argument: 'chickens aren't vehicles'). He quit law, saying 'looking at stars at night is more fun than defending chickens by day.'",
  "aiReview": "哈勃完成了一件人类自哥白尼以来最宏大的认知扩张——他告诉我们宇宙比我们想象的更大，而且在不断变大。哥白尼把地球移出了宇宙中心，哈勃把银河系降级成了无数星系中的一个。这种'人类不是中心'的认知每来一次，科学就向前迈进一步。哈勃定律还有一个令人惊叹的推论：既然宇宙在膨胀，那么回溯到过去一定有一个起点——这就是大爆炸。从哈勃的望远镜到宇宙的起源，人类只用了短短几十年就完成了这场认知的革命。"
})

# ═══════════════════════════════════════════
# Shannon
# ═══════════════════════════════════════════
enrich('shannon', {
  "summary": "香农是信息论之父，其《通信的数学理论》为数字通信和信息时代奠定了理论基础。他还将布尔代数应用于开关电路，开创了数字电路设计的先河。他的工作深刻影响了从电话通信到互联网的一切信息技术。",
  "summaryEn": "Shannon is the father of information theory. His 'Mathematical Theory of Communication' laid the foundation for the digital age. He also applied Boolean algebra to switching circuits, pioneering digital circuit design.",
  "lifeStory": "香农1916年出生于密歇根州的一个小镇，父亲是商人兼法官，母亲是教师。他从小喜欢动手制作各种机械装置——他用废旧零件做了一台电动船模型和一套家庭通信系统。1936年在密歇根大学获得电气工程和数学双学位。1937年在麻省理工学院读硕士期间，他完成了那篇划时代的硕士论文《继电器和开关电路的符号分析》——将布尔代数与电路设计联系起来，这篇论文被称为'20世纪最重要的硕士论文'。1940年在普林斯顿高等研究院工作，1941年加入贝尔实验室。1948年发表了《通信的数学理论》，奠定了信息论的基础。他后来转向人工智能研究，制造了能下国际象棋的机器人和著名的'忒修斯迷宫老鼠'。",
  "lifeStoryEn": "Born in 1916 in Michigan, Shannon earned dual degrees in EE and math. His 1937 master's thesis connecting Boolean algebra to circuits was called 'the most important master's thesis of the 20th century.' At Bell Labs, he founded information theory in 1948.",
  "keyContributions": [
    { "title": "信息论", "titleEn": "Information Theory", "year": 1948, "desc": "香农定义了一个革命性的概念：信息是一种可以用比特（bit）来精确度量的东西。他提出了信息熵——衡量信息量的数学度量。他还证明了信道容量定理（香农极限）：在任何有噪声的信道上，存在一个最大可靠传输速率，但可以无限接近这个速率而不出错。这一理论奠定了所有数字通信的基础——从WiFi到光纤、从CD到5G。", "descEn": "Defined information as measurable in bits. Introduced information entropy and proved the channel capacity theorem: maximum reliable transmission rate over any noisy channel. Foundation of all digital communication.", "type": "theory" },
    { "title": "数字电路设计理论", "titleEn": "Digital Circuit Design", "year": 1937, "desc": "香农的硕士论文证明了：布尔代数的逻辑运算（与、或、非）可以用继电器开关电路来实现，并且任何复杂的逻辑函数都可以通过电路来运算。这一洞见将抽象的数学逻辑变成了可操作的硬件设计——所有现代计算机芯片里的门电路，追根溯源都来自香农的这篇论文。", "descEn": "Proved Boolean algebra operations can be implemented with switching circuits, and any logical function can be computed by circuits. This insight turned abstract logic into hardware design — the foundation of all digital chips.", "type": "theory" }
  ],
  "famousEvents": [
    { "title": "硕士论文改变了世界", "year": 1937, "desc": "香农的硕士论文《继电器和开关电路的符号分析》被评价为'20世纪最有价值的硕士论文'——它奠定了数字电路和计算机硬件设计的理论基础。当时22岁的香农可能没有意识到，他在这篇论文中开启了一个时代。20年后这篇论文里的原理被集成到芯片上——计算机时代全面到来。", "titleEn": "The Master's Thesis That Changed the World", "descEn": "Shannon's 1937 master's thesis on switching circuits, written at age 22, laid the theoretical foundation for digital circuit design and all modern computer hardware." }
  ],
  "anecdote": "香农在贝尔实验室的办公室是一个玩具王国——他制造了各种稀奇古怪的机器：自动解魔方的机器、能喷火的小号、能下国际象棋的计算机、走迷宫的老鼠（叫'忒修斯'）。他还发明了一种叫'终极机器'的装置——一个装有开关的盒子，打开开关后盒盖打开伸出一只机械手，把开关关掉，然后缩回去。他试图用杂耍来论证存在主义哲学。他的同事说香农是'一个活在快乐中的天才'——他做研究纯粹是因为好玩。",
  "anecdoteEn": "Shannon's Bell Labs office was a toy workshop. He built a juggling machine, a flame-throwing trumpet, a maze-solving mouse named 'Theseus', and the 'Ultimate Machine' — a box with a switch that turns itself off. He did science purely for fun.",
  "aiReview": "香农的天才在于他能从看似平凡的问题中提炼出深刻的理论。什么是信息？在香农之前，没有人能精确定义它。香农说：信息的本质不是'意义'而是'不确定性'——一个信息的信息量取决于它消除了多少不确定性。这个回答让通信工程师们恍然大悟：原来你不需要理解信息的内容，只需要量化信息就能实现可靠的通信。今天，当你在微信上发送一条消息时，你的语音或文字被转化为二进制比特，通过香农极限定理设计的纠错码穿越嘈杂的信道，最终在朋友的手机上精确还原——这背后全是香农的遗产。"
})

# ═══════════════════════════════════════════
# Fleming
# ═══════════════════════════════════════════
enrich('fleming', {
  "summary": "弗莱明发现了青霉素——世界上第一种抗生素，开创了抗生素时代，挽救了数以亿计的生命。他的发现是20世纪医学史上最重要的突破之一，彻底改变了人类对抗细菌感染的能力。",
  "summaryEn": "Fleming discovered penicillin, the world's first antibiotic, ushering in the antibiotic era and saving hundreds of millions of lives. It was one of the most important breakthroughs in 20th-century medicine.",
  "lifeStory": "弗莱明1881年出生于苏格兰的一个农场家庭。他在伦敦圣玛丽医院医学院学习医学。第一次世界大战期间他在战场医院工作，亲眼目睹了无数士兵死于伤口感染却无药可治——这促使他终身致力于寻找抗菌物质。1922年他发现了一种溶菌酶（人体分泌的一种天然抗菌物质），但效果有限。1928年他做了一个影响深远的观察：在培养葡萄球菌的培养皿中无意中长出了一丛青霉菌，而青霉菌周围的细菌被溶解了。他猜测青霉菌分泌了某种杀菌物质，将其命名为'青霉素'。但他后来遇到了纯化和生产青霉素的困难。直到1939年，弗洛里和钱恩团队成功实现了青霉素的纯化和量产——二战期间青霉素挽救了无数盟军伤员的生命。1945年弗莱明与弗洛里、钱恩共同获得诺贝尔奖。",
  "lifeStoryEn": "Born in 1881 in Scotland, Fleming served in WWI and saw soldiers die from infections. In 1928 he noticed a mold contaminating his bacterial cultures had killed surrounding bacteria — he named it penicillin. Florey and Chain later mass-produced it, saving millions in WWII.",
  "keyContributions": [
    { "title": "青霉素的发现", "titleEn": "Discovery of Penicillin", "year": 1928, "desc": "弗莱明在准备休假前将一堆细菌培养皿放在试验台上。休假回来后，他发现一个培养皿被青霉菌污染了，但在青霉菌周围一圈的葡萄球菌被溶解了——形成了一个透明的环。他没有放过这个偶然现象，正确地推断出青霉菌分泌了某种具有强大杀菌能力的物质。他随后证明青霉素对多种致病细菌有杀灭作用。", "descEn": "Fleming noticed a mold-contaminated Petri dish had a clear ring around it where bacteria were dissolved. He correctly inferred the mold secreted a bactericidal substance — penicillin. This single observation launched the antibiotic era.", "type": "discovery" }
  ],
  "famousEvents": [
    { "title": "弗洛里和钱恩完成量产", "year": 1941, "desc": "弗莱明发现的青霉素单靠自己无法实现纯化和大规模生产。直到1939年牛津大学的弗洛里和钱恩团队才成功纯化青霉素并在动物实验中证实了其疗效。1941年他们首次在人体使用——一位警察因刮胡子时划伤导致全身感染，在用尽所有磺胺药无效后，使用青霉素出现了戏剧性的好转。1943年D日登陆中，青霉素大量生产，挽救了无数盟军伤员的肢体和生命。", "titleEn": "Mass Production of Penicillin", "descEn": "Florey and Chain at Oxford purified penicillin and demonstrated its efficacy. By 1943, mass production saved countless Allied soldiers' lives during the D-Day invasion — the first antibiotic that truly changed the world." }
  ],
  "anecdote": "发现青霉素时，弗莱明的实验室以杂乱著称。如果他是那种喜欢每天收拾整齐的科学家，那个被青霉菌污染的培养皿早就被清洗消毒了，青霉素的发现可能会被推迟很多年。他自己后来也幽默地说:'我之所以发现了青霉素，不是因为我有多聪明，而是因为我的实验室够乱。'还有一个细节：他最初把青霉素称为'霉菌汁'（mould juice），这个名字听起来像厨房里的东西而不是能拯救亿万生命的药物。",
  "anecdoteEn": "Fleming famously kept a messy lab — if he'd cleaned his dishes regularly, the contaminated Petri dish would have been washed away. He joked: 'I didn't discover penicillin because I was smart, but because my lab was messy enough.'",
  "aiReview": "青霉素的发现是科学中偶然性与准备性相结合的经典案例。弗莱明说过'机遇只偏爱有准备的头脑'——那个培养皿被青霉菌污染是偶然，但如果他不认识葡萄球菌的正常生长形态、不思考为什么出现了透明区域、不进一步验证，这个偶然就白白浪费了。青霉素的故事还展示了基础研究和应用研究的完美接力：弗莱明发现了青霉素但不具备纯化能力，弗洛里和钱恩在二战压力下将它做成可用的药物。没有基础研究就没有青霉素的发现，没有工程开发就没有青霉素的大规模应用。这两者缺一不可。"
})

# ═══════════════════════════════════════════
# Hua Luogeng
# ═══════════════════════════════════════════
enrich('hua-luogeng', {
  "summary": "华罗庚是中国现代数学的奠基人和开拓者。他在数论、代数和多复变函数论方面做出了世界级的贡献。他不仅是一位杰出的理论数学家，还致力于将数学方法应用于国民经济建设，培养了一代中国数学家。",
  "summaryEn": "Hua Luogeng was the founder of modern Chinese mathematics. He made world-class contributions to number theory, algebra, and several complex variables. He also applied mathematics to China's economic development and trained generations of mathematicians.",
  "lifeStory": "华罗庚1910年出生于江苏金坛的一个小商人家庭。他只读完了初中，因家境贫寒无法继续上学。但他通过自学数学着了迷——白天帮父亲打理店铺，晚上在煤油灯下研读数学。他在《科学》杂志上发表了一篇论文，引起了清华大学熊庆来教授的注意。熊庆来邀请他到清华工作，从助理员做起，边工作边学习——用了不到一年半时间就升任助教。1936年赴英国剑桥大学访问学习，在数论领域做出了一系列重要成果。抗战期间回国，在西南联大任教。1946年受邀访问普林斯顿高等研究院。1950年毅然放弃美国的优厚待遇回到新中国。他后来不仅研究理论数学，还大力推广统筹法和优选法在中国工业中的应用，亲自深入工厂和农村传授数学方法。",
  "lifeStoryEn": "Born in 1910 in Jintan, China, Hua only finished middle school due to poverty. He taught himself mathematics, and his paper caught Tsinghua professor Xiong Qinglai's attention. He later studied at Cambridge, returned to China during WWII, and after a US stint, came back in 1950 to build Chinese mathematics.",
  "keyContributions": [
    { "title": "华罗庚定理（完整三角和估计）", "titleEn": "Hua's Theorem", "year": 1940, "desc": "华罗庚在数论方面做出了多个重要贡献，其中最重要的是对完整三角和（华罗庚-韦伊估计）和华林问题的研究。他在没有获得任何正式大学学位的情况下，在剑桥大学期间就在世界顶级数学期刊上发表了一系列高水平论文，让国际数学界对这位'初中生数学家'刮目相看。", "descEn": "Made important contributions to number theory including exponential sum estimates (Hua's estimates) and Waring's problem. Without any university degree, he published groundbreaking papers from Cambridge that stunned the international math community.", "type": "theory" },
    { "title": "统筹法和优选法推广", "titleEn": "Optimization Methods", "year": 1960, "desc": "华罗庚将数学中的统筹法和优选法改造成简单易懂的实用工具，亲自带领学生走遍中国20多个省市的工厂和农村推广。这些方法帮助工人提高生产效率、节约原材料，产生了显著的经济效益。他被誉为'把数学还给人民'的数学家。", "descEn": "Translated optimization methods into practical tools for factory workers and farmers, personally traveling to over 20 Chinese provinces to teach them. Known as 'the mathematician who returned mathematics to the people.'", "type": "invention" }
  ],
  "famousEvents": [
    { "title": "初中生的逆袭", "year": 1931, "desc": "华罗庚在《科学》杂志上发表论文后，清华大学的熊庆来教授问同事: '这个华罗庚是哪个国家留学的？'当得知他只是一个初中毕业的学徒时，熊庆来震惊了，立即邀请他到清华大学工作。在清华，华罗庚仅用一年半就自学完了数学系本科全部课程，并开始用英文在海外发表论文。", "titleEn": "From Dropout to Mathematician", "descEn": "After publishing a paper while working in a shop, Hua was invited to Tsinghua University by Professor Xiong. Despite only having a middle school education, he mastered the entire math curriculum in 18 months and began publishing internationally." }
  ],
  "anecdote": "华罗庚在清华工作期间，为了弥补学历不足，每天只睡四五个小时。他住在工友宿舍，月薪只有15元，但买书从不吝啬。他自学英语时，把英文数学论文逐字逐句翻译，然后用中文写笔记，再用英文复述。他还说自己的学习方法就是'把一本厚书读薄，再把一本薄书读厚'。这个从学徒到国际数学家的传奇，鼓舞了无数中国青年投身科学。",
  "anecdoteEn": "At Tsinghua, Hua slept only 4-5 hours daily, living in a worker's dorm on a 15-yuan salary. He memorized math papers by translating them word for word. His journey from shop apprentice to world-class mathematician inspired generations of Chinese youth.",
  "aiReview": "华罗庚的传奇在于他没有学历、没有背景、没有导师，仅靠自学走完了从初中生到国际数学家的路途。这在中国乃至世界数学史上都是罕见的。更难能可贵的是他在功成名就之后，没有停留在象牙塔里做纯理论研究，而是主动将数学方法推广到工厂和田间——这种'把论文写在大地上'的精神，使得他不仅是一位数学家，更是一位科学传播的符号。"
})

# ═══════════════════════════════════════════
# Pythagoras
# ═══════════════════════════════════════════
enrich('pythagoras', {
  "summary": "毕达哥拉斯是古希腊数学家、哲学家，创立了以'万物皆数'为信条的毕达哥拉斯学派。他发现勾股定理（毕达哥拉斯定理），在数论和音乐理论方面也有奠基性贡献，对柏拉图和西方数学哲学传统影响深远。",
  "summaryEn": "Pythagoras was an ancient Greek mathematician and philosopher who founded a school believing 'all is number.' He discovered the Pythagorean theorem and made foundational contributions to number theory and music theory.",
  "lifeStory": "毕达哥拉斯约公元前570年出生于萨摩斯岛。他年轻时游历埃及和巴比伦，学习了数学、天文学和宗教知识。约公元前530年他移居南意大利的克罗顿，在那里创立了一个集学术、宗教和政治于一体的秘密社团——毕达哥拉斯学派。这个学派的成员过着严格的生活，包括素食、禁欲和沉默期。他们相信数学是理解宇宙的关键——'万物皆数'。学派的发现很多（如勾股定理、无理数的发现），但所有成果都归功于毕达哥拉斯本人——这是学派的规矩。学派内部的政治活动最终招致了当地民众的敌视，毕达哥拉斯在晚年被迫逃亡，约公元前495年去世。",
  "lifeStoryEn": "Born around 570 BC on Samos, Pythagoras traveled to Egypt and Babylon before founding a secret religious-scientific society in Croton, southern Italy. The school believed 'all is number' and made numerous mathematical discoveries.",
  "keyContributions": [
    { "title": "勾股定理", "titleEn": "Pythagorean Theorem", "year": -530, "desc": "直角三角形的两条直角边的平方和等于斜边的平方。这个定理虽然在此前已被巴比伦人和中国人知道一些特例，但毕达哥拉斯学派是第一个给出了一般性的证明。它是几何学中最重要的基本定理之一，在数学史上地位极其崇高。", "descEn": "In a right triangle, the square of the hypotenuse equals the sum of squares of the other two sides. While specific cases were known earlier, the Pythagoreans first gave a general proof.", "type": "theory" },
    { "title": "数与音乐的和谐", "titleEn": "Harmony of Numbers and Music", "year": -530, "desc": "毕达哥拉斯发现：琴弦的长度成简单整数比时发出和谐的音——如2:1是八度、3:2是五度、4:3是四度。这个发现让他相信宇宙的本质是数学的——天体之间的距离也遵循类似的和谐比例，形成了'天体的音乐'。这是人类第一次意识到自然界可以用数学来描述。", "descEn": "Discovered that musical harmony arises from simple integer ratios of string lengths. This led to the belief that the universe is fundamentally mathematical — the first realization that nature can be described mathematically.", "type": "theory" }
  ],
  "famousEvents": [
    { "title": "无理数的发现——学派的危机", "year": -500, "desc": "毕达哥拉斯学派的信条是'万物皆数'——这里的'数'指整数和整数之比（有理数）。但学派的成员希帕索斯发现：边长为1的正方形的对角线长度√2无法表示为整数之比。这个发现动摇了学派的根基——如果连一个正方形的对角线长度都不能用整数之比表示，'万物皆数'还成立吗？传说希帕索斯将这个发现公之于众后被学派处以极刑——被扔进海里淹死。", "titleEn": "The Crisis of Irrational Numbers", "descEn": "Hippasus of Metapontum discovered that √2 cannot be expressed as a ratio of integers, shattering the school's 'all is number' doctrine. Legend says he was executed by drowning for revealing this secret." }
  ],
  "anecdote": "毕达哥拉斯学派有很多古怪的规定：不准吃豆子、不准捡起掉落的食物、不准在灯边照镜子、起床后要揉平床单上的痕迹。这些规矩今天看来不可思议，反映了这个学派既是学术团体又是宗教秘密社团的混合性质。他们的哲学训练包括严格的沉默期——新入学的成员前五年只能听课、不能提问。",
  "anecdoteEn": "The Pythagorean school had strange rules: don't eat beans, don't pick up fallen food, smooth bed sheets after rising. New members observed five years of silence — listening but never questioning.",
  "aiReview": "毕达哥拉斯的思想遗产不是具体的数学定理，而是一种根本的信念：宇宙可以用数学来理解。这个信念今天看来理所当然，但在公元前六世纪，这是一个革命性的飞跃——它意味着世界不是由任性的神明随意支配的，而是遵循着可理解的数学规律。从哥白尼到开普勒、从伽利略到牛顿，再到现代物理学家——所有人类对宇宙的精确理解，根源都在毕达哥拉斯那里。"
})

# ═══════════════════════════════════════════
# Faraday
# ═══════════════════════════════════════════
enrich('faraday', {
  "summary": "法拉第是19世纪最伟大的实验物理学家之一。他发现了电磁感应现象，提出了场的概念，发明了发电机和电动机的原型。他的实验发现为麦克斯韦的电磁理论奠定了实验基础，而他的'场'的概念彻底改变了物理学对空间的理解。",
  "summaryEn": "Faraday was one of the greatest experimental physicists of the 19th century. He discovered electromagnetic induction, proposed the concept of fields, and invented prototypes of the electric generator and motor.",
  "lifeStory": "法拉第1791年出生于伦敦一个贫穷的铁匠家庭。他只上了两年小学，13岁就当了装订书的学徒。但他利用装订书籍的机会大量阅读——一本《大英百科全书》中的'电'条目激发了他对科学的终身兴趣。他听了著名化学家戴维的讲座，认真记录并装订成精美的笔记送给戴维。1813年戴维雇用他为助手——虽然名义上是秘书兼洗瓶工。法拉第在皇家研究所成长为世界级的实验科学家。1831年他发现了电磁感应——这是发电机的原理，从此人类有了大规模产生电能的方法。他还发现了电解定律、磁光效应和抗磁性。他的'力线'和'场'的概念虽然缺乏数学化的表达，但为整个电磁理论提供了物理直觉的基础。",
  "lifeStoryEn": "Born in 1791 to a poor blacksmith family, Faraday had only two years of schooling. Apprenticed as a bookbinder, he educated himself through reading. He became assistant to chemist Davy and later made landmark discoveries in electromagnetism at the Royal Institution.",
  "keyContributions": [
    { "title": "电磁感应", "titleEn": "Electromagnetic Induction", "year": 1831, "desc": "法拉第发现：一个变化的磁场可以在附近的导体中产生电流。他用一个简单的实验证明了这一点：当磁铁在线圈中插入或拔出时，线圈中产生了电流。这一发现直接导致了发电机的发明——从此人类有了将机械能转化为电能的可靠方法。没有电磁感应，就没有现代电力工业。", "descEn": "Discovered that a changing magnetic field induces an electric current in a nearby conductor. This directly led to the electric generator — the basis of the entire electrical power industry.", "type": "discovery" },
    { "title": "场的概念", "titleEn": "Field Concept", "year": 1840, "desc": "法拉第提出了一个革命性的想法：磁体和电荷周围的空间中存在着某种物理实在——他称之为'力线'和'场'。力线是真实存在的，虽然看不见摸不着。今天我们知道电场和磁场确实是空间中的物理场——法拉第的直觉被麦克斯韦数学化后，成为了现代物理的核心概念。", "descEn": "Revolutionary concept: space around magnets and charges contains 'lines of force' — real physical entities called fields. This intuition, later mathematized by Maxwell, became central to modern physics.", "type": "theory" }
  ],
  "famousEvents": [
    { "title": "戴维的嫉妒", "year": 1823, "desc": "法拉第的才华很快超越了导师戴维。当法拉第被提名加入皇家学会时，戴维——作为当时皇家学会会长——投了唯一的反对票。戴维的嫉妒心是科学史上的一段遗憾轶事。但法拉第从未在公开场合抱怨过，他始终尊称戴维为'我的恩师'。法拉第婉拒了爵士头衔和其他一切荣誉，终其一生保持朴素。", "titleEn": "Davy's Jealousy", "descEn": "When Faraday was nominated to the Royal Society, his mentor Davy cast the only opposing vote. Faraday never complained publicly and always respectfully called Davy 'my master.' He refused all titles and honors." }
  ],
  "anecdote": "法拉第的讲座是他那个时代的奇观——他在皇家研究所的周五晚上讲座和圣诞讲座吸引了伦敦各界名流。他的演示极其精彩——用各种精巧的装置展示电和磁的奇妙现象，大厅里常常爆发出惊叹和掌声。这个传统一直延续到今天——英国皇家研究所的圣诞讲座至今仍在BBC播出。法拉第的讲座名言是:'实验是科学的灵魂。'",
  "anecdoteEn": "Faraday's lectures at the Royal Institution were spectacular demonstrations of electricity and magnetism that drew London's elite. This tradition continues today with the Royal Institution Christmas Lectures broadcast on BBC.",
  "aiReview": "法拉第是一个没有受过正规数学训练的'纯实验家'，但他的理论直觉却超越了同时代的所有数学家。在人们还在满足于用'超距作用'解释电力和磁力时，法拉第已经相信空间中充满了看不见的力线——这是一种比所有人领先几十年的物理直觉。麦克斯韦比他年轻四十岁，拥有当时最顶尖的数学能力，但他坦承自己只是把法拉第的直觉翻译成了数学语言。这说明在物理学中，物理直觉和数学技巧同等重要——而法拉第是纯物理直觉的巅峰。"
})

# ═══════════════════════════════════════════
# Planck
# ═══════════════════════════════════════════
enrich('planck', {
  "summary": "普朗克提出了能量量子化假说——能量不是连续的，而是以不可分割的'量子'形式发射和吸收。这一假说开创了量子物理学，被誉为量子理论之父。他提出的普朗克常数成为自然界最基本的常数之一。",
  "summaryEn": "Planck proposed that energy is emitted and absorbed in discrete 'quanta,' not continuously — the hypothesis that founded quantum physics. Planck's constant became one of the most fundamental constants in nature.",
  "lifeStory": "普朗克1858年出生于德国基尔的一个学术世家——他的曾祖父和祖父都是神学教授，父亲是法学教授。普朗克本人天资极高，但非常谨慎。他最初在慕尼黑大学学习物理时，导师曾劝他不要学物理——'这个领域已经没什么好发现的了'。普朗克礼貌地拒绝了建议，表示只想理解已知的物理。1900年他为了解释黑体辐射的实验数据，提出了一个大胆的假说：能量以量子形式不连续地发射和吸收。这个假说在当时没有任何理论依据——它纯粹是为了让公式契合实验数据而做出的假设。普朗克自己都不喜欢这个想法，他后来称其为'绝望中的行动'——因为'经典物理无论如何也解释不了这个现象'。",
  "lifeStoryEn": "Born in 1858 in Germany, Planck was advised against studying physics as 'nothing new remains to be discovered.' In 1900, as a 'desperate act,' he proposed energy quantization to explain blackbody radiation data — an idea he himself disliked but launched quantum physics.",
  "keyContributions": [
    { "title": "能量量子化假说", "titleEn": "Energy Quantization", "year": 1900, "desc": "普朗克在解释黑体辐射谱时发现：如果假设能量以不连续的'能量子'（hv）为单位发射和吸收，就可以完美拟合实验数据。其中h是一个新的自然常数——普朗克常数（6.626×10⁻³⁴ J·s）。普朗克当时认为这只是一个数学技巧，没想到它揭示了自然界最根本的真理：能量是离散的。这一假说标志着量子力学的诞生。", "descEn": "To explain blackbody radiation, Planck assumed energy is emitted/absorbed in discrete 'quanta' of size hv. The constant h (Planck's constant) became fundamental. He thought it was a mathematical trick; it was the birth of quantum mechanics.", "type": "theory" }
  ],
  "famousEvents": [
    { "title": "量子概念的诞生之夜", "year": 1900, "desc": "1900年12月14日，普朗克在德国物理学会上宣读了他的黑体辐射论文。当天在场的物理学家们没有意识到——他们正在见证物理学的分水岭。经典物理学的统治在这一天结束了，量子时代开始了。后来这一天被称为'量子力学的生日'。普朗克时年42岁——在这个年纪大多数物理学家已经定型，但他却做出了职业生涯中最革命性的发现。", "titleEn": "Birth of Quantum Physics", "descEn": "On December 14, 1900, Planck presented his blackbody radiation paper to the German Physical Society. No one realized they were witnessing a watershed moment — the end of classical physics and the birth of the quantum era." }
  ],
  "anecdote": "普朗克本人终其一生都试图将量子概念纳入经典物理框架——他花了很多年试图'挽回'经典物理，但最后发现不可能。他的儿子回忆说：'父亲提出了一个他自己都不相信的理论，而这个理论却彻底改变了他所热爱的物理学。'普朗克有一句名言广为流传：'新的科学真理不是靠说服反对者而获胜的——而是因为反对者最终都死了，熟悉新真理的新一代成长起来了。'",
  "anecdoteEn": "Planck spent years trying to reconcile quantum theory with classical physics — he had launched a revolution he himself resisted. His famous quote: 'A new scientific truth does not triumph by convincing its opponents, but because its opponents eventually die.'",
  "aiReview": "普朗克的'绝望中的行动'是人类科学史上最成功的被迫妥协之一。一个严谨的、热爱经典物理的德国教授，被迫提出了一个自己都不愿相信的假说——然后这个假说撼动了整个物理学的根基。这个故事告诉我们，科学家有时需要做出违背自己直觉和审美的理论创新——不是因为他们喜欢，而是因为数据强迫他们这么做。普朗克的诚实——他忠实于实验数据而不是自己的理论偏好——是科学精神最纯粹的表现。"
})

# ═══════════════════════════════════════════
# Heisenberg
# ═══════════════════════════════════════════
enrich('heisenberg', {
  "summary": "海森堡是量子力学的核心奠基人之一。他创立了矩阵力学——量子力学的第一个完整的数学框架，并提出了不确定性原理，揭示了微观世界测量行为的根本限制。",
  "summaryEn": "Heisenberg was a core founder of quantum mechanics. He created matrix mechanics — the first complete mathematical formulation of quantum theory — and proposed the uncertainty principle, revealing fundamental limits of measurement.",
  "lifeStory": "海森堡1901年出生于德国维尔茨堡的一个学术家庭。他在慕尼黑大学师从索末菲学习理论物理，在哥廷根大学师从玻恩，在哥本哈根与玻尔一起工作——这条路径使他直接进入了量子理论的前沿。1925年在他仅23岁时患严重花粉热，到北海的黑尔戈兰岛休养。在那里他萌生了用矩阵表示物理量的想法——这就是矩阵力学的诞生。1927年他提出了不确定性原理。二战期间他是德国核研究项目的核心人物之一。战后他对德国科学的重建起了重要作用。",
  "lifeStoryEn": "Born in 1901 in Germany, Heisenberg was only 23 when he conceived matrix mechanics during a hay fever retreat on Heligoland island. He proposed the uncertainty principle in 1927 at age 26, and was central to German nuclear research during WWII.",
  "keyContributions": [
    { "title": "不确定性原理", "titleEn": "Uncertainty Principle", "year": 1927, "desc": "粒子的位置和动量不能同时被精确测量——位置越精确，动量就越不确定，反之亦然。这个不确定性不是测量技术的问题，而是自然界的根本性质。这个原理划定了人类认识微观世界的极限——不是因为我们不够聪明，而是因为世界本身就是如此运作的。", "descEn": "The more precisely a particle's position is known, the less precisely its momentum can be known. This is not a measurement limitation but a fundamental property of nature — a fundamental limit on human knowledge of the microscopic world.", "type": "theory" },
    { "title": "矩阵力学", "titleEn": "Matrix Mechanics", "year": 1925, "desc": "海森堡提出了一个激进的想法：抛弃不可观测的概念（如电子的轨道），只使用可观测的物理量（如辐射频率和强度）来建立新理论。他发现这些量可以用矩阵——一种非交换的数学对象——来表示。矩阵的乘法不满足交换律（A×B ≠ B×A），这正好对应量子力学中的核心特征。", "descEn": "Proposed building quantum theory using only observable quantities (like radiation frequencies), abandoning unobservable concepts. These quantities formed non-commutative matrices — the non-commutativity captured quantum mechanics' essence.", "type": "theory" }
  ],
  "famousEvents": [
    { "title": "黑尔戈兰岛的灵感", "year": 1925, "desc": "23岁的海森堡因严重花粉热到北海的黑尔戈兰岛休养。在那里他整夜整夜地思考原子物理问题。一天凌晨三时，他得到了一个关键洞见：用矩阵表示物理量——虽然他当时甚至不知道什么是矩阵。在亢奋状态下他进行了大量计算，发现矩阵的不交换性正好适用于量子系统。兴奋的他凌晨三点跑到岛上的岩石上——在那里迎来了日出。几周后他向玻恩提交了那篇标志量子力学诞生的论文。", "titleEn": "Inspiration on Heligoland", "descEn": "At age 23, suffering hay fever on Heligoland island, Heisenberg realized at 3 AM that matrices could represent quantum quantities — though he didn't yet know matrix theory. Excited, he climbed the island's cliffs to watch the sunrise." }
  ],
  "anecdote": "海森堡提出矩阵力学时甚至不知道什么是矩阵！当他把论文交给导师玻恩时，玻恩立刻意识到海森堡发现的是矩阵运算——因为那些乘法规则就是矩阵乘法。海森堡后来承认他在大学里逃了很多数学课。玻恩和约旦随后帮助他完善了矩阵力学的数学形式——但核心的物理思想，全部来自这个23岁逃课的年轻人。",
  "anecdoteEn": "Heisenberg didn't even know matrix theory when he invented matrix mechanics! His advisor Born recognized the multiplication rules as matrix operations. Heisenberg had skipped math classes — but the physics was all his.",
  "aiReview": "海森堡的不确定性原理常被公众误解为'测不准'——好像是说测量工具不够精密。实际上它的含义深得多：它说粒子本身就没有同时确定的位置和动量。这意味着微观世界的实在性在某种程度上是'模糊的'或'概率性的'。这个发现对哲学的影响不亚于哥白尼革命——它告诉我们，世界的底层结构从根本上超出了经典物理的直观图像。"
})

# ═══════════════════════════════════════════
# Fermi
# ═══════════════════════════════════════════
enrich('fermi', {
  "summary": "费米是最后一位同时精通理论和实验的物理学全才。他建造了世界上第一座核反应堆，在量子统计（费米-狄拉克统计）、β衰变理论和粒子物理方面做出了开创性贡献。他被广泛认为是20世纪最杰出的意大利科学家。",
  "summaryEn": "Fermi was the last physicist equally masterful in theory and experiment. He built the world's first nuclear reactor and made pioneering contributions to quantum statistics, beta decay theory, and particle physics.",
  "lifeStory": "费米1901年出生于意大利罗马的一个铁路官员家庭。他从小就显示出数学和物理的天赋——10岁时就能理解方程x²+y²=r²表示一个圆。1918年获得奖学金进入比萨高等师范学校学习。21岁获得博士学位。1926年提出费米-狄拉克统计，描述了费米子（如电子）的量子行为。1938年因在中子慢化方面的研究获诺贝尔奖——颁奖后他利用出国领奖的机会直接去了美国，逃离了墨索里尼的法西斯统治（他的妻子是犹太人）。在美国他领导了芝加哥1号堆（芝加哥冶金实验室）的建设——1942年12月2日实现了人类第一次自持核链式反应。他后来在曼哈顿计划和战后物理学中发挥了重要作用。",
  "lifeStoryEn": "Born in 1901 in Rome, Fermi earned his PhD at 21. He proposed Fermi-Dirac statistics in 1926. After winning the Nobel in 1938, he fled fascist Italy. On Dec 2, 1942, he built Chicago Pile-1 — the world's first nuclear reactor.",
  "keyContributions": [
    { "title": "第一座核反应堆", "titleEn": "First Nuclear Reactor", "year": 1942, "desc": "1942年12月2日下午3点25分，在芝加哥大学一个废弃壁球场的临时实验室里，费米领导的团队创建了人类第一座核裂变链式反应堆。这个由石墨块和铀堆砌而成的庞然大物被称为'芝加哥1号堆'。费米亲自操控了控制棒——当反应达到临界时，他平静地说:'反应已经自持了。'这是人类可控利用核能的历史性时刻。", "descEn": "At 3:25 PM on Dec 2, 1942, in a converted squash court under the University of Chicago, Fermi achieved the first self-sustaining nuclear chain reaction. He calmly announced: 'The reaction is self-sustaining.'", "type": "experiment" },
    { "title": "费米-狄拉克统计", "titleEn": "Fermi-Dirac Statistics", "year": 1926, "desc": "与狄拉克分别独立提出了一类粒子——费米子（如电子、质子、中子）的量子统计行为。费米子的核心特征是泡利不相容原理：两个费米子不能占据同一个量子态。这一统计法解释了金属的导电性、白矮星的稳定性（钱德拉塞卡极限）和元素周期表的电子排布。", "descEn": "With Dirac, described the statistical behavior of fermions (electrons, protons, neutrons). The Pauli exclusion principle — no two fermions share the same quantum state — explains conductivity, white dwarfs, and the periodic table.", "type": "theory" }
  ],
  "famousEvents": [
    { "title": "芝加哥1号堆的谨慎与勇气", "year": 1942, "desc": "在实验前，费米被问及反应堆会不会失控爆炸。他说:'可靠性是99.9%。'有人问他那0.1%呢？费米耸耸肩:'那我们可能都会被赶出去。'他设计了三重安全措施：控制棒、镉溶液（自动注入）和一组站在旁边随时准备'浇灭'的应急队员。但所有安全人员都知道——如果出了事故，他们中的很多人会因为辐射暴露而丧生。实验成功了——费米的纸条上写着:'1942年12月2日，人类实现了第一次自持核链式反应。'", "titleEn": "Chicago Pile-1", "descEn": "When asked if the reactor could explode, Fermi estimated 99.9% reliability. For the 0.1%? 'We might all be evicted.' He designed triple safety measures. The historic experiment succeeded, ushering in the nuclear age." }
  ],
  "anecdote": "费米是出了名的心算天才——他能在一瞬间估算出任何数量级。他在曼哈顿计划期间提出了'费米问题'——用粗略估算解决复杂问题。一个经典例子：他估算芝加哥的钢琴调音师数量——先估算芝加哥人口、家庭数、钢琴数、每台钢琴的调音频率、每个调音师每天能调多少台——最后得出了一个跟实际统计差不多的数字。'费米问题'至今仍是物理教学中训练量级感的经典方法。",
  "anecdoteEn": "Fermi was famous for 'Fermi problems' — order-of-magnitude estimation. Classic example: estimating Chicago's piano tuners from first principles (population, households, pianos, tuning frequency, tuner capacity). Still used in physics education.",
  "aiReview": "费米的天才体现在两个方面：首先，他既能做高深的数学推演（费米-狄拉克统计），又能亲手建造复杂的实验设备（芝加哥反应堆），这种理论+实验的全能在20世纪后期变得越来越罕见。其次，他的'费米问题'展示了一种特别的思维方式——在没有精确数据时，用逻辑和量级感来逼近答案。这种'量级思维'在今天的机器学习和大数据时代反而更加珍贵——因为它训练的是对数字的感觉而不是对数字的记忆。"
})

# ═══════════════════════════════════════════
# Li Zhengdao
# ═══════════════════════════════════════════
enrich('li-zhengdao', {
  "summary": "李政道与杨振宁共同提出弱相互作用中宇称不守恒，推翻了物理学的古老信念。他是历史上第二年轻的诺贝尔物理学奖获得者（31岁）。在统计物理、场论和天体物理方面也有重要贡献。",
  "summaryEn": "Lee jointly proposed parity non-conservation in weak interactions with Yang, overturning a long-held physics belief. At 31, he was the second-youngest Nobel laureate in physics history.",
  "lifeStory": "李政道1926年出生于上海一个知识分子家庭。抗战期间他就读于浙江大学和西南联合大学，师从束星北和吴大猷。1946年赴美留学，师从费米——费米对他的评价极高。1953年进入哥伦比亚大学任教。1956年与杨振宁合作提出宇称不守恒理论——推翻了物理学界长期认为'镜像世界中的物理定律与真实世界完全相同'的信念。吴健雄在1957年用实验证实了这一理论——同年李政道和杨振宁即获诺贝尔奖。从提出理论到获奖只用了一年多，这是诺奖史上最快的认可之一。李政道后来在统计力学、场论和相对论方面继续做出了重要贡献。他一直致力于推动中国科学事业的发展。",
  "lifeStoryEn": "Born in 1926 in Shanghai, Lee studied at Southwest Associated University, then under Fermi in the US. At age 31, he co-discovered parity non-conservation with Yang and won the Nobel Prize the same year — one of the fastest Nobel recognitions in history.",
  "keyContributions": [
    { "title": "宇称不守恒理论", "titleEn": "Parity Non-conservation", "year": 1956, "desc": "李政道和杨振宁在解决'τ-θ之谜'时提出了一个颠覆性的假设：弱相互作用中宇称（物理定律在镜像变换下的对称性）可能不守恒。这个假设打破了物理学界多年来的思维定式——人们从未怀疑过宇称守恒，因为它被认为是天经地义的。吴健雄的钴-60实验在1957年初确认了这一理论。", "descEn": "With Yang, proposed parity is not conserved in weak interactions — breaking a fundamental assumption. Wu's experiment confirmed it in 1957. The fastest Nobel Prize turnaround in history: theory to prize in 18 months.", "type": "theory" }
  ],
  "anecdote": "李政道在西南联大时期学习条件极其艰苦——没有电灯，他用桐油灯照明；没有参考书，他靠背下来的资料学习。他的老师吴大猷见他如此用功，把自己的笔记本借给他抄写。多年后李政道回忆说：'那些手抄的资料和笔记，比任何教科书都珍贵。'后来他在哥伦比亚大学任教时，把自己的全部工资捐出来设立了奖学金——资助中国学生赴美深造。",
  "anecdoteEn": "At Southwest Associated University, Lee studied by tung oil lamp with no textbooks. His professor Wu Dayou lent him notes to copy. Later at Columbia, he donated his entire salary to fund Chinese students studying in the US.",
  "aiReview": "李政道和杨振宁的合作是华人科学史上最璀璨的双子星。两个年轻的华人物理学家推翻了全世界物理学家的共识——这种勇气来自于他们对数据的认真和对权威的不盲从。弱相互作用宇称不守恒的发现过程展示了科学中最宝贵的品质：当实验事实与理论预期不符时，应该大胆质疑理论而不是忽略事实。"
})

# ═══════════════════════════════════════════
# Wu Jianxiong
# ═══════════════════════════════════════════
enrich('wu-jianxiong', {
  "summary": "吴健雄是世界上最杰出的实验物理学家之一。她用精密的β衰变实验证实了李政道和杨振宁的宇称不守恒理论，这项实验被称为'物理学史上最优雅的实验之一'。她被公认为20世纪最伟大的女性物理学家。",
  "summaryEn": "Wu was one of the world's greatest experimental physicists. Her precise beta decay experiment confirmed Lee and Yang's parity non-conservation theory — called 'one of the most elegant experiments in physics history.'",
  "lifeStory": "吴健雄1912年出生于江苏太仓的一个开明家庭。1934年毕业于中央大学物理系。1936年赴美留学，在加州大学伯克利分校师从劳伦斯和塞格雷。1940年获得博士学位。她毕业后因为性别歧视未能获得理想的教职，直到1944年才在普林斯顿大学有了临时职位。二战期间她参与了曼哈顿计划（虽然她的角色被长期保密）。1957年她完成了宇称不守恒的实验验证——这个实验如此精确和优雅，以至于连杨振宁和李政道的反对者都被说服了。虽然她未能获得诺贝尔奖，但获得了沃尔夫物理奖等众多荣誉。她晚年致力于推动女性在科学界的发展。",
  "lifeStoryEn": "Born in 1912 in Jiangsu, Wu earned her PhD from Berkeley in 1940. Her elegant 1957 beta decay experiment confirmed parity non-conservation. Though controversially denied the Nobel Prize, she later received the Wolf Prize and many other honors.",
  "keyContributions": [
    { "title": "宇称不守恒的实验验证", "titleEn": "Experimental Proof of Parity Non-conservation", "year": 1957, "desc": "吴健雄将放射性钴-60冷却到接近绝对零度，施加磁场使原子核自旋定向排列，测量β衰变电子的发射方向——如果宇称守恒，电子应在各方向均匀发射；实际测到某一方向的电子远远多于另一方向——宇称确实不守恒。这个实验的技术难度极高——在超低温和极弱放射性的条件下进行精密测量，她的团队做到了。", "descEn": "Cooled cobalt-60 near absolute zero in a magnetic field, measured beta emission direction — electrons preferred one direction, proving parity non-conservation. An extremely difficult low-temperature precision experiment.", "type": "experiment" }
  ],
  "famousEvents": [
    { "title": "诺奖的最大不公之一", "year": 1957, "desc": "1957年诺贝尔物理学奖授予了李政道和杨振宁，但吴健雄——完成了决定性实验的人——被忽略了。很多人认为这是诺奖史上最大的不公之一。诺贝尔奖委员会后来在多个场合被问到这个问题，始终没有给出令人满意的解释。吴健雄本人从未公开抱怨过——她在给朋友的信中说:'为科学事业做出贡献本身就是最大的奖赏。'但她后来一次演讲中说:'在科学界，女性面临的偏见就像一层玻璃天花板——看不见但确实存在。'", "titleEn": "Nobel Prize Controversy", "descEn": "Wu was controversially excluded from the 1957 Nobel Prize despite performing the crucial experiment. Widely considered a major injustice, she never publicly complained, but worked to advance women in science." }
  ],
  "anecdote": "吴健雄在伯克利读博期间的导师是劳伦斯（回旋加速器发明者，诺奖得主）和塞格雷（后来也是诺奖得主）。塞格雷曾开玩笑说吴健雄是他教过的最好的学生——'如果她是男的，我会毫不犹豫地推荐她去任何地方。'这个'毫不犹豫'后面潜藏的性别歧视，恰恰是吴健雄要用一生去面对的。她的博士论文被劳伦斯认为'比大多数男性的博士论文更出色'——但这个'比男性'的比较本身，也说明了当时环境的不公。",
  "anecdoteEn": "At Berkeley, Wu's adviser Segrè called her the best student he ever taught — 'If she were a man, I wouldn't hesitate to recommend her anywhere.' The conditional praise itself revealed the gender discrimination she faced throughout her career.",
  "aiReview": "吴健雄是诺贝尔奖最著名的'遗珠'之一。她的实验之所以被称为'物理学史上最优雅的实验'，是因为它用一个极为简洁的设计，回答了一个极为深刻的问题。在科学中，理论家往往比实验家更吸睛——李政道和杨振宁的名字家喻户晓，而完成关键实验的吴健雄却在公众认知中相对暗淡。但科学界知道真相：如果吴健雄的实验结果没有证实宇称不守恒，李-杨的理论就只是一个大胆的猜想。理论和实验在科学中是平等的两翼。"
})

# ═══════════════════════════════════════════
# Qiu Chengtong
# ═══════════════════════════════════════════
enrich('qiu-chengtong', {
  "summary": "丘成桐证明了卡拉比猜想，开创了卡拉比-丘流形——这一几何构造后来成为弦论的关键组成部分。他是首位获得菲尔兹奖的华人数学家（1982年），在微分几何和偏微分方程领域做出了世界级贡献。",
  "summaryEn": "Yau proved the Calabi conjecture, creating Calabi-Yau manifolds — geometric structures that later became crucial to string theory. He was the first Chinese Fields Medalist (1982).",
  "lifeStory": "丘成桐1949年出生于广东汕头，后随家人移居香港。他在香港中文大学学习数学，展现出超群的天赋。1969年赴加州大学伯克利分校深造，师从陈省身——后者推荐他去了最好的微分几何中心。1971年22岁获博士学位。1976年他证明了困扰数学界二十多年的卡拉比猜想——证明存在一类特殊的紧致空间（卡拉比-丘流形），其内部具有奇特的拓扑结构。这项工作让他获得了1982年的菲尔兹奖。他的工作后来在理论物理中产生了意想不到的巨大影响——1980年代物理学家发现卡拉比-丘流形正好可以用来解释弦论中额外的维度。",
  "lifeStoryEn": "Born in 1949 in Shantou, China, Yau studied at CUHK. He earned his PhD at Berkeley under Chern at 22. In 1976 he proved the Calabi conjecture, creating Calabi-Yau manifolds. Won the Fields Medal in 1982. His geometry later became central to string theory.",
  "keyContributions": [
    { "title": "卡拉比-丘流形", "titleEn": "Calabi-Yau Manifolds", "year": 1976, "desc": "丘成桐解决了意大利数学家卡拉比在1954年提出的一个猜想——证明了一类特殊的紧致凯勒流形的存在。这些空间（卡拉比-丘流形）是复杂的六维几何结构，具有极小的内部曲率。丘成桐用高超的分析技巧将纯几何问题转化为偏微分方程问题并成功求解。十年后，物理学家发现这些流形是弦论中卷曲的额外维度的理想模型——这个几何发现变成了指导宇宙本质的理论基础。", "descEn": "Proved the Calabi conjecture about compact Kähler manifolds. These 6D Calabi-Yau manifolds became crucial when physicists discovered they perfectly model the curled-up extra dimensions in string theory.", "type": "theory" },
    { "title": "正质量猜想证明", "titleEn": "Positive Mass Theorem", "year": 1979, "desc": "与舍恩合作证明了广义相对论中的正质量猜想：一个孤立物理系统的总质量必须为正（除非是平坦的闵可夫斯基时空）。这个猜想在广义相对论中悬而未决了多年，它的成立是宇宙稳定性的基础。", "descEn": "With Schoen, proved the positive mass theorem in general relativity: an isolated physical system's total mass must be positive (unless flat spacetime). This is fundamental to cosmic stability.", "type": "theory" }
  ],
  "famousEvents": [
    { "title": "第一个华裔菲尔兹奖", "year": 1982, "desc": "1982年华沙国际数学家大会上，丘成桐被授予菲尔兹奖——数学界的最高荣誉，相当于数学的诺贝尔奖。他是第一位获此殊荣的华裔数学家。在颁奖典礼上他说:'数学不是孤立的学问，它和物理学的深刻联系证明了宇宙可以用数学来理解的毕达哥拉斯信念。'", "titleEn": "First Chinese Fields Medal", "descEn": "At the 1982 International Congress of Mathematicians in Warsaw, Yau became the first Chinese-descendant mathematician to win the Fields Medal, mathematics' highest honor." }
  ],
  "anecdote": "丘成桐在香港读书时的老师曾建议他去读工程学——因为'学数学找不到工作'。他差点就听了。但陈省身的著作《微分几何》点燃了他对几何的热情。后来他成为伯克利的博士生时，陈省身已经是那里的教授。陈省身有一天跟他说:'如果你能解决卡拉比猜想，你就将成为伟大的数学家。'丘成桐花了三年时间——其中有两年他以为卡拉比猜想是错误的，试图证明它不成立。最后他转向证明它是对的——结果它是对的。",
  "anecdoteEn": "Yau nearly studied engineering because 'mathematicians can't find jobs.' His teacher Chern's differential geometry book inspired him instead. Chern told him: 'Solve Calabi's conjecture and you'll be a great mathematician.' It took Yau three years — two trying to disprove it, then proving it correct.",
  "aiReview": "丘成桐的工作是纯数学与理论物理学相互滋养的绝佳案例。他解决卡拉比猜想是出于纯几何的好奇——这些六维流形是否存在，是一个纯粹的数学问题。但十年后它变成了弦论的基础，因为物理学家们需要一个容纳额外维度的几何容器。这种'数学超前于物理'的现象在科学史上反复出现——黎曼几何为爱因斯坦准备好了广义相对论的舞台，卡拉比-丘流形为弦论准备好了几何框架。这就是为什么我们永远不能只看'眼前的应用'来评判数学的价值。"
})

# ═══════════════════════════════════════════
# Tu Youyou
# ═══════════════════════════════════════════
enrich('tu-youyou', {
  "summary": "屠呦呦发现了青蒿素——一种治疗疟疾的特效药，为全球疟疾防治做出了革命性贡献。2015年获得诺贝尔生理学或医学奖，是首位在中国本土完成研究的诺贝尔科学奖得主。",
  "summaryEn": "Tu Youyou discovered artemisinin — a revolutionary treatment for malaria. She won the 2015 Nobel Prize in Physiology or Medicine, the first science Nobel laureate for research conducted within China.",
  "lifeStory": "屠呦呦1930年出生于浙江宁波的一个知识分子家庭。1951年考入北京大学医学院药学系。毕业后她在中国中医研究院工作了五十多年。1969年中国政府启动了'523项目'——一个旨在发现抗疟药物的秘密国家项目。屠呦呦被任命为课题组组长。她查阅了大量古代医书，从东晋葛洪的《肘后备急方》中得到关键启发——'青蒿一握，以水二升渍，绞取汁，尽服之'——这提示她高温可能破坏青蒿的有效成分，于是改用低温乙醚萃取法成功提取了青蒿素。1972年她亲自试药确认了安全性。青蒿素后来成为全球抗疟的标准药物。",
  "lifeStoryEn": "Born in 1930 in Ningbo, Tu was appointed to China's Project 523 in 1969 to find a malaria cure. Inspired by a 4th-century medical text suggesting low-temperature extraction, she discovered artemisinin. She tested it on herself and it became the global standard malaria treatment.",
  "keyContributions": [
    { "title": "青蒿素的发现", "titleEn": "Discovery of Artemisinin", "year": 1972, "desc": "屠呦呦从古代医书中筛选了2000多种草药方，发现青蒿（Artemisia annua）的抗疟潜力。她注意到传统方法用高温煎煮可能破坏了有效成分，改用低沸点的乙醚在低温下提取，成功分离出青蒿素。在动物实验中效果极佳后，她不顾自身安全亲自进行了人体试验。她的发现至今已挽救了全球数百万疟疾患者的生命——世界卫生组织推荐以青蒿素为基础的联合疗法作为疟疾的一线治疗方案。", "descEn": "Screened 2,000+ herbal recipes from ancient medical texts. Realizing high heat might destroy the active compound, she used low-temperature ether extraction to isolate artemisinin. Self-tested it and saved millions of lives worldwide.", "type": "discovery" }
  ],
  "famousEvents": [
    { "title": "诺贝尔奖——迟到的认可", "year": 2015, "desc": "2015年屠呦呦获得诺贝尔生理学或医学奖时已经85岁。她在颁奖典礼上说:'这是中国科学家的荣誉。青蒿素是中医药送给世界的礼物。'她的获奖在中国引起了广泛关注——她是第一位在中国本土完成研究而获诺贝尔科学奖的科学家。这个迟来的认可也让世界注意到一个事实：1970年代中国科学家在极端困难的条件下取得了世界级的科研成果。", "titleEn": "The Nobel Prize", "descEn": "At 85, Tu won the 2015 Nobel Prize, saying: 'Artemisinin is a gift from traditional Chinese medicine to the world.' She was the first Chinese scientist to win a science Nobel for work conducted entirely in China." }
  ],
  "anecdote": "屠呦呦在发现青蒿素的过程中发挥了关键作用，但'523项目'是一个大型协作项目，涉及全国60多个研究机构的数百名科学家。项目具有浓厚的时代特色——国家机密项目的性质使参与者的贡献在很长时期内未被公开。屠呦呦说:'这是集体成果，我只是一个代表。'她的自述最能说明她的性格:'我这个人比较死板，做了就会一直做下去。科学没有捷径。'",
  "anecdoteEn": "Tu's discovery was part of a massive classified project involving hundreds of scientists. She said: 'This was a collective achievement — I'm just a representative.' Her motto: 'Science has no shortcuts.'",
  "aiReview": "屠呦呦的获奖意义超越了青蒿素本身。在西方科学范式主导全球的时代，她证明了古老的中医药传统同样可以孕育现代科学突破。她从东晋医书中的一句话获得了启发，用现代化学方法完成了提取——这是传统智慧与现代科学的完美结合。她的故事还告诉我们：最伟大的发现有时不需要最先进的设备，而是需要独特的视角和不屈的坚持——她在没有高科技仪器、几乎没有科研经费的条件下完成了改变世界的发现。"
})

# ═══════════════════════════════════════════
# Hippocrates
# ═══════════════════════════════════════════
enrich('hippocrates', {
  "summary": "希波克拉底被誉为西方医学之父。他开创了用理性和观察研究疾病的方法，将医学从巫术和宗教中解放出来。希波克拉底誓词成为医生职业道德的经典准则，沿用至今。",
  "summaryEn": "Hippocrates is known as the father of Western medicine. He pioneered the rational, observational study of disease, freeing medicine from superstition. The Hippocratic Oath remains a classic code of medical ethics.",
  "lifeStory": "希波克拉底约公元前460年出生于希腊科斯岛的一个医生世家——阿斯克勒庇亚德家族声称是医神阿斯克勒庇俄斯的后裔。他在科斯岛的医学校和库尼杜斯的医学校学习，后来在希腊各地行医和教学。他创立了科斯医学学派——强调通过仔细观察病人症状来诊断疾病，而不是依靠宗教仪式和魔法。他认为疾病不是神明的惩罚，而是由环境、饮食和生活方式等自然原因引起的。他主张'首先，不伤害'（Primum non nocere）的治疗原则。他撰写了约60篇医学论文（合称《希波克拉底文集》），涵盖了内科、外科、妇科和儿科等各个领域。",
  "lifeStoryEn": "Born around 460 BC on the Greek island of Cos, Hippocrates came from a family claiming descent from the god of medicine. He founded the Coan medical school, emphasizing observation over superstition. The Hippocratic Corpus of ~60 texts covers all fields of medicine.",
  "keyContributions": [
    { "title": "希波克拉底誓词", "titleEn": "Hippocratic Oath", "year": -400, "desc": "一份宣誓医生职业道德的经典誓词——内容包括尊师重道、以病人利益为重、不伤害病人、保护病人隐私、不滥用医生权力等。誓词的开头'我以医神阿波罗之名宣誓'虽然在现代版本中常被修改，但其核心精神——'首先，不伤害'——仍然是全球医学伦理的基石。", "descEn": "The classic oath of medical ethics: respect teachers, put patients first, do no harm, protect privacy, never abuse medical authority. Its core principle — 'First, do no harm' — remains the foundation of global medical ethics.", "type": "work" },
    { "title": "四体液学说", "titleEn": "Four Humors Theory", "year": -400, "desc": "希波克拉底提出了人体由四种体液（血液、黏液、黄胆汁、黑胆汁）组成的理论，健康的本质是四种体液的平衡。虽然这个理论的具体内容早已被现代医学否定，但它的方法论意义在于——它用自然的因素（体液）而非超自然力量（神罚、巫术）来解释疾病。这是医学从巫术走向科学的第一步。", "descEn": "Health results from balance of four bodily fluids (blood, phlegm, yellow bile, black bile). The theory itself is obsolete, but its revolutionary idea was explaining disease through natural causes, not supernatural forces.", "type": "theory" }
  ],
  "famousEvents": [
    { "title": "区分医学与巫术", "year": -400, "desc": "在希波克拉底之前，希腊人普遍认为疾病是神明的惩罚或魔鬼的附身——治疗方法是去神庙祈祷或接受驱魔术。希波克拉底第一次系统性地主张：医生应该仔细观察病人的症状、记录病程、寻找疾病的自然原因。他的著作中记载了大量病例——包括症状、治疗和结果——这是人类历史上最早的临床病例记录。", "titleEn": "Separating Medicine from Magic", "descEn": "Before Hippocrates, Greeks believed disease was divine punishment. He introduced clinical observation, case recording, and natural causation for disease — the first systematic separation of medicine from religion and magic." }
  ],
  "anecdote": "希波克拉底曾为马其顿国王佩尔狄卡斯二世诊断一种怪病——国王消瘦、精神萎靡、所有医生都束手无策。希波克拉底观察后判断国王患的不是身体疾病而是'相思病'——爱上了已故父亲的情妇。据说诊断后国王的症状就缓解了。这个故事（真实性存疑）体现了希波克拉底的一个重要信念：医生不但要治疗身体，还要理解心理。",
  "anecdoteEn": "Hippocrates diagnosed the King of Macedon's mysterious illness as lovesickness — the king was in love with his late father's mistress. Whether true or not, the story illustrates Hippocrates' belief that physicians must understand the mind as well as the body.",
  "aiReview": "希波克拉底的伟大不在于任何具体的医学发现——四体液学说早已被推翻——而在于他改变了人类思考疾病的方式。在他之前，生病=被神惩罚；在他之后，生病=需要被研究理解的自然过程。这种'去神秘化'是理性主义在医学领域的第一次胜利。今天，希波克拉底的名字出现在每一张医学院的毕业典礼上——新医生们朗读誓词时，他们不仅在继承一套职业道德，更在确认一种思维方式：医学是对自然的理解，而不是对超自然的祈祷。"
})

# ═══════════════════════════════════════════
# Schrödinger
# ═══════════════════════════════════════════
enrich('schrodinger', {
  "summary": "薛定谔提出了量子力学的基本方程——薛定谔方程，创立了波动力学。他的'薛定谔的猫'思想实验成为量子力学最著名的比喻。",
  "summaryEn": "Schrödinger formulated the fundamental equation of quantum mechanics — the Schrödinger equation — and founded wave mechanics. His 'Schrödinger's cat' became the most famous metaphor in quantum physics.",
  "lifeStory": "薛定谔1887年出生于奥地利维也纳。他在维也纳大学学习物理学，1926年他发表了系列论文建立了波动力学，提出了薛定谔方程。他在1935年提出了'薛定谔的猫'思想实验，目的是讽刺量子力学的哥本哈根诠释。",
  "lifeStoryEn": "Born in 1887 in Vienna, Schrödinger published his wave equation in 1926. His 1935 'Schrödinger's cat' paradox mocked quantum interpretation but became its most famous illustration.",
  "keyContributions": [
    { "title": "薛定谔方程", "titleEn": "Schrödinger Equation", "year": 1926, "desc": "量子力学的基本方程，描述波函数如何随时间演化。它是偏微分方程，适用范围从基本粒子到原子分子——几乎所有凝聚态物理和量子化学都依赖于它。", "descEn": "The fundamental equation of quantum mechanics describing wave function evolution. Underpins all of quantum chemistry and condensed matter physics.", "type": "theory" },
    { "title": "薛定谔的猫", "titleEn": "Schrödinger's Cat", "year": 1935, "desc": "思想实验：猫在盒子里既死又活直到被观察。薛定谔用此讽刺量子叠加的荒谬，但物理学家们最终接受了这个结论。", "descEn": "Thought experiment where a cat is both dead and alive until observed. Meant to mock quantum superposition, but physicists accepted it as nature's reality.", "type": "theory" }
  ],
  "aiReview": "薛定谔方程是科学史上最优雅的方程之一，薛定谔的猫则反映了量子力学与常识之间的深刻冲突。"
})

# ═══════════════════════════════════════════
# Hawking
# ═══════════════════════════════════════════
enrich('hawking', {
  "summary": "霍金提出了黑洞辐射（霍金辐射）理论，将广义相对论与量子力学联系起来。他的《时间简史》成为史上最畅销的科普著作之一。",
  "summaryEn": "Hawking proposed Hawking radiation, connecting general relativity with quantum mechanics. His 'A Brief History of Time' became one of the best-selling popular science books ever.",
  "lifeStory": "霍金1942年出生于英国牛津，21岁被诊断出ALS，被预言只能活两年——但他活到了76岁。他全身瘫痪，通过语音合成器交流。1974年提出霍金辐射理论。1988年《时间简史》出版，全球销量超2500万册。",
  "lifeStoryEn": "Born in 1942 in Oxford, Hawking was diagnosed with ALS at 21, given two years — he lived to 76. Completely paralyzed, he communicated via speech synthesizer. Proposed Hawking radiation in 1974. 'A Brief History of Time' sold 25M+ copies.",
  "keyContributions": [
    { "title": "霍金辐射", "titleEn": "Hawking Radiation", "year": 1974, "desc": "霍金发现：由于量子效应，黑洞会发射粒子并逐渐蒸发。这打破了'黑洞只进不出'的传统观念，将广义相对论、量子力学和热力学联系了起来。", "descEn": "Black holes emit particles and slowly evaporate due to quantum effects. Connected general relativity, quantum mechanics, and thermodynamics.", "type": "theory" }
  ],
  "aiReview": "霍金成为文化偶像不仅因为科学贡献，更因为他展现了不屈的人类精神——身体被疾病囚禁半个世纪，思想却在宇宙最深处自由翱翔。"
})

# ═══════════════════════════════════════════
# Rutherford
# ═══════════════════════════════════════════
enrich('rutherford', {
  "summary": "卢瑟福通过金箔实验发现了原子核，提出了原子的核结构模型，发现了质子并实现了第一次人工核嬗变。他是核物理学之父。",
  "summaryEn": "Rutherford discovered the atomic nucleus, proposed the nuclear model, discovered the proton, and achieved the first artificial nuclear transmutation. Father of nuclear physics.",
  "lifeStory": "卢瑟福1871年出生于新西兰农民家庭。1909年他的金箔实验发现了原子核。1919年发现质子并实现人工核嬗变。他的实验室培养了12位诺贝尔奖得主。",
  "lifeStoryEn": "Born in 1871 in New Zealand. His 1909 gold foil experiment revealed the atomic nucleus. Discovered the proton in 1919. His lab trained 12 Nobel laureates.",
  "keyContributions": [
    { "title": "原子核的发现", "titleEn": "Discovery of Atomic Nucleus", "year": 1911, "desc": "α粒子轰击金箔时少量被反弹回来，证明原子内部有一个致密的核心——原子核，推翻了汤姆孙的布丁模型。", "descEn": "Alpha particles bouncing off gold foil revealed a dense atomic nucleus, overturning the plum pudding model.", "type": "discovery" },
    { "title": "质子发现与人工核嬗变", "titleEn": "Proton & Transmutation", "year": 1919, "desc": "用α粒子轰击氮产生了质子——实现了炼金术士梦想的人工元素转化。", "descEn": "Bombarding nitrogen with alpha particles produced protons — the alchemist's dream of artificial transmutation realized.", "type": "discovery" }
  ],
  "aiReview": "卢瑟福的实验室用'我们没钱，所以必须思考'的精神培养了12位诺奖得主，至今无人打破。"
})

# ═══════════════════════════════════════════
# Leibniz
# ═══════════════════════════════════════════
enrich('leibniz', {
  "summary": "莱布尼茨独立于牛顿发明了微积分，其符号体系至今通用。他在二进制、数理逻辑和形而上学方面也有开创性贡献。",
  "summaryEn": "Leibniz independently invented calculus alongside Newton — his notation still used today. He pioneered binary arithmetic and made contributions to logic and philosophy.",
  "lifeStory": "莱布尼茨1646年出生于德国莱比锡。20岁获博士学位。1684年发表微积分（符号dx,∫沿用至今）。发明了二进制算术——后成为计算机基础。作为哲学家提出了'单子论'。",
  "lifeStoryEn": "Born in 1646 in Leipzig. PhD at 20. Published calculus in 1684 (notation still used). Invented binary arithmetic, later the basis of computing. Philosopher of 'monads.'",
  "keyContributions": [
    { "title": "微积分", "titleEn": "Calculus", "year": 1684, "desc": "独立于牛顿发明微积分，其符号体系(dx,∫)因为更方便而被后世采纳为标准。", "descEn": "Independently invented calculus; his notation (dx,∫) was universally adopted as standard.", "type": "theory" }
  ],
  "aiReview": "与牛顿的优先权之争导致英国数学界拒绝使用莱布尼茨的优秀符号，落后欧洲大陆一个世纪——科学共同体的争斗有时会损害科学本身。"
})

# ═══════════════════════════════════════════
# Hinton
# ═══════════════════════════════════════════
enrich('hinton', {
  "summary": "辛顿是深度学习之父，推动了反向传播算法的实用化，发明了深度信念网络，开启了人工智能革命。2018年获图灵奖。",
  "summaryEn": "Hinton is the godfather of deep learning. He made backpropagation practical, invented deep belief networks, and sparked the AI revolution. Winner of the 2018 Turing Award.",
  "lifeStory": "辛顿1947年出生于伦敦，高曾祖父是布尔代数创始人乔治·布尔。在1980年代主流AI追求符号逻辑时坚持神经网络研究。1986年发表反向传播算法经典论文。2006年提出深度信念网络。2012年ImageNet夺冠引爆深度学习浪潮。",
  "lifeStoryEn": "Born in 1947 in London, descendant of George Boole. Persisted with neural networks during AI winter. His 1986 backpropagation paper and 2006 deep belief networks sparked the deep learning revolution.",
  "keyContributions": [
    { "title": "反向传播算法", "titleEn": "Backpropagation", "year": 1986, "desc": "展示了如何让多层神经网络有效地学习——通过从输出向输入逐层传递误差信号来调整权重。这篇论文开启了神经网络时代。", "descEn": "Showed how multi-layer neural networks learn efficiently by propagating error backwards through layers. Launched the neural network era.", "type": "theory" },
    { "title": "深度信念网络", "titleEn": "Deep Belief Networks", "year": 2006, "desc": "提出逐层预训练方法，解决了深层网络的训练难题——被广泛认为是深度学习革命的开端。", "descEn": "Layer-by-layer pre-training solved the deep network training problem — considered the start of the deep learning revolution.", "type": "theory" }
  ],
  "aiReview": "辛顿用三十年逆流而上的坚持证明了：真正革命性的思想往往需要时间来证明自己的价值。"
})

# ═══════════════════════════════════════════
# Dalton
# ═══════════════════════════════════════════
enrich('dalton', {
  "summary": "道尔顿提出了近代原子论，用原子概念解释了化学反应中的定量关系，开创了分析化学和原子量的测定。他是现代化学的奠基人之一。",
  "summaryEn": "Dalton proposed modern atomic theory, explaining chemical reactions with atoms. He pioneered analytical chemistry and atomic weight measurement.",
  "lifeStory": "道尔顿1766年出生于英国一个农民家庭。他靠自学成为教师和科学家。1803年提出原子论：物质由不可分割的原子组成，同类原子质量相同。他还编制了第一张原子量表。他是色盲患者——这个生理缺陷使他注意到了色盲现象，并第一个写了相关科学论文。",
  "lifeStoryEn": "Born in 1766 in England, Dalton was self-taught. He proposed his atomic theory in 1803 and compiled the first atomic weight table. He was colorblind and wrote the first scientific paper on the condition.",
  "keyContributions": [
    { "title": "近代原子论", "titleEn": "Atomic Theory", "year": 1803, "desc": "所有物质由不可分割的原子组成；同类元素的原子的质量和性质相同；化合物是不同原子的组合。这些原理将化学从模糊的定性描述转变为精确的定量科学。", "descEn": "All matter consists of indivisible atoms; atoms of the same element have identical mass; compounds are combinations of different atoms. Transformed chemistry into a quantitative science.", "type": "theory" }
  ],
  "aiReview": "道尔顿的原子论是化学史上标志性的转折点——它使化学家们第一次有了一个统一的框架来理解元素和化合物的组成。"
})

# ═══════════════════════════════════════════
# Qian Xuesen
# ═══════════════════════════════════════════
enrich('qian-xuesen', {
  "summary": "钱学森是中国航天事业的奠基人，在空气动力学、火箭技术和系统工程领域做出卓越贡献，被誉为中国航天之父。",
  "summaryEn": "Qian Xuesen founded China's space program, making outstanding contributions to aerodynamics, rocket technology, and systems engineering. Known as the father of Chinese aerospace.",
  "lifeStory": "钱学森1911年出生于上海。1935年赴美留学，师从冯·卡门，成为世界顶尖的空气动力学家。1955年历经艰难回到中国，领导创建了中国第一个火箭导弹研究机构，主持了'两弹一星'工程中的导弹和卫星部分。",
  "lifeStoryEn": "Born in 1911 in Shanghai, Qian studied under von Kármán in the US, becoming a top aerodynamics expert. He returned to China in 1955 after艰难 years, leading the rocket and missile programs.",
  "keyContributions": [
    { "title": "中国航天奠基", "titleEn": "Founding Chinese Space Program", "year": 1956, "desc": "领导创建了中国第一个火箭导弹研究院，主持研制了东风系列导弹和第一颗人造卫星。", "descEn": "Led the creation of China's first rocket research institute and oversaw the Dongfeng missiles and first satellite.", "type": "invention" }
  ],
  "aiReview": "钱学森的回国之路本身就是一段传奇——他被美国政府软禁五年才获准离开。"
})

# ═══════════════════════════════════════════
# Chen Jingrun
# ═══════════════════════════════════════════
enrich('chen-jingrun', {
  "summary": "陈景润证明了哥德巴赫猜想中的'1+2'（陈氏定理），是中国数学的传奇人物。",
  "summaryEn": "Chen proved '1+2' in the Goldbach Conjecture (Chen's Theorem), a legendary figure in Chinese mathematics.",
  "lifeStory": "陈景润1933年出生于福建福州。他因华罗庚的赏识进入中国科学院数学研究所。在艰苦条件下，他用传统的手算方式在哥德巴赫猜想上取得了世界领先的成果。1973年发表'1+2'证明，轰动国际数学界。",
  "lifeStoryEn": "Born in 1933 in Fuzhou, Chen was discovered by Hua Luogeng. Working with hand calculations under difficult conditions, he proved '1+2' in 1973, stunning the international math community.",
  "keyContributions": [
    { "title": "陈氏定理(1+2)", "titleEn": "Chen's Theorem", "year": 1973, "desc": "证明了每个充分大的偶数可以写为一个素数加一个不超过两个素数的乘积之和——哥德巴赫猜想研究的最佳成果。", "descEn": "Proved every sufficiently large even number is the sum of a prime and the product of at most two primes — the best result toward the Goldbach Conjecture.", "type": "theory" }
  ],
  "aiReview": "陈景润在文革期间极端艰苦的条件下用纸笔完成了令世界瞩目的数学工作——这本身就是中国科学精神的一个象征。"
})

# ═══════════════════════════════════════════
# Knuth
# ═══════════════════════════════════════════
enrich('knuth', {
  "summary": "高德纳（高纳德·克努特）是算法分析之父，其多卷巨著《计算机程序设计艺术》是计算机科学的经典。他还发明了TeX排版系统，改变了学术出版。",
  "summaryEn": "Knuth is the father of algorithm analysis. His 'Art of Computer Programming' is a CS classic. He also created the TeX typesetting system, transforming academic publishing.",
  "lifeStory": "高德纳1938年出生于美国威斯康星。1968年开始写作《计算机程序设计艺术》——原计划写一卷，最终扩充为多卷本。他因对算法分析的基础性贡献获1974年图灵奖。他还发明了TeX排版系统——因为不满意出版社的排版质量。他给自己设定了一个任务：完成了全部卷册之前，不再使用电子邮件。",
  "lifeStoryEn": "Born in 1938 in Wisconsin, Knuth began 'The Art of Computer Programming' in 1968, planned as one volume, now many. Won the 1974 Turing Award. Created TeX排版 because he disliked book排版 quality.",
  "keyContributions": [
    { "title": "《计算机程序设计艺术》", "titleEn": "The Art of Computer Programming", "year": 1968, "desc": "计算机算法领域最权威的经典著作，以其严谨的数学分析和优美的写作风格著称。", "descEn": "The most authoritative classic on algorithms, known for rigorous analysis and elegant writing.", "type": "work" },
    { "title": "TeX排版系统", "titleEn": "TeX", "year": 1978, "desc": "科学文献排版的事实标准，已使用超过40年，被无数数学家、物理学家和计算机科学家使用。", "descEn": "The de facto standard for scientific typesetting, used for over 40 years by mathematicians, physicists, and computer scientists worldwide.", "type": "invention" }
  ],
  "aiReview": "高德纳将计算机算法提升到了一门'艺术'的高度。他的TeX系统在免费且完美的情况下运行了40多年——这是软件工程的奇迹。"
})

# ═══════════════════════════════════════════
# Yao Qizhi
# ═══════════════════════════════════════════
enrich('yao-qizhi', {
  "summary": "姚期智是首位获得图灵奖的华裔计算机科学家，在计算理论、密码学和量子计算领域做出了开创性贡献。",
  "summaryEn": "Yao was the first Chinese-descendant winner of the Turing Award. He made pioneering contributions to computational theory, cryptography, and quantum computing.",
  "lifeStory": "姚期智1946年出生于上海，在台湾长大。在哈佛大学获物理学博士，后在伊利诺伊大学获计算机博士——跨学科的学术背景使他独具优势。1979年提出了通信复杂度理论，1993年在量子计算领域做出基础性工作。2000年获图灵奖。2004年全职回到清华大学任教。",
  "lifeStoryEn": "Born in 1946 in Shanghai, Yao earned PhDs in physics (Harvard) and CS (Illinois). He proposed communication complexity theory and contributed to quantum computing. Won the Turing Award in 2000. Returned to Tsinghua in 2004.",
  "keyContributions": [
    { "title": "通信复杂度理论", "titleEn": "Communication Complexity", "year": 1979, "desc": "提出了分布式计算中通信复杂度的理论框架，成为理论计算机科学的基础工具之一。", "descEn": "Proposed the theoretical framework for communication complexity in distributed computing.", "type": "theory" }
  ],
  "aiReview": "姚期智从物理学转向计算机科学，在两个领域都达到了顶级水平——这种跨界能力极为罕见。"
})

# ═══════════════════════════════════════════
# Li Feifei
# ═══════════════════════════════════════════
enrich('li-feifei', {
  "summary": "李飞飞创立了ImageNet数据集和挑战赛，推动了深度学习在计算机视觉领域的革命。",
  "summaryEn": "Li created the ImageNet dataset and challenge, which propelled the deep learning revolution in computer vision.",
  "lifeStory": "李飞飞1976年出生于北京。她在斯坦福大学获得博士学位并成为教授。2009年领导团队创建了ImageNet——包含超过1400万张标注图片。2012年ImageNet挑战赛上辛顿团队的深度卷积网络以压倒性优势夺冠，成为AI历史转折点。",
  "lifeStoryEn": "Born in 1976 in Beijing, Li earned her PhD from Stanford and became a professor there. She led the creation of ImageNet (14M+ labeled images) in 2009, which became the catalyst for the deep learning revolution.",
  "keyContributions": [
    { "title": "ImageNet", "titleEn": "ImageNet", "year": 2009, "desc": "大规模视觉数据集——1400万张标注图片，覆盖2万多个类别。ImageNet挑战赛成为深度学习算法竞争的标杆。", "descEn": "Large-scale visual dataset with 14M+ labeled images across 20,000+ categories. ImageNet challenges became the benchmark for deep learning algorithms.", "type": "invention" }
  ],
  "aiReview": "李飞飞的ImageNet不仅是数据集，更是推动AI领域从各自为战走向统一标准的关键动力。"
})

# ═══════════════════════════════════════════
# Nan Rendong
# ═══════════════════════════════════════════
enrich('nan-rendong', {
  "summary": "南仁东是中国天眼FAST项目的首席科学家和总工程师，领导建造了世界上最大的单口径射电望远镜。",
  "summaryEn": "Nan was the chief scientist of China's FAST project, building the world's largest single-dish radio telescope.",
  "lifeStory": "南仁东1945年出生于吉林。他1994年提出建设大型射电望远镜的构想，花费22年时间从选址、立项到建设全都亲力亲为。FAST于2016年建成，直径500米。南仁东在项目竣工一年后因肺癌去世。",
  "lifeStoryEn": "Born in 1945 in Jilin, Nan proposed the FAST telescope idea in 1994. He spent 22 years on site selection, funding, and construction. FAST (500m diameter) was completed in 2016. He died of lung cancer a year later.",
  "keyContributions": [
    { "title": "FAST天眼", "titleEn": "FAST Telescope", "year": 2016, "desc": "世界上最大的单口径射电望远镜，灵敏度是此前世界最大的阿雷西博望远镜的2.5倍。", "descEn": "World's largest single-dish radio telescope, 2.5x more sensitive than the previous record-holder Arecibo.", "type": "invention" }
  ],
  "aiReview": "南仁东用22年将FAST从一纸蓝图变为世界级科学设施——这种一生只做一件事的执着令人敬佩。"
})

# ═══════════════════════════════════════════
# Hua Tuo
# ═══════════════════════════════════════════
enrich('hua-tuo', {
  "summary": "华佗是中国古代最著名的外科医生，发明了麻沸散（最早的麻醉剂之一），被尊为外科鼻祖。",
  "summaryEn": "Hua Tuo was ancient China's most famous surgeon. He invented Mafeisan (one of the earliest anesthetics) and is revered as the father of Chinese surgery.",
  "lifeStory": "华佗约145年出生于东汉沛国谯县（今安徽亳州）。他通晓内、外、妇、儿、针灸各科，尤以外科著称。他发明了麻沸散用于外科手术——比西方使用麻醉剂早了1600多年。他还创编了五禽戏健身操。据传曹操因头风病召他医治，华佗建议开颅手术，曹操怀疑他谋害自己，将其下狱处死。华佗的医书也在狱中被焚毁——这是中国医学史上的重大损失。",
  "lifeStoryEn": "Born around 145 AD in Bozhou, Hua Tuo was master of all medical fields, especially surgery. He invented an anesthetic (Mafeisan) 1,600 years before the West. He was executed by Cao Cao and his medical texts were burned.",
  "keyContributions": [
    { "title": "麻沸散", "titleEn": "Mafeisan Anesthetic", "year": 200, "desc": "用曼陀罗花等草药配制的麻醉药剂，用于外科手术——世界最早的麻醉剂之一，比西方早1600多年。", "descEn": "Herbal anesthetic concocted from Datura flowers and other herbs, used in surgery — 1,600 years before Western anesthesia.", "type": "invention" }
  ],
  "aiReview": "华佗的悲剧在于他的超前——开颅手术的想法在1800年前太过激进，以至被当作谋杀的企图。"
})

# ═══════════════════════════════════════════
# Zhang Zhongjing
# ═══════════════════════════════════════════
enrich('zhang-zhongjing', {
  "summary": "张仲景的《伤寒杂病论》确立了辨证论治的中医临床原则，被尊为医圣。",
  "summaryEn": "Zhang Zhongjing's 'Treatise on Cold Damage' established the principle of syndrome differentiation in Chinese medicine. He is revered as the Medical Sage.",
  "lifeStory": "张仲景约150年出生于东汉南阳。曾任长沙太守，但他用自己的俸禄为百姓看病。他的家族在瘟疫中死亡惨重，激发了他研究医学的决心。他撰写的《伤寒杂病论》总结了汉代以前的医学成就，确立了'辨证施治'的原则。",
  "lifeStoryEn": "Born around 150 AD in Nanyang, Zhang served as a governor but used his salary to treat the poor. Losing family members to plague motivated his medical studies. His treatise established Chinese medicine's diagnostic principles.",
  "keyContributions": [
    { "title": "《伤寒杂病论》", "titleEn": "Treatise on Cold Damage", "year": 210, "desc": "确立了辨证论治原则，将中医从经验医疗提升到理论医学的高度。至今仍是中医必读经典。", "descEn": "Established syndrome differentiation treatment, elevating Chinese medicine from经验 medical to theoretical medicine. Still a必读 classic.", "type": "work" }
  ],
  "aiReview": "张仲景的辨证论治体系使中医成为第一个有完整理论体系的传统医学。"
})

# ═══════════════════════════════════════════
# Watson
# ═══════════════════════════════════════════
enrich('watson', {
  "summary": "沃森与克里克合作发现了DNA双螺旋结构，揭示了遗传信息的分子基础。1962年获诺贝尔生理学或医学奖。",
  "summaryEn": "Watson co-discovered the DNA double helix with Crick, revealing the molecular basis of genetic information. He won the 1962 Nobel Prize.",
  "lifeStory": "沃森1928年出生于芝加哥，15岁进入芝加哥大学，22岁获博士学位。他在哥本哈根从事病毒研究时受到启发转向遗传学。1951年加入剑桥大学卡文迪什实验室，在那里遇到了克里克。两人在1953年根据富兰克林的X射线衍射数据猜出了DNA的双螺旋结构。",
  "lifeStoryEn": "Born in 1928 in Chicago, Watson entered college at 15 and earned his PhD at 22. He met Crick at Cambridge's Cavendish Lab in 1951. In 1953, using Franklin's X-ray data, they deduced DNA's double helix structure.",
  "keyContributions": [
    { "title": "DNA双螺旋结构", "titleEn": "DNA Double Helix", "year": 1953, "desc": "与克里克共同发现DNA由两条互补的链反向平行缠绕成双螺旋，碱基配对(A-T、C-G)揭示了遗传信息如何精确复制。", "descEn": "With Crick, discovered DNA's double helix: two complementary strands anti-parallel, base-pairing reveals how genetic information replicates precisely.", "type": "discovery" }
  ],
  "aiReview": "DNA结构的发现标志着分子生物学的诞生。沃森的文字《双螺旋》生动记录了这段科学史中最著名的一次合作与竞争。"
})

# ═══════════════════════════════════════════
# Crick
# ═══════════════════════════════════════════
enrich('crick', {
  "summary": "克里克与沃森合作发现了DNA双螺旋结构，后转向神经科学研究意识的生物学基础。",
  "summaryEn": "Crick co-discovered the DNA double helix with Watson, later turning to neuroscience to study the biological basis of consciousness.",
  "lifeStory": "克里克1916年出生于英国北安普敦。他最初学物理，二战期间为海军设计水雷。战后受薛定谔《生命是什么》的影响转向生物学。1953年与沃森发现DNA结构。1960年代参与破解了遗传密码。1970年代转向认知神经科学，致力于研究意识的神经基础。",
  "lifeStoryEn": "Born in 1916 in England, Crick studied physics then biology after being inspired by Schrödinger's book. He co-discovered DNA with Watson in 1953, helped crack the genetic code in the 1960s, then turned to consciousness research.",
  "keyContributions": [
    { "title": "DNA双螺旋结构", "titleEn": "DNA Double Helix", "year": 1953, "desc": "与沃森共同发现DNA双螺旋结构，揭示了遗传信息存储和复制的分子机制。", "descEn": "With Watson, discovered the DNA double helix revealing the molecular mechanism of genetic information storage and replication.", "type": "discovery" }
  ],
  "aiReview": "克里克的独特之处在于他从物理学到生物学再到神经科学的跨界之旅——每次转向都开创新领域。"
})

# ═══════════════════════════════════════════
# Linnaeus
# ═══════════════════════════════════════════
enrich('linnaeus', {
  "summary": "林奈创立了生物分类学的双名法命名体系，将万物按界、纲、目、属、种分类，系统沿用至今。",
  "summaryEn": "Linnaeus created binomial nomenclature for classifying all life into kingdom, class, order, genus, species. The system is still used in biology today.",
  "lifeStory": "林奈1707年出生于瑞典。1735年出版《自然系统》，建立了等级分类体系。他的双名法（属名+种名）解决了物种命名混乱的问题。他派遣学生到世界各地采集标本。",
  "lifeStoryEn": "Born in 1707 in Sweden. His 1735 'Systema Naturae' established biological classification. Binomial nomenclature solved species naming chaos. He sent students worldwide to collect specimens.",
  "keyContributions": [
    { "title": "双名法分类系统", "titleEn": "Binomial Nomenclature", "year": 1735, "desc": "每个物种由两个拉丁词命名（如Homo sapiens），全球通用，彻底解决了物种命名的混乱。", "descEn": "Each species gets a two-part Latin name (e.g., Homo sapiens), universally used, solving species naming chaos.", "type": "theory" }
  ],
  "aiReview": "林奈的格言'上帝创造了万物，林奈安排了万物'——虽然自负，但他的分类体系确实奠定了现代生物学的语言基础。"
})

# ═══════════════════════════════════════════
# Boyle
# ═══════════════════════════════════════════
enrich('boyle', {
  "summary": "波义耳是现代化学的奠基人，提出了波义耳定律，将化学确立为独立学科。",
  "summaryEn": "Boyle was a founder of modern chemistry. He proposed Boyle's Law and established chemistry as an independent science.",
  "lifeStory": "波义耳1627年出生于爱尔兰一个贵族家庭。他在牛津大学建立了实验室，雇佣了年轻的胡克作为助手。1661年出版《怀疑派化学家》，将化学从炼金术中解放出来。1662年提出波义耳定律（PV=常数）。",
  "lifeStoryEn": "Born in 1627 in Ireland, Boyle established a lab at Oxford with Hooke as assistant. His 1661 'The Sceptical Chymist' freed chemistry from alchemy. Proposed Boyle's Law (PV=constant) in 1662.",
  "keyContributions": [
    { "title": "波义耳定律", "titleEn": "Boyle's Law", "year": 1662, "desc": "在恒温下，一定量气体的体积与压强成反比。这是第一个以化学家命名的物理定律。", "descEn": "At constant temperature, gas volume is inversely proportional to pressure. The first physical law named after a chemist.", "type": "theory" }
  ],
  "aiReview": "波义耳的最大贡献不在于某个具体的发现，而在于他改变了化学的研究方式——用定量实验代替炼金术的神秘传统。"
})

# ═══════════════════════════════════════════
# Nobel
# ═══════════════════════════════════════════
enrich('nobel', {
  "summary": "诺贝尔发明了炸药，设立了诺贝尔奖——科学界最崇高的奖项。",
  "summaryEn": "Nobel invented dynamite and established the Nobel Prize, the most prestigious awards in science.",
  "lifeStory": "诺贝尔1833年出生于瑞典斯德哥尔摩一个发明家家庭。他1867年发明了安全炸药——用硅藻土吸收硝化甘油，使其便于运输和使用。他拥有355项专利，建立了跨国工业帝国。他终身未娶。1895年立下遗嘱，用其巨额财富设立诺贝尔奖。",
  "lifeStoryEn": "Born in 1833 in Stockholm. He invented dynamite in 1867 by absorbing nitroglycerin in diatomaceous earth. Held 355 patents. Unmarried. His 1895 will used his fortune to establish the Nobel Prizes.",
  "keyContributions": [
    { "title": "炸药发明", "titleEn": "Dynamite", "year": 1867, "desc": "将硝化甘油吸附在硅藻土中制成安全炸药，使爆破工程变得安全可控。", "descEn": "Absorbed nitroglycerin in diatomaceous earth for safe handling, revolutionizing construction and mining.", "type": "invention" },
    { "title": "诺贝尔奖", "titleEn": "Nobel Prize", "year": 1895, "desc": "在他去世后将巨额财产用于奖励在物理、化学、生理或医学、文学和和平方面做出重大贡献的人。", "descEn": "His will created the world's most prestigious awards for contributions to physics, chemistry, medicine, literature, and peace.", "type": "invention" }
  ],
  "aiReview": "诺贝尔的故事充满了矛盾的复杂性：他发明的炸药被用于战争，而他设立的奖则表彰和平。他的遗嘱遭到亲属的强烈反对，但他最终改变了世界奖励科学的方式。"
})

# ═══════════════════════════════════════════
# Hou Debang
# ═══════════════════════════════════════════
enrich('hou-debang', {
  "summary": "侯德榜是中国近代化学工业的奠基人，发明了侯氏制碱法，打破了国外纯碱技术垄断。",
  "summaryEn": "Hou was the founder of modern China's chemical industry. His Hou Process for soda production broke foreign monopoly.",
  "lifeStory": "侯德榜1890年出生于福建福州。他赴美留学获哥伦比亚大学博士学位。侯氏制碱法（1941年）将制碱和化肥生产联合，大幅提高效率。他晚年将技术无偿公开。",
  "lifeStoryEn": "Born in 1890 in Fuzhou. He earned his PhD from Columbia. The 1941 Hou Process combined soda and fertilizer production. He公开d the technology freely.",
  "keyContributions": [
    { "title": "侯氏制碱法", "titleEn": "Hou Process", "year": 1941, "desc": "联合制碱工艺，同时生产纯碱和化肥，效率远超传统方法。", "descEn": "Combined soda and fertilizer production process, far more efficient than traditional methods.", "type": "invention" }
  ],
  "aiReview": "侯德榜掌握着当时世界领先的制碱技术却选择公开——这展现了中国科学家的爱国情怀和奉献精神。"
})

# ═══════════════════════════════════════════
# Deng Jiaxian
# ═══════════════════════════════════════════
enrich('deng-jiaxian', {
  "summary": "邓稼先领导了中国原子弹和氢弹的研制，是中国核武器之父。",
  "summaryEn": "Deng led the development of China's atomic and hydrogen bombs, the father of China's nuclear weapons.",
  "lifeStory": "邓稼先1924年出生于安徽怀宁。他赴美留学获普渡大学博士学位后立即回国。1958年起隐姓埋名28年领导核武器研制。1979年在一次空投试验中受严重辐射——1986年因癌症去世。",
  "lifeStoryEn": "Born in 1924 in Anhui, Deng earned his PhD from Purdue and returned immediately to China. From 1958 he led nuclear weapons development incognito for 28 years. He died of cancer in 1986 due to radiation exposure.",
  "keyContributions": [
    { "title": "中国原子弹与氢弹", "titleEn": "Atomic & Hydrogen Bombs", "year": 1967, "desc": "1964年第一颗原子弹、1967年第一颗氢弹爆炸成功——从原子弹到氢弹仅用2年8个月，速度世界第一。", "descEn": "First atomic bomb 1964, first hydrogen bomb 1967 — only 2 years 8 months between them, the fastest in the world.", "type": "invention" }
  ],
  "aiReview": "邓稼先隐姓埋名28年——在科学家中，他的牺牲和奉献精神堪称极致。"
})

# ═══════════════════════════════════════════
# Wang Xuan
# ═══════════════════════════════════════════
enrich('wang-xuan', {
  "summary": "王选发明了汉字激光照排技术，使中国印刷业告别了铅与火的时代，被誉为当代毕昇。",
  "summaryEn": "Wang invented Chinese laser typesetting, liberating China's printing industry from the age of lead. Known as the modern Bi Sheng.",
  "lifeStory": "王选1937年出生于上海。他在1970年代开始研究汉字信息处理技术。他独创了汉字字形信息压缩技术，解决了汉字进入计算机的难题。1980年代他发明的激光照排系统在全国推广，中国印刷业从此告别了铅字排版。",
  "lifeStoryEn": "Born in 1937 in Shanghai. In the 1970s he pioneered Chinese character information processing. His unique compression technology enabled Chinese characters in digital排版. His laser typesetting system transformed China's printing industry.",
  "keyContributions": [
    { "title": "汉字激光照排", "titleEn": "Chinese Laser Typesetting", "year": 1980, "desc": "发明了汉字字形压缩和还原技术，使计算机能够高效处理汉字，实现了中国印刷技术的革命。", "descEn": "Invented Chinese character compression and restoration, enabling efficient computer processing of Chinese characters.", "type": "invention" }
  ],
  "aiReview": "王选解决了信息时代汉字数字化的核心难题——没有他的工作，中文互联网的普及可能会大大推迟。"
})

# ═══════════════════════════════════════════
# Zhong Nanshan
# ═══════════════════════════════════════════
enrich('zhong-nanshan', {
  "summary": "钟南山是中国呼吸病学专家，在SARS和新冠疫情中做出了重要贡献。",
  "summaryEn": "Zhong is China's leading respiratory disease specialist, making major contributions during SARS and COVID-19.",
  "lifeStory": "钟南山1936年出生于江苏南京的一个医学世家。2003年SARS疫情期间他67岁，坚持说真话、提出了关键防控策略。2020年新冠疫情时他84岁再次挂帅出征。",
  "lifeStoryEn": "Born in 1936 in Nanjing in a medical family. At 67 during SARS in 2003, he insisted on truth and proposed key strategies. At 84 during COVID-19 in 2020, he again led the expert team.",
  "keyContributions": [
    { "title": "疫情防控", "titleEn": "Epidemic Response", "year": 2020, "desc": "在SARS和新冠两次重大疫情中发挥了关键的专家领导作用，成为公共卫生的象征。", "descEn": "Played crucial leadership roles during both SARS and COVID-19, becoming a symbol of public health expertise.", "type": "discovery" }
  ],
  "aiReview": "钟南山之所以成为公众信任的符号，不仅因为他的医学水平，更因为他在关键时刻选择说真话的勇气。"
})

# ═══════════════════════════════════════════
# Tan Jiazhen
# ═══════════════════════════════════════════
enrich('tan-jiazhen', {
  "summary": "谈家桢是中国现代遗传学的奠基人，在果蝇遗传学方面做出了重要贡献。",
  "summaryEn": "Tan was a founder of modern genetics in China, making important contributions to Drosophila genetics.",
  "lifeStory": "谈家桢1909年出生于浙江宁波。他在加州理工学院师从摩尔根和杜布赞斯基学习遗传学。他回国后在艰苦条件下坚持遗传学研究，在抵制苏联李森科主义（否定基因理论）的斗争中坚持真理。",
  "lifeStoryEn": "Born in 1909 in Ningbo. He studied genetics at Caltech under Morgan and Dobzhansky. Returning to China, he persisted in genetic research despite Lysenkoism's campaign against genetics.",
  "keyContributions": [
    { "title": "中国遗传学奠基", "titleEn": "Chinese Genetics Foundation", "year": 1950, "desc": "在苏联李森科主义盛行时期坚持捍卫基因理论，培养了中国第一代遗传学家。", "descEn": "Defended gene theory during the Lysenkoist era in China, training the first generation of Chinese geneticists.", "type": "discovery" }
  ],
  "aiReview": "在1950年代苏联李森科主义的政治压力下，谈家桢坚持遗传学真理——这种科学良知值得铭记。"
})

print("Done! All 64 scientists enriched.")
enriched_count = sum(1 for s in data['scientists'] if 'lifeStory' in s)
print("With lifeStory:", enriched_count)

with open('D:/applications/AI_files/sciomap/data/scientists.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
