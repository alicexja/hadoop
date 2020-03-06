# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:01:08 2020

@author: dell
"""

import sys
from indexer import Indexer

def main(args):
    if len(args)==3:
        g1 = args[0].lower()
        g2 = args[2].lower()
        if args[1].lower() == "and":
            op="and"
        elif args[1].lower() == "or":
            op = "or"
    elif len(args)==1:
        op="u"
        g1=args[0].lower()
        g2=""
    else:
        print("usage 1.Single genre\n")
        print("usage 2.genre 1 and genre 2\n")
        print("usage 3.genre 1 or genre 2\n")
        sys.exit()
    res = list(Indexer(g1,g2,op))
    print(res)
        