#!/usr/bin/env python
import sys

(last_key, count_val) = (None, ' ')
for line in sys.stdin:
	(key, val) = line.strip().split(",",1)
	if last_key and last_key != key:
		print "%s,%s" % (last_key, count_val)
		(last_key, count_val) = (key, val)
	else:
		(last_key, count_val) = (key, val+count_val)
if last_key:
	print "%s,%s" % (last_key, count_val)
