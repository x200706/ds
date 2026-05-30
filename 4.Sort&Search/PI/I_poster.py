import sys
input = sys.stdin.readline

# 演算法：二分答案（Binary Search on Answer）+ 貪心（Greedy）
# 二分高度 h，對每個 h 貪心從左到右依序替每張海報找最早可放的位置，
# 判斷所有海報是否都能以高度 h 貼上。

def can_place(boards, posters, h):
    n = len(boards)
    pos = 0
    for w in posters:
        if w == 0:          # 寬度為 0 的海報不需佔位置
            continue
        found = False
        i = pos
        while i + w <= n:
            ok = True
            for j in range(i, i + w):
                if boards[j] < h:
                    ok = False
                    i = j + 1   # 跳過不合格木板
                    break
            if ok:
                pos = i + w
                found = True
                break
        if not found:
            return False
    return True

try:
    while True:
        line = input().split()
        if not line:
            break
        n, p = int(line[0]), int(line[1])
        boards  = list(map(int, input().split()))
        posters = list(map(int, input().split()))

        if not boards or not posters:
            print(0)
            continue

        lo, hi = 0, max(boards)
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_place(boards, posters, mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        print(ans)
except EOFError:
    pass
