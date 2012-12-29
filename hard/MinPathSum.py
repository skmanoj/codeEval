import sys

def fun(cnt,inp):
    lst=[]
    res=[]
    for i in range(0,cnt):
        res.append([sys.maxint]*(cnt+1))
        inp[i]=inp[i].rstrip('\n')
        lst.append([int(x) for x in inp[i].split(',')])
    res.append([sys.maxint]*(cnt+1))
    for i in range(1,cnt+1):
        for j in range(1,cnt+1):
            if i==1 and j==1:
                res[i][j]=lst[i-1][j-1]     
                continue
            res[i][j] = min(res[i][j-1],res[i-1][j])+lst[i-1][j-1]        
    print res[cnt][cnt]

if __name__=='__main__':
    try:
        file=open(sys.argv[1],'r')
        inp = file.readlines()
        i=0
        while i<len(inp):
            leng=int(inp[i].rstrip('\n'))
            fun(leng,inp[i+1:i+leng+1])
            i=i+leng+1
    finally:
        file.close()
