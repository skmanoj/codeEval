import sys

def fib(n):
	a=0
	b=1
	for i in range(2,n+1):
		c=a+b
		a=b
		b=c
	return c				
		

f=open(str(sys.argv[1]),"r")
for line in f.readlines():
	n=int(line)
	print fib(n)
