import sys
input = sys.stdin.readline

# 演算法：暴力列舉因數 + 對 chunks 整體排序
# 對每個因數 d，將字串切成長度 d 的 chunk，
# 將 chunks 視為單位整體排序後串接，若結果與原始不同則輸出。

try:
    while True:
        s = input().strip()
        if not s:
            break
        n = len(s)
        results = []
        for d in range(1, n + 1):
            if n % d == 0:
                chunks = [s[i:i+d] for i in range(0, n, d)]
                new_s = ''.join(sorted(chunks))
                if new_s != s:
                    results.append(new_s)
        if results:
            for r in results:
                print(r)
        else:
            print('orz')
except EOFError:
    pass
