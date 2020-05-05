#!/usr/bin/env python

import re
import sys

for line in sys.stdin:
	line = line.split(',',1)
	#if (len(line)==2 and line[0]!=''):
		#if(len(line[0])==10):
	print ('%s,%s'%(line[0],len(line[1])))

	#print(line[0],line[1])

	   
	