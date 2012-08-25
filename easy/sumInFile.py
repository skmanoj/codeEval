import sys

f=open(str(sys.argv[1]),"r")
sum1=0
for line in f.readlines():	
	sum1+=int(line)
print sum1	
