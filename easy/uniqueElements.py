from itertools import ifilterfalse
import sys


def unique(iterable):
    seen = set()
    seen_add = seen.add

    for element in ifilterfalse(seen.__contains__, iterable):
        seen_add(element)
        yield element



test_cases = open(sys.argv[1], 'r')
for line in test_cases:
    line=line.rstrip()	
    print ','.join(unique(line.split(',')))


