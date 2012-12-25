import sys

def fun(n):
    count=0
    while n>=5:
        n=n-5
        count=count+1
    while n>=3:
        n=n-3
        count=count+1
    while n>=1:
        n=n-1
        count=count+1
    return count   

if __name__=='__main__':
    try:
        file=open(sys.argv[1],'r')
        for line in file:
            line=line.rstrip('\n')
            num=int(line)
            print fun(num)
    finally:
        file.close()    
