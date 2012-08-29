import sys

s1=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
s2=["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
s3=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]

def out(n):
    c=n%10
    n/=10
    b=n%10
    a=n/10
    if a!=0:
        sys.stdout.write(s1[a]+"Hundred")
    if b==1:
        sys.stdout.write(s3[c])
    else:
        if b>=2:    
            sys.stdout.write(s2[b])
        if c!=0:
            sys.stdout.write(s1[c])

def solve(n):
    c=n%1000
    n/=1000
    b=n%1000
    a=n/1000
    if a!=0:
        out(a)
        sys.stdout.write("Million")	
    if b!=0:
        out(b)	    
        sys.stdout.write("Thousand")	  
    out(c)
    sys.stdout.write("Dollars")

if  __name__=='__main__':
    f=open(str(sys.argv[1]),"r")
    for line in f.readlines():
        line.rstrip("\n")
        n=int(line)
        solve(n)	
        print

