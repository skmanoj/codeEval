import sys

if(__name__=="__main__"):
    filename=sys.argv[1]

    f=open(filename)
    data=f.read()
    f.close()

    lines=data.split("\n")[:-1]
    delimited=[i.split(',') for i in lines]
    positions=[i[0].rfind(i[1]) for i in delimited]
    print "\n".join([str(i) for i in positions])
