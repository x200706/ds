def solve():
    while True:
        try:
            # 一次讀一行（你原本的邏輯就是一行一組測資）
            line = input().strip()
            if not line:
                continue
            
            # 處理資料（完全不動邏輯）
            tokens = line.split()
            value = [None if t == 'None' else int(t) for t in tokens]
            n = len(value)
            subtree_sum = [0] * n

            # 計算子樹和
            def calc(i):
                if i >= n or value[i] is None:
                    return 0
                s = value[i] + calc(2*i+1) + calc(2*i+2)
                subtree_sum[i] = s
                return s

            total = calc(0)
            best = 0

            # 搜尋最佳解
            def search(i):
                nonlocal best  # 這裡改用 nonlocal 比較安全
                if i >= n or value[i] is None:
                    return
                s = subtree_sum[i]
                best = max(best, s * (total - s))
                search(2*i+1)
                search(2*i+2)

            # 只搜左右子樹（原本邏輯）
            search(1)
            search(2)
            print(best)

        except EOFError:
            # 輸入結束就跳出
            break

solve()