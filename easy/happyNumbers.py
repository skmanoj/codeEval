import sys

def happy(n):
    past = set()			
    while True:
        total = sum(int(i)**2 for i in str(n))
        if total == 1:
            return True
        if total in past:
            return False
        n = total
        past.add(total)

f=open(str(sys.argv[1]),"r")
for line in f.readlines():
	line=line.rstrip("\n") 
	if happy(line):
		print 1
	else:
		print 0	
