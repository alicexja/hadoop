# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 21:48:02 2020

@author: dell
"""

# part2 indexer
import csv
import sys

class Indexer(op,g1,g2):
    datfile = "movies.dat"
    d={} # keeps the genre
    with open(datfile,newline='',encoding='ISO-8859-1') as file:
        csvreader = csv.reader((line.replace('::', '~') for line in file),delimiter='~')
        for row in csvreader:
            genres = row[2].split('|')
            if genres[0]=="":
                if "none" in d.keys():
                    d["none"].append(row[0])
                else:
                    d["none"]=[]
                    d["none"].append(row[0])
            else:
                for g in genres:
                    if g in d.keys():
                        d[g.lower()].append(row[0])
                    else:
                        d[g.lower()]=[]
                        d[g.lower()].append(row[0])
    # now a dictionary is constructed.
    if op=="and":
        s1 = set(d[g1])
        s2 = set(d[g2])
        res = s1.intersection(s2)
    elif op=="or":
        s1=set(d[g1])
        s2=set(d[g2])
        res = s1.union(s2)
    else:
        #unary
        res = set(d[g1])
    return res
        

    