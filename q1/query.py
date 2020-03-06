# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 23:22:47 2020

@author: dell
"""

# query for q1
import sys

def main(args):
    n = 0
    c=""
    
    if len(args)==0:
        print ("usage:python query.py cityname")
        sys.exit()
    elif len(args)>1:
        for arg in args:
            c+=arg+" "
    else:
        c = args[0]
    c = c.strip()
    with open("cityinformation","r") as f:
        for line in f:
            city,count = line.split('\t',1)
            if c.lower()==city.lower():
                try:
                    count = int(count)
                except ValueError:
                    continue
                n = count
    if n>0:
        print("%s has %s Starbuck(s)" % (c,n))
    else:
        print("The number of Starbucks in %s is not recorded in the system" % c)

if __name__ == "__main__":
    main(sys.argv[1:])
                    
