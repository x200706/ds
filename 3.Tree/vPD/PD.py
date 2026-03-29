def solve(line):
    # 分割輸入
    tokens = line.split()
    if not tokens:
        return

    # 建立節點值列表（None 代表空節點）
    n = len(tokens)
    node_value = []
    for token in tokens:
        if token == "None":
            node_value.append(None)
        else:
            node_value.append(int(token))

    results = []

    # DFS 走所有根到葉子路徑
    def dfs(current_index, path):
        # 超出範圍 or 節點為空 → 回傳
        if current_index >= n or node_value[current_index] is None:
            return

        # 把目前節點加入路徑
        path.append(current_index)

        # 計算左右子節點
        left_index = 2 * current_index + 1
        right_index = 2 * current_index + 2

        # 判斷左右是否存在
        left_exist = left_index < n and node_value[left_index] is not None
        right_exist = right_index < n and node_value[right_index] is not None

        # 如果是葉節點 → 記錄路徑與總和
        if not left_exist and not right_exist:
            total = 0
            for i in path:
                total += node_value[i]
            
            path_str = "->".join(str(i) for i in path)
            results.append((path_str, total))
        
        # 否則繼續遞迴
        else:
            if left_exist:
                dfs(left_index, path)
            if right_exist:
                dfs(right_index, path)

        # 回溯：移除最後一個節點
        path.pop()

    # 從根節點開始
    dfs(0, [])

    # 輸出結果
    for route, total in results:
        print(f"The route {route} took {total}.")

while True:
    try:
        line = input().strip()
        if line == "EOF":
            break
        solve(line)
    except EOFError:
        break