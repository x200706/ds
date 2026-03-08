import sys

for line in sys.stdin:
    s = line.rstrip('\n')
    if len(s) == 0:
        break
    n = len(s)
    # 核心邏輯：以每個位置k為首，拼接後面+前面的字符
    res = [s[k:] + s[:k] for k in range(n)]
    # 單空格分隔輸出
    print(' '.join(res))
