import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    idx = 0
    results = []

    while idx < len(data):
        n = int(data[idx]); idx += 1

        left = [0] * (n + 1)
        right = [0] * (n + 1)

        for node in range(1, n + 1):
            l = int(data[idx]); idx += 1
            r = int(data[idx]); idx += 1
            left[node] = l
            right[node] = r

        # BFS from root=1, 找最大深度
        max_depth = 0
        q = deque()
        q.append((1, 1))  # (node, depth)

        while q:
            u, d = q.popleft()
            if left[u] == 0 and right[u] == 0:
                max_depth = max(max_depth, d)
            if left[u] != 0:
                q.append((left[u], d + 1))
            if right[u] != 0:
                q.append((right[u], d + 1))

        results.append(max_depth)

    print('\n'.join(map(str, results)))

solve()