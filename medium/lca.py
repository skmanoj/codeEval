import sys

btree = {
            30: {
                8: {
                    3: None, 
                    20: {
                        10: None, 
                        29: None 
                    }
                },
                52: None
            }
        }

def bsearch(a, b, tree):
    for key in tree:
        if (a < key and key < b) or (b < key and key < a):
            return key
        elif tree[key]:
            return bsearch(a, b, tree[key])


with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        a, b = [int(s) for s in line.rstrip().split(" ")]
        print bsearch(a, b, btree)

