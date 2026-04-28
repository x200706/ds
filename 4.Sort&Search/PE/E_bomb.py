import sys
input = sys.stdin.readline

# 演算法：Binary Search（二分搜尋）
# 在 [M, N] 範圍內用二分搜尋找 k，回傳比較次數；若 k 不在範圍內輸出 -1。

try:
    while True:
        line = input().split()
        if not line: break
        M, N = int(line[0]), int(line[1])
        k = int(input())
        if k < M or k > N:
            print(-1)
            continue
        lo, hi = M, N
        count = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            count += 1
            if mid == k:
                break
            elif mid < k:
                lo = mid + 1
            else:
                hi = mid - 1
        print(count)
except EOFError:
    pass
