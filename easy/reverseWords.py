import sys
filename=sys.argv[1]
f=open(filename)
data=f.read()
f.close()

lines=data.split("\n")[:-1]
words=[i.split() for i in lines]
for i in words:
    i.reverse()
print "\n".join([" ".join(i) for i in words])
