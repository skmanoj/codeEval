import sys

f=open(str(sys.argv[1]),"r")
for line in f.readlines():
	x,n= [int(p) for p in line.split(",")]
	while n<=x:
		n+=n
	print n
