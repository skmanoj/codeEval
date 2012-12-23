import itertools


def lcs_lens(seq_x, seq_y):
    curr = list(itertools.repeat(0, 1 + len(seq_y)))
    for x in seq_x:
        prev = list(curr)
        for i, y in enumerate(seq_y):
            if x == y:
                curr[i + 1] = prev[i] + 1
            else:
                curr[i + 1] = max(curr[i], prev[i + 1])
    return curr


def lcs(seq_x, seq_y):
    nx, ny = len(seq_x), len(seq_y)
    if nx == 0:
        return []
    elif nx == 1:
        return [seq_x[0]] if seq_x[0] in seq_y else []
    else:
        i = nx // 2
        xb, xe = seq_x[:i], seq_x[i:]
        ll_b = lcs_lens(xb, seq_y)
        ll_e = lcs_lens(xe[::-1], seq_y[::-1])
        _, k = max((ll_b[j] + ll_e[ny - j], j)
                    for j in range(ny + 1))
        yb, ye = seq_y[:k], seq_y[k:]
        return lcs(xb, yb) + lcs(xe, ye)


if __name__ == '__main__':
    import sys
    try:
        dat = open(sys.argv[1])
        for l in [l.strip() for l in dat.readlines()]:
            seqs = l.split(';')
            if not seqs or len(seqs) <= 1:
                # For missing delimiter
                print ''
                continue

            print ''.join(lcs(seqs[0], seqs[1]))
    except Exception, e:
        sys.exit(e)
    finally:
        if dat:
            dat.close()
