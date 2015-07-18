#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys

# 00. 文字列の逆順
# 文字列"stressed"の文字を逆に(末尾から先頭に向かって)並べた文字列を得よ.
print "00."
print "stressed"[::-1]

# 01. 「パタトクカシーー」
# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ.
print "01."
print u"パタトクカシーー"[1::2]

# 02. 「パトカー」+「タクシー」=「パタトクカシーー」
# 「パトカー」+「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ.
print "02."
for (p, t) in zip(u"パトカー", u"タクシー") :
    sys.stdout.write(p + t)
print ""

# 03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し,
# 各単語の(アルファベットの)文字数を先頭から出現順に並べたリストを作成せよ.
text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print "03."
for w in text.split(" ") :
    sys.stdout.write(str(len(w)))
print ""
