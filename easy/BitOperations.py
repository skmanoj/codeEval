import sys

f=open(str(sys.argv[1]),"r")
for line in f.readlines():
	lst=[]
	lst= [int(p) for p in line.split(",")]
	a=(lst[0]>>(lst[1]-1)) & 1
	b=(lst[0]>>(lst[2]-1)) & 1
	if a==b:
		print "true"
	else:
		print "false"
