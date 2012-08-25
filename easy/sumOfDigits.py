import sys

f=open(str(sys.argv[1]),"r")
for line in f.readlines():	
	sum1=0
	for i in range(0,len(line)-1):
		sum1=sum1+(ord(line[i])-48)	
	print sum1
