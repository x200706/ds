import sys
input = sys.stdin.readline

# 演算法：排序 + Two Pointers
# 排序後用頭尾指針配對，使兩人書籍數量之和盡量相等（最大化配對數）。

try:
    while True:
        line = input().strip()
        if not line: continue
        n = int(line)
        if n == 0:
            break
        xs = list(map(int, input().split()))
        xs.sort()
        lo, hi = 0, n - 1
        pairs = []
        while lo < hi:
            pairs.append(xs[lo] + xs[hi])
            lo += 1
            hi -= 1
        print(len(pairs))
        print(' '.join(map(str, pairs)))
except EOFError:
    pass
