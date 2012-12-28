import sys
 
def pascal(n):
    if n == 1:
        return [ [1] ]
    else:
        result = pascal(n-1)
        lastRow = result[-1]
        result.append( [ (a+b) for a,b in zip([0]+lastRow, lastRow+[0]) ] )
        return result
  
if __name__ == '__main__':
    file=open(sys.argv[1],'r')
    for line in file: 
        line=line.rstrip('\n')
        lst=pascal(int(line))
        lst = sum(lst,[])
        for i in range(0,len(lst)-1):
            print lst[i],
        print lst[len(lst)-1]    
