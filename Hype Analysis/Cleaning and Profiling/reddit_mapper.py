#!/usr/bin/env python

import re
import sys



for line in sys.stdin:
	line = re.sub(r'^$','',line)  #remove empty line
	line = re.sub('http\S+\s*','',line)  # to remove URL
	line = line.split(' ',2)
	if (len(line)==3 and line[0]!=''):  #to only select non-empty lines
		if(len(line[0])==10):           #Only select first date value
			print ('%s,%s'%(line[0],line[2])),
	#print(line[0],line[1])

	   
	