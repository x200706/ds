import sys
input = sys.stdin.readline

# 演算法：排序（找最小差值）
# PerfectValue：從所有 n*n 個差值中取最小的 n 個（全域排序後取前 n）。
# SelectedValue：每列各取與 m 差值最小的那個，加總。

case = 1
try:
    while True:
        line = input().split()
        n = int(line[0])
        if n == 0:
            break
        m = int(line[1])
        matrix = []
        all_diffs = []
        for _ in range(n):
            row = list(map(int, input().split()))
            matrix.append(row)
            for v in row:
                all_diffs.append(abs(v - m))

        all_diffs.sort()
        perfect  = sum(all_diffs[:n])
        selected = sum(min(abs(v - m) for v in row) for row in matrix)

        print(f'Case {case}: {perfect} VS. {selected}')
        print('Perfect Teammate.' if perfect == selected else 'Just Teammate.')
        case += 1
except EOFError:
    pass
