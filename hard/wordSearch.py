import sys

def fun(inp,lst,line,leng,cnt,x,y):
    if cnt==leng:
        return True
    if x<0 or x>2 or y<0 or y>3 or lst[x][y]==1:
        return False
    if inp[x][y]!=line[cnt]:
        return False
    lst[x][y]=1
    if fun(inp,lst,line,leng,cnt+1,x,y-1):
        return True
    if fun(inp,lst,line,leng,cnt+1,x,y+1):
        return True
    if fun(inp,lst,line,leng,cnt+1,x-1,y):
        return True
    if fun(inp,lst,line,leng,cnt+1,x+1,y):
        return True
    return False

if __name__=='__main__':
    inp=[['a','b','c','e'],['s','f','c','s'],['a','d','e','e']]
    lst=[]
    res=[]
    dict={'a': [[0,0],[2,0]],'b':[[0,1]],'c':[[0,2],[1,2]],'d':[[2,1]],'e':[[0,3],[2,2],[2,3]],'f':[[1,1]],'s':[[1,0],[1,3]]}
    try:
        file=open(sys.argv[1],'r')
        for line in file:
            line = line.rstrip('\n').lower()
            res=dict[line[0]]
            for i in range(0,len(res)):
                lst=[]
                for j in range(0,3):
                    lst.append([0]*4)
                if fun(inp,lst,line,len(line),0,res[i][0],res[i][1]):
                    print 'True'
                    break
            else:
                print 'False'
    finally:
        file.close()
