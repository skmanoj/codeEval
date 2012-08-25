import sys


def trailing_string(ary):
    if ary[0].split()[-1].endswith(ary[1]):
        return 1
    else:
        return 0


test_cases = open(sys.argv[1], 'r')
for line in test_cases:
    line = line.rstrip()
    if line:
        print trailing_string(line.split(','))

