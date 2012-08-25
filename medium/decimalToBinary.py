import sys

def decimal_to_binary(n):
    result = ''
    while(n > 0):
        result = str(n % 2) + result
        n /= 2
    return result

test_cases = open(sys.argv[1], 'r')
for line in test_cases:
    print(decimal_to_binary(int(line.rstrip())))

