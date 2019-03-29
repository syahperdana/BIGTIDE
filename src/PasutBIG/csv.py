#!/usr/bin/python

"""
Comma Separated Values function
"""

import csv

def getsecondrow(filename):
  with open(filename, 'r') as f:
    for row, line in enumerate(f):
      if row == 1:
        secondrow = line.split(",")
        break
    return secondrow

def getlastrow(filename):
  with open(filename, 'r') as f:
    lastrow = None
    for lastrow in csv.reader(f): pass
    return lastrow

def savedb(filename):
	with open(filename) as csvfile:
		reader = csv.reader(csvfile)
		firstrow = next(reader)
	lastrow = getlastrow(filename)
	filerename = firstrow[0].replace('/', r'').replace(' ', r'Z').replace(':', r'') + "-" + lastrow[0].replace('/', r'').replace(' ', r'Z').replace(':', r'') + ".csv"
	return filerename

def savedbf(filename):
	secondrow = getsecondrow(filename)
	lastrow = getlastrow(filename)
	filerename = secondrow[0].replace('/', r'').replace(' ', r'Z').replace(':', r'') + "-" + lastrow[0].replace('/', r'').replace(' ', r'Z').replace(':', r'') + ".csv"
	return filerename
