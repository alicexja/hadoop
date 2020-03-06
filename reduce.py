# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 22:51:28 2020

@author: dell
"""

from operator import itemgetter
import sys
"""

current_word=None
current_count=0
word=None

for line in sys.stdin:
    line=line.strip()
    word,count=line.split('\t',1)
    try:
        count=int(count)
    except ValueError:
        continue
    if current_word == word:
        current_count+=count
    else:
        if current_word:
            print("%s\t%s" % (current_word,current_count))
        current_count = count
        current_word = word
if current_word == word:
    print("%s\t%s" % (current_word,current_count))
"""

d={}
for line in sys.stdin:
    line = line.strip()
    word,count = line.split('\t',1)
    try:
        count = int(count)
    except ValueError:
        continue
    if word in d:
        d[word]+=count
    else:
        d[word]=count
for k in d:
    print("%s\t%s" % (k,d[k]))