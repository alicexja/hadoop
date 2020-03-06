# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 22:50:26 2020

@author: dell
"""

# normal mapper
import sys

for line in sys.stdin:
    line=line.strip()
    words = line.split()
    for word in words:
        print("%s\t%s" % (word,1))