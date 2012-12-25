import sys

def fun(lst,x):
    no=len(lst)-(len(lst)%x)
    for i in range(0,no,x):
        lst[i:i+x]=reversed(lst[i:i+x]);
    s=[str(lst[x]) for x in range(0,len(lst))]
    print ','.join(s)
    

if __name__=='__main__':
    try:
        file=open(sys.argv[1],'r')
        for line in file:
            line=line.rstrip('\n');
            lst=line.split(';')
            num=int(lst[1])
            res=[int(x) for x in lst[0].split(',')]
            fun(res,num)
    finally:
        file.close()
