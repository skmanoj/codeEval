SUPORTED_OPERATORS = ['+', '*', '/', ]


def _eval(operator, operand1, operand2):
    if operator == "+":
        return operand1 + operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2
    else:
        raise Exception("Unknown operator: %s" % operator)


def _calc(tokens):
    stack = []
    total = None
    for token in tokens:
        if type(token) is int or type(token) is float:
            if total is None:
                total = token
            else:
                total = _eval(stack.pop(0), total, token)
        else:
            stack.insert(0, token)
    return total and total or 0


def prefix(expression):
    if not expression:
        return None

    tokens = [t.isdigit() and int(t) or t \
            for t in expression.split(' ') if t]

    if not tokens:
        return None
    return _calc(tokens)

if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        sys.exit(__doc__)

    dat = None
    try:
        dat = open(sys.argv[1])
        for l in [l.strip() for l in dat.readlines()]:
            print prefix(l)
    except Exception, e:
        sys.exit(e)
    finally:
        if dat:
            dat.close()

