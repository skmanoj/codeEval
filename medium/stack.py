import sys
f=open(str(sys.argv[1]),"r")
for line in f.readlines():
	line=line.rstrip("\n")
	lst=[]
	lst=line.split(" ")
	out=[]
	while lst:
		out.append(lst.pop())
		lst.pop()
	print " ".join(out)	
