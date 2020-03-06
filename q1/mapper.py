# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 20:23:38 2020

@author: dell
"""
# mapper

import csv

filename = "starbucks-locations-sort.csv"

with open(filename,newline='',encoding="ISO-8859-1") as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')
    next(csvreader)# skipping the first row
    for row in csvreader:
        print("%s\t%s" % (row[9].lower(),1))
