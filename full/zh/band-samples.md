# zh: word samples per band, for the cutoff

Positions are places in the cleaned list (kept lemmas only). The developer chooses the cutoff from these words and the comparison across languages; this file decides nothing. Glosses are written by a model as a reading aid.

From the cleaned list as it loads (`snapshots/zh.json`, review rounds 1-11: every flagged lemma inside 40.5k reviewed by two reviewers and an adjudicator; the unflagged keeps screened across the window and again after each re-route; zh rulings and calls 1-25 in `full/zh/junk-review.md`). Corpus: **818,629,336 tokens** in 1,049,585 documents (HPLT v2 zho_Hans 818,281,416; Tatoeba cmn 347,920; Simplified only), counted through Honeyeater 8bc1817 with honeyeater_lemma_zh 1.6.4. Converged at 770,163,267 tokens; kept rank 40,000 = raw rank 44,747 (f 726, 0.89 per million).

Reading the words: a key after `#` is part of the lemma (a reading such as 行#xíng, a sense such as 花#spend, #comp a complement, #mw a measure word); names stay where they are learnable things (lemmatiser ruling R12: places, holidays, platforms, famous institutions and household-name companies), people drop; 成语 and other fixed expressions are words.

## Frequency per million tokens at kept ranks

| kept rank | lemma there | raw rank | f | per million |
|---:|---|---:|---:|---:|
| 1,000 | 消费者 | 1,015 | 109,037 | 133.19 |
| 5,000 | 皇后 | 5,115 | 16,082 | 19.65 |
| 10,000 | 工匠 | 10,396 | 6,155 | 7.52 |
| 15,000 | 停放 | 15,791 | 3,413 | 4.17 |
| 20,000 | 认罪 | 21,311 | 2,226 | 2.72 |
| 25,000 | 宜兴 | 26,923 | 1,589 | 1.94 |
| 30,000 | 自由度 | 32,658 | 1,197 | 1.46 |
| 35,000 | 靠垫 | 38,631 | 923 | 1.13 |
| 40,000 | 统治力 | 44,747 | 726 | 0.89 |

## Convergence (split-half disagreement)

The count stopped on the split-half rule (3 consecutive full-mix checkpoints with <= 5 % at the top 20k and <= 10 % at the top 50k). The last checkpoints (`convergence.md` has every one):

| tokens | per source | mix | 5k chg | 5k shift | f@5k | 5k split | 10k chg | 10k shift | f@10k | 10k split | 20k chg | 20k shift | f@20k | 20k split | 50k chg | 50k shift | f@50k | 50k split | stop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 496,046,878 | hplt-v2-zh 495,698,958, tatoeba-cmn 347,920 | full | 0.5% | 13 | 9,881 | 5.0% | 0.6% | 27 | 3,886 | 5.6% | 0.6% | 61 | 1,469 | 6.2% | 0.9% | 188 | 366 | 7.6% | 0/3 |
| 554,868,685 | hplt-v2-zh 554,520,765, tatoeba-cmn 347,920 | full | 0.7% | 17 | 11,027 | 4.1% | 0.8% | 36 | 4,355 | 4.5% | 0.9% | 82 | 1,642 | 5.2% | 1.1% | 249 | 410 | 6.8% | 0/3 |
| 637,016,180 | hplt-v2-zh 636,668,260, tatoeba-cmn 347,920 | full | 0.8% | 23 | 12,658 | 4.2% | 0.9% | 41 | 4,975 | 4.3% | 0.9% | 88 | 1,879 | 5.0% | 1.3% | 263 | 470 | 6.4% | 1/3 |
| 669,911,930 | hplt-v2-zh 669,564,010, tatoeba-cmn 347,920 | full | 0.3% | 9 | 13,333 | 3.8% | 0.4% | 19 | 5,223 | 4.2% | 0.4% | 40 | 1,976 | 4.7% | 0.6% | 125 | 495 | 6.3% | 2/3 |
| 770,163,267 | hplt-v2-zh 769,815,347, tatoeba-cmn 347,920 | full | 1.0% | 28 | 15,447 | 3.7% | 0.9% | 56 | 6,027 | 4.1% | 1.1% | 115 | 2,280 | 4.7% | 1.3% | 305 | 569 | 5.9% | 3/3 |

## Band 0-10,000: 25 random words

| position | word | POS | frequency | gloss (model-written) |
|---:|---|---|---:|---|
| 246 | 网站 | NOUN | 389,584 | website |
| 687 | 卖 | VERB | 159,077 | to sell |
| 1,035 | 立刻 | ADV | 105,032 | immediately |
| 1,486 | 贷款 | NOUN | 72,256 | loan |
| 1,543 | 旁边 | NOUN | 69,172 | beside; side |
| 2,324 | 家人 | NOUN | 43,140 |  |
| 2,581 | 猜 | VERB | 37,923 |  |
| 3,026 | 销量 | NOUN | 31,015 |  |
| 3,051 | 低头 | VERB | 30,718 |  |
| 3,112 | 天地 | ADJ | 29,969 |  |
| 4,971 | 计 | VERB | 16,241 |  |
| 6,491 | 耽误 | VERB | 11,200 |  |
| 7,317 | 占有 | VERB | 9,488 |  |
| 7,403 | 唇 | VERB | 9,320 |  |
| 7,412 | 产业化 | NOUN | 9,293 |  |
| 7,422 | 亲眼 | ADV | 9,282 |  |
| 7,630 | 明日 | NOUN | 8,949 |  |
| 7,795 | 克制 | VERB | 8,721 |  |
| 8,321 | 进门 | VERB | 7,954 |  |
| 8,388 | 触摸 | VERB | 7,878 |  |
| 8,657 | 富贵 | NOUN | 7,540 |  |
| 8,826 | 上限 | NOUN | 7,363 |  |
| 9,172 | 新华网 | NOUN | 6,962 |  |
| 9,624 | 火光 | NOUN | 6,498 |  |
| 9,756 | 电影院 | NOUN | 6,372 |  |

## Band 10,000-20,000: 25 random words

| position | word | POS | frequency | gloss (model-written) |
|---:|---|---|---:|---|
| 10,076 | 不朽 | NOUN | 6,097 |  |
| 10,493 | 削减 | VERB | 5,768 |  |
| 10,585 | 办公楼 | NOUN | 5,684 |  |
| 10,976 | 误解 | NOUN | 5,386 |  |
| 11,364 | 巧合 | NOUN | 5,129 |  |
| 11,393 | 物种 | NOUN | 5,110 |  |
| 13,117 | 健身房 | NOUN | 4,153 |  |
| 13,201 | 祭坛 | NOUN | 4,115 |  |
| 13,763 | 穷人 | NOUN | 3,875 |  |
| 13,829 | 政法委 | NOUN | 3,846 |  |
| 13,964 | 把头 | PROPN | 3,794 |  |
| 14,162 | 射程 | NOUN | 3,715 |  |
| 14,558 | 行者 | NOUN | 3,568 |  |
| 14,820 | 紧迫 | ADJ | 3,480 |  |
| 15,166 | 真挚 | ADJ | 3,357 |  |
| 15,346 | 友善 | VERB | 3,296 |  |
| 16,665 | 宣誓 | NOUN | 2,910 |  |
| 17,218 | 蝎子 | NOUN | 2,774 |  |
| 17,493 | 劲儿 | NOUN | 2,712 |  |
| 17,602 | 家家 | NOUN | 2,684 |  |
| 18,189 | 毫不留情 | VERB | 2,564 |  |
| 18,506 | 马虎 | PROPN | 2,505 |  |
| 19,032 | 参赛者 | NOUN | 2,399 |  |
| 19,683 | 讲道 | VERB | 2,281 |  |
| 19,825 | 方阵 | NOUN | 2,256 |  |

## Band 20,000-25,000: 25 random words

| position | word | POS | frequency | gloss (model-written) |
|---:|---|---|---:|---|
| 20,005 | 水污染 | NOUN | 2,225 | water pollution |
| 20,139 | 受害人 | NOUN | 2,205 |  |
| 20,244 | 药学 | PROPN | 2,188 |  |
| 20,429 | 时至今日 | NOUN | 2,157 |  |
| 20,548 | 法律效力 | NOUN | 2,135 |  |
| 20,576 | 不息 | ADJ | 2,129 |  |
| 20,599 | 摧残 | NOUN | 2,125 |  |
| 20,884 | 一段距离 | PROPN | 2,080 | a stretch of distance |
| 20,885 | 双翼 | NOUN | 2,080 |  |
| 21,627 | 亳州 | VERB | 1,977 |  |
| 21,719 | 插嘴 | VERB | 1,965 |  |
| 21,750 | 水力 | NOUN | 1,961 |  |
| 22,211 | 总动员 | NOUN | 1,901 |  |
| 22,368 | 成套设备 | PROPN | 1,881 |  |
| 22,384 | 闷热 | NOUN | 1,879 |  |
| 22,760 | 押注 | VERB | 1,835 |  |
| 23,076 | 柿子 | PROPN | 1,797 |  |
| 23,167 | 广告词 | PROPN | 1,786 |  |
| 23,256 | 西北部 | NOUN | 1,777 |  |
| 23,281 | 获救 | VERB | 1,774 |  |
| 23,439 | 牲畜 | NOUN | 1,754 |  |
| 23,851 | 丧生 | VERB | 1,704 |  |
| 24,202 | 战斧 | NOUN | 1,669 |  |
| 24,614 | 成婚 | VERB | 1,629 |  |
| 24,639 | 斑马 | NOUN | 1,626 |  |

## Band 25,000-30,000: 25 random words

| position | word | POS | frequency | gloss (model-written) |
|---:|---|---|---:|---|
| 25,090 | 父王 | PROPN | 1,581 |  |
| 25,125 | 楼阁 | ADJ | 1,578 |  |
| 25,491 | 避讳 | VERB | 1,543 |  |
| 25,714 | 黄芪 | PROPN | 1,524 |  |
| 25,828 | 楼梯口 | NOUN | 1,514 |  |
| 25,955 | 香草 | NOUN | 1,500 |  |
| 25,967 | 冷却液 | ADJ | 1,498 |  |
| 26,073 | 雷声 | ADJ | 1,490 |  |
| 26,103 | 助长 | VERB | 1,486 |  |
| 26,456 | 幡 | VERB | 1,456 |  |
| 26,544 | 客户群 | NOUN | 1,449 |  |
| 26,563 | 进站 | VERB | 1,448 |  |
| 27,019 | 本心 | NOUN | 1,410 |  |
| 27,550 | 醇厚 | NOUN | 1,365 |  |
| 27,725 | 唇部 | VERB | 1,350 |  |
| 28,144 | 灵犀 | VERB | 1,318 |  |
| 28,235 | 慰藉 | NOUN | 1,312 |  |
| 28,360 | 复赛 | VERB | 1,303 |  |
| 28,435 | 剑刃 | NOUN | 1,298 |  |
| 28,447 | 传承者 | NOUN | 1,297 |  |
| 28,666 | 外遇 | NOUN | 1,282 |  |
| 28,809 | 乡长 | PROPN | 1,272 |  |
| 28,989 | 近卫 | NOUN | 1,260 |  |
| 29,169 | 雅观 | NOUN | 1,249 |  |
| 29,582 | 期许 | NOUN | 1,222 |  |

## Band 30,000-35,000: 25 random words

| position | word | POS | frequency | gloss (model-written) |
|---:|---|---|---:|---|
| 30,004 | 主会场 | NOUN | 1,196 |  |
| 30,079 | 定压 | NOUN | 1,192 |  |
| 30,161 | 电子秤 | NOUN | 1,186 |  |
| 30,345 | 堆放 | NOUN | 1,174 |  |
| 30,602 | 油锅 | NOUN | 1,157 |  |
| 30,609 | 飘浮 | NOUN | 1,157 |  |
| 30,739 | 寨主 | NOUN | 1,149 |  |
| 30,822 | 紧急状态 | NOUN | 1,143 |  |
| 31,199 | 耗子 | ADJ | 1,121 |  |
| 31,535 | 亲眼所见 | PROPN | 1,101 |  |
| 31,727 | 无脑 | ADJ | 1,090 |  |
| 31,744 | 扫帚 | NOUN | 1,089 |  |
| 31,747 | 白烟 | NOUN | 1,089 |  |
| 32,116 | 错题 | NOUN | 1,067 |  |
| 32,211 | 非典 | ADJ | 1,062 |  |
| 32,428 | 网罗 | NOUN | 1,050 |  |
| 32,492 | 异步 | NOUN | 1,046 |  |
| 32,695 | 大中城市 | NOUN | 1,036 |  |
| 33,164 | 埃塞俄比亚 | PROPN | 1,010 |  |
| 33,230 | 幼时 | NOUN | 1,007 |  |
| 33,618 | 揽住 | VERB | 987 |  |
| 34,727 | 眼熟 | ADJ | 935 |  |
| 34,856 | 万山 | NOUN | 928 |  |
| 34,932 | 发紫 | VERB | 925 |  |
| 35,000 | 靠垫 | VERB | 923 | cushion |

## Band 35,000-40,000: 25 random words

| position | word | POS | frequency | gloss (model-written) |
|---:|---|---|---:|---|
| 35,128 | 超级计算机 | NOUN | 916 |  |
| 36,043 | 院方 | ADV | 877 |  |
| 36,112 | 亲力亲为 | ADJ | 873 |  |
| 36,263 | 空行 | NOUN | 867 |  |
| 36,299 | 关岛 | NOUN | 865 |  |
| 36,498 | 探员 | NOUN | 857 |  |
| 36,555 | 醉汉 | NOUN | 855 |  |
| 36,611 | 总汇 | NOUN | 852 |  |
| 36,710 | 分中心 | NOUN | 848 |  |
| 36,871 | 补考 | NOUN | 842 |  |
| 36,991 | 南方日报 | PROPN | 836 |  |
| 37,044 | 背#dìfang | NOUN | 834 |  |
| 37,547 | 配资 | VERB | 813 |  |
| 38,021 | 享有盛誉 | ADJ | 794 |  |
| 38,045 | 血花 | NOUN | 794 |  |
| 38,163 | 润肤 | NOUN | 789 |  |
| 38,181 | 基建投资 | NOUN | 788 |  |
| 38,713 | 正东 | NOUN | 770 |  |
| 38,953 | 乒乓 | NOUN | 761 |  |
| 38,963 | 展映 | VERB | 761 |  |
| 39,538 | 信众 | NOUN | 741 |  |
| 39,707 | 明末 | NOUN | 736 |  |
| 39,774 | 桀骜 | NOUN | 734 |  |
| 39,811 | 上证综指 | PROPN | 732 |  |
| 39,926 | 买账 | VERB | 728 |  |

## Band 40,000-45,000: 25 random words

| position | word | POS | frequency | gloss (model-written) |
|---:|---|---|---:|---|
| 40,318 | 试镜 | VERB | 717 |  |
| 40,389 | 暂扣 | ADV | 714 |  |
| 40,564 | 狂犬 | NOUN | 709 |  |
| 40,608 | 栾 | VERB | 708 |  |
| 40,644 | 富庶 | NOUN | 707 |  |
| 40,851 | 思明 | NOUN | 701 |  |
| 40,894 | 无措 | NOUN | 700 |  |
| 41,036 | 山涧 | PROPN | 696 |  |
| 41,438 | 药片 | NOUN | 686 |  |
| 41,872 | 地市级 | ADJ | 675 |  |
| 41,954 | 云团 | NOUN | 673 |  |
| 42,091 | 厦大 | NOUN | 670 |  |
| 42,106 | 深潭 | NOUN | 670 |  |
| 42,296 | 点金 | NOUN | 666 |  |
| 42,404 | 能自拔 | ADJ | 664 |  |
| 43,209 | 神户 | ADJ | 646 |  |
| 43,448 | 宇辰 | NOUN | 641 | Yuchen (given name) |
| 43,453 | 悬崖峭壁 | NOUN | 641 |  |
| 43,927 | 意指 | NOUN | 630 |  |
| 44,023 | 起跑 | VERB | 628 |  |
| 44,198 | 新词 | NOUN | 624 |  |
| 44,261 | 禁闭 | ADJ | 623 |  |
| 44,583 | 矿业权 | NOUN | 616 |  |
| 44,887 | 氢能 | NOUN | 610 |  |
| 44,945 | 榆树 | NOUN | 609 |  |

## Just above the cut (40,000): the last 60 words

| position | word | POS | frequency | gloss (model-written) |
|---:|---|---|---:|---|
| 39,941 | 献殷勤 | NOUN | 728 | curry favor; be attentive |
| 39,942 | 生存率 | PROPN | 728 | survival rate |
| 39,943 | 电气化 | NOUN | 728 | electrification |
| 39,944 | 秃 | VERB | 728 | bald |
| 39,945 | 租给 | VERB | 728 | rent to |
| 39,946 | 结膜炎 | NOUN | 728 | conjunctivitis |
| 39,947 | 老实人 | NOUN | 728 | honest person |
| 39,948 | 胖乎乎 | NOUN | 728 | plump; chubby |
| 39,949 | 西塘 | NOUN | 728 | Xitang (water town, Zhejiang) |
| 39,950 | 郡守 | NOUN | 728 | commandery governor |
| 39,951 | 阡陌 | NOUN | 728 | field paths |
| 39,952 | 领头人 | NOUN | 728 | leader |
| 39,953 | 高个子 | PROPN | 728 | tall person |
| 39,954 | 齐整 | NOUN | 728 | neat; tidy |
| 39,955 | 专利产品 | VERB | 727 | patented product |
| 39,956 | 举枪 | NOUN | 727 | to raise a gun |
| 39,957 | 乘务 | VERB | 727 | transport crew service |
| 39,958 | 传译 | ADJ | 727 | interpret; interpreting |
| 39,959 | 俯卧撑 | NOUN | 727 | push-up |
| 39,960 | 入神 | VERB | 727 | entranced; spellbound |
| 39,961 | 全面性 | PROPN | 727 | comprehensiveness |
| 39,962 | 出人头地 | VERB | 727 | stand out; get ahead |
| 39,963 | 办理手续 | NOUN | 727 | go through formalities |
| 39,964 | 天秤 | NOUN | 727 | balance scale; Libra |
| 39,965 | 实至名归 | NOUN | 727 | fame matches merit |
| 39,966 | 差遣 | NOUN | 727 | dispatch; send on errand |
| 39,967 | 广告片 | PROPN | 727 | commercial; ad film |
| 39,968 | 弃婴 | ADJ | 727 | abandoned baby |
| 39,969 | 必选 | NOUN | 727 | mandatory option |
| 39,970 | 志气 | NOUN | 727 | ambition; aspiration |
| 39,971 | 总费用 | NOUN | 727 | total cost |
| 39,972 | 拖住 | VERB | 727 | hold back; tie down |
| 39,973 | 挥之不去 | NOUN | 727 | linger; hard to shake |
| 39,974 | 掉线 | NOUN | 727 | be disconnected |
| 39,975 | 无所顾忌 | NOUN | 727 | without scruples |
| 39,976 | 时尚界 | NOUN | 727 | fashion world |
| 39,977 | 旺铺 | NOUN | 727 | prosperous shop |
| 39,978 | 活塞杆 | NOUN | 727 | piston rod |
| 39,979 | 爱河 | NOUN | 727 | river of love |
| 39,980 | 甘南 | VERB | 727 | Gannan (Gansu prefecture) |
| 39,981 | 男青年 | NOUN | 727 | young man |
| 39,982 | 研报 | NOUN | 727 | research report |
| 39,983 | 红头 | NOUN | 727 | red head; red-headed |
| 39,984 | 队医 | NOUN | 727 | team doctor |
| 39,985 | 雏鹰 | NOUN | 727 | eaglet; young eagle |
| 39,986 | 体系结构 | NOUN | 726 | architecture; system structure |
| 39,987 | 公尺 | NOUN | 726 | meter |
| 39,988 | 冰点 | NOUN | 726 | freezing point |
| 39,989 | 单片 | ADJ | 726 | single-chip; single-piece |
| 39,990 | 因应 | VERB | 726 | respond to; adapt to |
| 39,991 | 多才多艺 | NOUN | 726 | versatile; multitalented |
| 39,992 | 尾款 | NOUN | 726 | final payment |
| 39,993 | 布展 | NOUN | 726 | set up an exhibition |
| 39,994 | 引智 | VERB | 726 | attract intellectual talent |
| 39,995 | 擦身而过 | VERB | 726 | brush past |
| 39,996 | 文理学院 | NOUN | 726 | liberal arts college |
| 39,997 | 机载 | ADJ | 726 | airborne |
| 39,998 | 没法子 | ADJ | 726 | no way; helpless |
| 39,999 | 系统优化 | NOUN | 726 | system optimization |
| 40,000 | 统治力 | NOUN | 726 | dominance; ruling power |

## What a cut at 45,000 adds: 25 random words of 5,000

| position | word | POS | frequency | gloss (model-written) |
|---:|---|---|---:|---|
| 40,136 | 排污泵 | NOUN | 722 |  |
| 40,382 | 傲骨 | NOUN | 714 |  |
| 40,496 | 西洋参 | NOUN | 711 |  |
| 40,567 | 硫化物 | NOUN | 709 |  |
| 40,756 | 盖伊 | NOUN | 704 |  |
| 41,078 | 头名 | VERB | 695 |  |
| 41,134 | 称心如意 | ADJ | 694 |  |
| 41,150 | 各项任务 | NOUN | 693 |  |
| 41,444 | 银联卡 | NOUN | 686 |  |
| 41,671 | 次元 | NOUN | 680 |  |
| 41,740 | 四射 | NOUN | 678 |  |
| 42,041 | 占有欲 | PROPN | 671 |  |
| 42,206 | 育肥 | ADJ | 668 |  |
| 42,310 | 阿雅 | VERB | 666 |  |
| 42,712 | 昔时 | NOUN | 656 |  |
| 42,967 | 生意人 | NOUN | 651 |  |
| 43,022 | 九阴真经 | PROPN | 649 |  |
| 43,371 | 齐鸣 | VERB | 643 |  |
| 43,652 | 万贯 | NOUN | 636 |  |
| 43,690 | 莫小 | NOUN | 636 |  |
| 44,276 | 雨棚 | NOUN | 623 |  |
| 44,350 | 珍珠棉 | PROPN | 621 |  |
| 44,688 | 酒坛 | NOUN | 614 |  |
| 44,788 | 裆 | NOUN | 612 |  |
| 44,833 | 苔 | VERB | 611 |  |

## The same positions in the loaded es, de and ja lists

Five consecutive entries at each kept position, from the snapshots Honeyeater loads (`reference/lemmas/<lang>.json`; positions are entry order). Entries near 40,000 in those snapshots include the learnable names their builds appended after the cut.

| position | zh | es | de | ja |
|---:|---|---|---|---|
| 1,000 | 消费者 股 商品 结合 欢迎 | dólar vacacional subir hacer clic en algo vivienda | schwierig Regierung wohnen Zug ruhig | エロ 残念 事件 開く#ひらく 感想 |
| 5,000 | 皇后 耳边 过后 复合 毫不 | membrana nublado acogida curación abrazar | Beleg Migrant Roulette Suchwort Prävention | 世帯 フェラチオ 予感 防災 古代 |
| 10,000 | 工匠 长长 自理 顾忌 庆典 | colorrectal aprovecharse pedalear vástago riviera maya | skurril Gesundheitsförderung Manga Stromnetz Vokabel | 象徴する ランドセル 見所 バル 優位 |
| 20,000 | 认罪 辅佐 驰骋 含蓄 服务平台 | dolorosamente doloso ecocardiograma elusión hospedero | Tierfreund Vorwarnung Waffenstillstand aufklappen belebend | 墜落 定期券 忠告 某所 英語圏 |
| 30,000 | 自由度 苗圃 针头 锅底 主会场 | grafitero hidrolavadora hipersónico homogenización intersecar | Audio-CD Auftragswert Branchenlösung Darmspiegelung Datacenter | 滅入る 球速 生息地 絶縁する 耽る |
| 35,000 | 靠垫 饲喂 骗钱 佩带 土层 | arredrar asmr bajura cegamiento chalazión | Ukraine-Konflikt Ulcus Vortritt Wasserwacht Wochenplan | 調色 近傍 雌雄 ぶんぶん ほど良い |
| 38,000 | 太假 学院派 实业公司 实弹 市场供应 | miniprograma mondongo monoinsaturada montonero multiaxial | Rumänisch Schuber Schulbibliothek Selbstachtung Shrimp | 罷免 荒稼ぎ 落し物 蛮行 語感 |
| 39,000 | 登峰造极 筹谋 综合执法 美育 联席 | actualizarse afrobeat agroglifo amigote ampuloso | piepen rappen schreiend trockentupfen unkalkulierbar | 練り 被写界深度 軋む 道交法 非凡 |

| list | tokens | f at entry 39,000 | per million |
|---|---:|---:|---:|
| zh | 818,629,336 | 760 | 0.93 |
| es | 1,382,684,047 | 72 | 0.05 |
| de | 451,548,754 | 259 | 0.57 |
| ja | 689,675,997 | 365 | 0.53 |

es counts ParaCrawl, whose frequencies fall off faster through the middle of the list (3.1 per million at entry 10,000 against de 4.8 and ja 6.2).
