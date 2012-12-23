import sys

def fun(lst):
    cl=[')',']','}']
    res=[]
    while lst: #runs till elements are present in list
        val = lst.pop()
        if val in cl:
            res.append(val)
            continue
        else:
            if not res:
                return 'False'
            tmp=res.pop()
            if (val=='(' and tmp==')') or (val=='{' and tmp=='}') or (val=='[' and tmp==']'):
                continue
            else:
                return 'False'
    if res:
        return 'False'
    return 'True'

if __name__=='__main__':
    try:
        file=open(sys.argv[1],'r')
        for line in file:
            line=line.rstrip('\n');
            print fun(list(line))
    finally:
        file.close() 
