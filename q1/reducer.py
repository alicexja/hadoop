# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 20:45:16 2020

@author: dell
"""

# reducer
from operator import itemgetter
import sys

d = {}
for line in sys.stdin:
    line=line.strip()
    city,_ = line.split('\t')
    if city in d:
        d[city]+=1
    else:
        d[city]=1
with open("cityinformation","w") as f:
    for k in d:
        f.write("%s\t%s\n" % (k,d[k]))