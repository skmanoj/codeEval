import sys
f=open(str(sys.argv[1]),"r")
for line in f.readlines():
	line=line.rstrip("\n")
	lst=[]
	lst=line.split(" ")
	p=len(lst)-1
	val=int(lst[p])
	if val > p:
		continue
	print lst[len(lst)-1-val]
