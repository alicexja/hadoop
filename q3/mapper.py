# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 22:18:17 2020

@author: dell
"""

# q3 mapper

import csv
import sys
datfile = "movies.dat"
with open(datfile,newline='',encoding='ISO-8859-1') as file:
    csvreader = csv.reader((line.replace('::', '~') for line in file),delimiter='~')
    for row in csvreader:
        genres = row[2].split('|')
        if genres[0]!="":
            for g in genres:
                print("%s\t%s" % (g,row[1]))
        else:
            print("%s\t%s" % ("None",row[1]))
            

        