#! /usr/bin/python

try:
	fo = open("counter.txt","r+")
	str = fo.read()
	print str
	fo.close()
except IOError:
	myfile = open('counter.txt','w')
	myfile.write("1")
	myfile.close()


