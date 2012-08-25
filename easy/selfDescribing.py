import sys

def is_self_describing_numbers(s):
    if all([s.count(str(idx)) == int(num) for idx, num in enumerate(s)]):
        return 1
    else:
        return 0

test_cases = open(sys.argv[1], 'r')
for line in test_cases:
    print is_self_describing_numbers(line.rstrip())

