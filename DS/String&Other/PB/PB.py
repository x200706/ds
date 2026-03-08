while True:
    try:
        # 讀取N(棋手數)、K(對弈次數)
        N, K = map(int, input().split())
        # 讀取棋手等級（保留原始順序，不排序）
        levels = list(map(int, input().split()))
        
        # 初始化DP表：dp[i][j][s]
        # i: 前i個棋手, j: 選j場比賽, s: 第i個棋手的狀態(0:未參加,1:參加1場,2:參加2場)
        # 存儲：達到該狀態的最小等級差總和
        INF = float('inf')
        # dp[i][j][0/1/2]，初始化為無窮大
        dp = [[[INF]*3 for _ in range(K+1)] for __ in range(N+1)]
        # 初始狀態：前0個棋手，選0場，狀態0，總和0
        dp[0][0][0] = 0
        
        # 填充DP表（核心邏輯）
        for i in range(1, N+1):  # 遍歷每個棋手
            for j in range(K+1):  # 遍歷選j場比賽
                # 狀態0：第i個棋手未參加 → 繼承前i-1個棋手的任意狀態
                dp[i][j][0] = min(dp[i-1][j][0], dp[i-1][j][1], dp[i-1][j][2])
                
                # 狀態1：第i個棋手參加1場 → 只能和i-1棋手配對（j>=1）
                if j >= 1:
                    # 前i-1個棋手狀態0/1，和i配對，新增等級差
                    cost = abs(levels[i-1] - levels[i-2]) if i >=2 else 0
                    dp[i][j][1] = min(dp[i-1][j-1][0], dp[i-1][j-1][1]) + cost
                
                # 狀態2：第i個棋手參加2場 → 不可能（一個棋手最多2場，此處簡化）
                dp[i][j][2] = INF
        
        # 計算最終結果：前N個棋手選K場的最小總和
        res = min(dp[N][K][0], dp[N][K][1], dp[N][K][2])
        print(res if res != INF else 0)

    except EOFError:
        break