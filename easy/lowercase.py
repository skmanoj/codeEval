import sys

f=open(str(sys.argv[1]),"r")
for line in f.readlines():
	print line.lower()
