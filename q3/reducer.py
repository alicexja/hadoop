# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 22:43:42 2020

@author: dell
"""

import sys

d={}

for line in sys.stdin:
    line = line.strip()
    genre,movieid=line.split('\t')
    if genre in d:
        d[genre].append(movieid)
    else:
        d[genre]=[]
        d[genre].append(movieid)
with open('genres','w') as f:
    for k in d:
        f.write("%s\t%s\n" % (k,d[k]))
