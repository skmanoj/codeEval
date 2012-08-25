import sys
from math import sqrt

def double_square(n):
    s = int(sqrt(n))
    count = 0
    for i in range(0, s + 1):
        D = sqrt(n - i * i)
        if D >= i and D == int(D):
            count += 1
    return count

test_cases = open(sys.argv[1], 'r')
n = int(test_cases.next())
for i in range(n):
    print(double_square(int(test_cases.next().rstrip())))

