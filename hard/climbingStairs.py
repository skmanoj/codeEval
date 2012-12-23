import sys


def fun(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 2
    return fun(n-1)+fun(n-2)

if __name__=='__main__':
    file=open(sys.argv[1],'r')
    try:
        for line in file:
            lst=int(line.rstrip('\n'))
            print fun(lst)
    finally:
        file.close()
