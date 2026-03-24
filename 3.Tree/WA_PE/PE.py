import sys
from collections import defaultdict, deque

raw = sys.stdin.read().strip()
blocks = raw.split('\n\n')

for block in blocks:
    lines = [l.strip() for l in block.strip().splitlines() if l.strip()]
    n = int(lines[0])
    w1, w2 = map(int, lines[1].split())

    children = defaultdict(list)
    parent = {}
    all_nodes = set()

    for line in lines[2:]:
        parts = list(map(int, line.split()))
        w = parts[0]
        all_nodes.add(w)
        for c in parts[1:]:
            children[w].append(c)
            parent[c] = w
            all_nodes.add(c)

    root = next(node for node in all_nodes if node not in parent)

    depth = {root: 0}
    par = {root: None}
    queue = deque([root])
    while queue:
        node = queue.popleft()
        for c in children[node]:
            depth[c] = depth[node] + 1
            par[c] = node
            queue.append(c)

    def lca(u, v):
        while depth[u] > depth[v]: u = par[u]
        while depth[v] > depth[u]: v = par[v]
        while u != v: u = par[u]; v = par[v]
        return u

    ancestor = lca(w1, w2)
    print(depth[w1] + depth[w2] - 2 * depth[ancestor])