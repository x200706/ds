import sys
from collections import deque
input = sys.stdin.readline

def solve():
    LOG = 17
    import sys
    data = sys.stdin.read().split()
    idx = 0
    
    results = []
    
    while idx < len(data):
        n = int(data[idx]); idx += 1
        
        children = [[] for _ in range(n)]
        has_parent = [False] * n
        
        for _ in range(n - 1):
            a = int(data[idx]); idx += 1
            b = int(data[idx]); idx += 1
            children[a].append(b)
            has_parent[b] = True
        
        c = int(data[idx]); idx += 1
        d = int(data[idx]); idx += 1
        
        # 找根
        root = next(i for i in range(n) if not has_parent[i])
        
        # BFS 建 depth 和 parent table
        depth = [0] * n
        parent = [[0] * LOG for _ in range(n)]
        parent[root][0] = root
        
        q = deque([root])
        visited = [False] * n
        visited[root] = True
        
        while q:
            u = q.popleft()
            for v in children[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    parent[v][0] = u
                    q.append(v)
        
        # Binary lifting
        for j in range(1, LOG):
            for i in range(n):
                parent[i][j] = parent[parent[i][j-1]][j-1]
        
        # LCA query
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = parent[u][j]
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if parent[u][j] != parent[v][j]:
                    u = parent[u][j]
                    v = parent[v][j]
            return parent[u][0]
        
        results.append(lca(c, d))
    
    print('\n'.join(map(str, results)))

solve()