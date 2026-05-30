import sys
input = sys.stdin.readline

# 演算法：多鍵排序（Multi-key sort）
# 優先分貝高 > 速度快 > 重量輕 > 編號小，用 sorted + key tuple 實現。

try:
    while True:
        n = int(input())
        if n == 0:
            break
        mosquitoes = []
        for _ in range(n):
            parts = input().split()
            no      = int(parts[0])
            weight  = float(parts[1])
            speed   = float(parts[2])
            decibel = float(parts[3])
            mosquitoes.append((no, weight, speed, decibel))
        mosquitoes.sort(key=lambda x: (-x[3], -x[2], x[1], x[0]))
        print(' '.join(str(m[0]) for m in mosquitoes))
except EOFError:
    pass
