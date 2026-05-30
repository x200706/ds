import sys
input = sys.stdin.readline

# 演算法：動態規劃（DP）
# dp[i] = 達到 i 行最少需要幾次 paste。
# 轉移：dp[i] = 1 + min(dp[j]) for j in [ceil(i/2), i-1]
# 因為每次 paste 最多能讓行數翻倍，所以 j >= i/2。
# dp 單調遞增，故 min(dp[j]) = dp[ceil(i/2)]，O(n) 完成預算。

MAX_N = 10001
dp = [0] * MAX_N
for i in range(2, MAX_N):
    dp[i] = 1 + dp[(i + 1) // 2]

case = 1
try:
    while True:
        line = input().strip()
        if not line: break
        n = int(line)
        if n < 0:
            break
        print(f'Case {case}: {dp[n]}')
        case += 1
except EOFError:
    pass
