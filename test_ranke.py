# -*- coding: utf-8 -*-
import rake
import operator
from summa import keywords, summarizer

rake_obj = rake.Rake("SmartStopList.txt")

test_text = """Windsor, Conn. (September 6, 2017) Morris Group, Inc. of Windsor, Connecticut, one of the largest CNC machine tool distribution networks in North America, has been selected by Desktop Metal of Burlington, Massachusetts as a top tier, Diamond Partner supplier of its innovative metal 3D printing systems in 30 states extending from Maine to Florida to the Dakotas. With the addition of Desktop Metal’s Studio System™ to its existing lineup of CNC machine tools, Morris Group’s extensive distributor network provides an end-to-end suite of advanced solutions to manufacturers of precision metal parts. We are very pleased to represent Desktop Metal and excited to introduce this groundbreaking 3D printing technology to metal cutting manufacturers in our distribution area,” states Brad Morris, President and CEO of Morris Group.  “Our organization brings more than seventy-five years of manufacturing experience, knowledge and customer support to the table.The Studio System, which debuted in May, is the first office-friendly metal 3D printing system for rapid prototyping, and is 10 times less expensive than existing technology. The Studio System is a complete platform, including a printer, a debinder and a sintering furnace. It requires no hazardous powders, lasers or cutting tools to operate. Instead it uses Bound Metal Deposition (BMD), a proprietary process, to near net shape parts, similar to the safest and most widely-used 3D printing process for plastics, Fused Deposition Modeling (FDM). The Studio System printer features safe-to-handle, swappable media cartridges and quick release print heads for seamless material changes. It was designed for use with a variety of materials-- from steels and copper to superalloys like Inconel.We are excited to partner with Morris Group to bring our metal 3D printing solutions to new markets,” said Ric Fulop, CEO and co-founder of Desktop Metal. “Through this partnership, manufacturers can leverage the same trusted source to purchase and service the highly complementary technologies of CNC machine tools and metal additive manufacturing that together deliver the dimensional accuracy and speed needed to produce reliable, precision metal parts.”“We researched many different additive manufacturing technologies over the past several years and believe that Desktop Metal offers the best metal 3D printing tool for our customers’ needs. We look forward to introducing the Studio System and other Desktop Metal products to the market as they are developed,” adds Mr. Morris. All machine tool distributors owned by Morris Group currently offer the Studio System. Demo systems will be exhibited at several geographic locations throughout the Morris Group distribution network. Additionally, demo systems will be displayed at AMTS in Dayton, Ohio in Technical Equipment’s booth and at SOUTH-TEC in Greenville, South Carolina in Morris South’s booth.For more information or to reserve the Studio System, contact your local Morris Group distributor.  To locate a Morris Group distributor near you, visit www.morrisgroupinc.com/home/companies.About Desktop Metal Desktop Metal, Inc., based in Burlington, Massachusetts, is accelerating the transformation of manufacturing with end-to-end metal 3D printing solutions. Founded in 2015 by leaders in advanced manufacturing, metallurgy, and robotics, the company is addressing the unmet challenges of speed, cost, and quality to make metal 3D printing an essential tool for engineers and manufacturers around the world. Desktop Metal has raised a total of $212 million in financing, with the Series D marking the largest round ever for an additive manufacturing company. In 2017, the company was selected as one of the world’s 30 most promising Technology Pioneers by World Economic Forum, and was recently named to MIT Technology Review’s list of 50 Smartest Companies. For more information, visit www.desktopmetal.com.About Morris Group, Inc.Morris Group, Inc., one of North America’s largest machine tool supply networks, owns fifteen independently operated business units. It supplies CNC machine tools and related technology and services to manufacturers representing virtually every industry segment. Morris Group, Inc. is headquartered in Windsor, Connecticut, home of its founding company, The Robert E. Morris Company, which has served the manufacturing industry since 1941. For more information, visit www.morrisgroupinc.com."""
# test_text = "3D printing metal on a desktop FDM printer, exclusive interview with The Virtual Foundry founder : Is 2017 going to be the year for 3D printing metal? Recently 3D Printing Industry reported announcements from Markforged about their forthcoming Metal X 3D "
scores, keyword = rake_obj.run(test_text)

# print scores
sorted_score = sorted(scores.iteritems(), key = lambda asd: asd[1], reverse = True)
print "sorted_score"
print sorted_score
filter_n = 0.1

topn_words = [w[0] for w in sorted_score[:int((len(sorted_score) * filter_n))]]
botton_words = [w[0] for w in sorted_score[len(sorted_score) - int((len(sorted_score) * filter_n)):]]

# print topn_words, botton_words
print keyword
goal_word = []

for i in keyword:

    # if len([w for w in i[0].split(' ') if w in topn_words and w not in botton_words]) != 0:
    #     goal_word .append(i)
    words = i[0].split(' ')
    word_score = 0
    for w in words:
        if scores.has_key(w):
            word_score += scores[w]
    mean_score = word_score / len(words)

    goal_word.append((i[0], mean_score))

goal_word = sorted(goal_word, key = lambda asd: asd[1], reverse = True)
print goal_word
print "|str|score|"
print "|-------------|-------------|"
# for s in goal_word[:int((len(goal_word) * filter_n))]:
for s in goal_word:
    print "|" + s[0] + '|' + str(s[1]) + '|'

    # words = keywords.keywords(test_text).split('\n')
    # words = summarizer.summarize(test_text)
    # print words
    # print "|str|"
    # print "|-------------|"
    # for w in words:
    #     print "|" + w + '|'
