#!/usr/bin/python

import sys
try:
	num = int(sys.argv[1])
	fo = open("counter.txt", "wb")
	fo.write(str(num+1));
	fo.close()
except:pass
