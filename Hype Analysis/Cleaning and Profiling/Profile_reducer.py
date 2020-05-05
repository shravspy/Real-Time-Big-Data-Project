#!/usr/bin/env python
import sys

max_date = '2017-01-01'
min_date = '2018-12-30'

#(last_key, max_val) = (None, -sys.maxint) 

for line in sys.stdin:
	(key, val) = line.strip().split(",")
	if key < min_date:
		min_date = key
	if key>max_date:
		max_date = key

print ('creation Date  Max_value: '+ min_date + 'Min_value ' + max_date)
