import sys
from bisect import bisect_left
input = sys.stdin.readline

# 演算法：排序 + Binary Search（bisect_left）
# 將商品價格排序後，對每個人的期望值 E，
# 用 bisect_left 找第一個 >= E 的價格（最低價且符合期望）。

try:
    while True:
        line = input().split()
        if not line:
            break
        m, n = int(line[0]), int(line[1])
        prices       = sorted(map(int, input().split()))
        expectations = list(map(int, input().split()))
        total = 0
        for e in expectations:
            idx = bisect_left(prices, e)
            if idx < len(prices):
                total += prices[idx]
        print(total)
except EOFError:
    pass
