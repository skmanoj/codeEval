import sys
 
 
def longest_lines(l, n):
    l.sort(key=lambda x: len(x) * -1)
    #print l
    return l[:n]
 
 
if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
 
    lines = [i.rstrip() for i in test_cases]
    print '\n'.join(longest_lines(lines[1:], int(lines[0])))
 
    test_cases.close()
