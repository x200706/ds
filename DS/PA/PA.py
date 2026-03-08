arr = list(map(int, input().split()))
n = len(arr)

Q_list = []
while True:
    try:
        q = int(input())
        Q_list.append(q)
    except:
        break

# 暴力法
for Q in Q_list:
    min_len = float('inf')
    # 遍歷所有起始位置i
    for i in range(n):
        current_sum = 0
        # 從i開始往後加
        for j in range(i, n):
            current_sum += arr[j]
            # 滿足條件就記錄長度
            if current_sum >= Q:
                min_len = min(min_len, j - i + 1)
                break
    
    # 輸出結果
    if min_len == float('inf'):
        print(0)
    else:
        print(min_len)