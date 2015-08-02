#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import pprint

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

# 04. 元素記号
# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can." 
# という文を単語に分解し,1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字,
# それ以外の単語は先頭に2文字を取り出し,
# 取り出した文字列から単語の位置(先頭から何番目の単語か)への連想配列(辞書型もしくはマップ型)を作成せよ.
print "04."
text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = text.split(" ")
choises = 1, 5, 6, 7, 8, 9, 15, 16, 19
d = {}
for index,w in enumerate(words, start=1):
    if((index) in choises ):
        key = w[:1]
    else:
        key = w[:2]
    d[key] = index
pprint.pprint(d)

