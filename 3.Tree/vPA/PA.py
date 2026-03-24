import sys

for line in sys.stdin:
    tokens = line.split()
    if not tokens:
        continue
    value = [None if t == 'None' else int(t) for t in tokens]
    n = len(value)
    subtree_sum = [0] * n

    def calc(i):
        if i >= n or value[i] is None:
            return 0
        s = value[i] + calc(2*i+1) + calc(2*i+2)
        subtree_sum[i] = s
        return s

    total = calc(0)
    best = 0

    def search(i):
        global best
        if i >= n or value[i] is None:
            return
        s = subtree_sum[i]
        best = max(best, s * (total - s))
        search(2*i+1)
        search(2*i+2)

    search(1)
    search(2)
    print(best)