from collections import deque
import sys

def solve():
    # 一次讀取所有輸入，並切成清單（最穩、不會炸）
    data = list(map(int, sys.stdin.read().split()))
    ptr = 0
    LOG = 17

    # 一直讀到資料結束
    while ptr < len(data):
        # 1. 讀節點數 n
        n = data[ptr]
        ptr += 1

        children = [[] for _ in range(n)]
        has_parent = [False] * n

        # 2. 讀 n-1 條邊
        for _ in range(n - 1):
            a = data[ptr]
            b = data[ptr + 1]
            children[a].append(b)
            has_parent[b] = True
            ptr += 2

        # 3. 讀要查詢的兩個節點 c, d
        c = data[ptr]
        d = data[ptr + 1]
        ptr += 2

        # 4. 找根節點
        root = 0
        for i in range(n):
            if not has_parent[i]:
                root = i
                break

        # 5. BFS 建立深度與父節點表
        depth = [0] * n
        parent = [[0] * LOG for _ in range(n)]
        visited = [False] * n
        q = deque([root])
        visited[root] = True
        parent[root][0] = root

        while q:
            u = q.popleft()
            for v in children[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    parent[v][0] = u
                    q.append(v)

        # 6. 倍增表預處理
        for j in range(1, LOG):
            for i in range(n):
                parent[i][j] = parent[parent[i][j-1]][j-1]

        # 7. LCA 查詢
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = parent[u][j]
            if u == v:
                return u
            for j in range(LOG-1, -1, -1):
                if parent[u][j] != parent[v][j]:
                    u = parent[u][j]
                    v = parent[v][j]
            return parent[u][0]

        print(lca(c, d))

solve()