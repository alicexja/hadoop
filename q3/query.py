# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 01:05:06 2020

@author: dell
"""

# query for q3

import sys
def main(args):
    res = set()
    
    if len(args)==3 and ((args[1].lower()=="and") or (args[1].lower()=="or")):
        g1 = args[0]
        g2 = args[2]
        id1=set()
        id2=set()
        with open('genres','r') as f:
            for line in f:
                line = line.strip()
                genre,idlst = line.split('\t')
                if g1.lower()==genre.lower():
                    id1 =set(idlst.strip('][').split(','))
                if g2.lower()==genre.lower():
                    id2=set(idlst.strip('][').split(','))
                    
                if args[1].lower()=="or":
                    res = id1.union(id2)
                elif args[1].lower()=="and":
                    res = id1.intersection(id2)             
    elif len(args)==1:
        g=args[0]
        with open('genres','r') as f:
            for line in f:
                line = line.strip()
                genre,idlst = line.split('\t')
                if g.lower()==genre.lower():
                    res = set(idlst.strip('][').split(','))
    else:
        print("usage 1.Single genre\n")
        print("usage 2.genre 1 and genre 2\n")
        print("usage 3.genre 1 or genre 2\n")
        sys.exit()
    if len(res)!=0:
        print(res)
    else:
        print("There is no movie stisfy the condition")
        sys.exit()

if __name__ == "__main__":
    main(sys.argv[1:])
        
        
        
        