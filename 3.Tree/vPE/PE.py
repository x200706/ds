from collections import defaultdict, deque
import sys

def solve(lines, idx):
    n = int(lines[idx]); idx += 1
    w1, w2 = map(int, lines[idx].split()); idx += 1

    children = defaultdict(list)
    parent = {}
    all_nodes = set()

    for _ in range(n):               # ← 固定讀 n 行
        parts = list(map(int, lines[idx].split())); idx += 1
        p = parts[0]
        all_nodes.add(p)
        for c in parts[1:]:
            children[p].append(c)
            parent[c] = p
            all_nodes.add(c)

    # 找根
    root = next(node for node in all_nodes if node not in parent)

    # BFS 建深度與父節點表
    depth = {root: 0}
    par = {root: None}
    q = deque([root])
    while q:
        cur = q.popleft()
        for child in children[cur]:
            depth[child] = depth[cur] + 1
            par[child] = cur
            q.append(child)

    # LCA
    u, v = w1, w2
    while depth[u] > depth[v]: u = par[u]
    while depth[v] > depth[u]: v = par[v]
    while u != v: u = par[u]; v = par[v]

    dist = depth[w1] + depth[w2] - 2 * depth[u]
    return dist, idx

def main():
    data = sys.stdin.read().split('\n')
    lines = [l.strip() for l in data if l.strip()]  # 去掉空行與 \r
    idx = 0
    while idx < len(lines):
        ans, idx = solve(lines, idx)
        print(ans)

if __name__ == "__main__":
    main()