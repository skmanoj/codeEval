import sys

f=open(str(sys.argv[1]),"r")
for line in f.readlines():
	lst=[]
	lst= [int(p) for p in line.split(",")]
	a=lst[0]
	b=lst[1]
	c=a/b
	print a-b*c

