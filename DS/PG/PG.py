import sys

for line in sys.stdin:
    s = line.strip()
    if not s:
        break
    n = len(s)
    res = [s[k:] + s[:k] for k in range(n)]
    print(' '.join(res))
