import sys
f=open(str(sys.argv[1]),"r")
for line in f.readlines():
	line=line.rstrip()
	n=int(line)
	cnt=0
	while n&(n-1)!=0:
		cnt+=1
		n=n&(n-1)
	print cnt+1	
