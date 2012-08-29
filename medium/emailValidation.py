import re
import sys

f=open(str(sys.argv[1]),"r")
for line in f.readlines():
	line=line.rstrip("\n")
