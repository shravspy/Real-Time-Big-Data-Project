#!/usr/bin/env python
import sys

(last_key, val) = (None,'')

for line in sys.stdin:
	print line
	key = line.split(',')[0]
	val1 = line.split(',')[1]
	if last_key and last_key != key:
		print "%s %s" % (last_key, val)
		(last_key, val) = (key, val1)
 	else:
 		(last_key, val) = (key, val1+val)
if last_key:
	print "%s\t%s" % (last_key, val)
	