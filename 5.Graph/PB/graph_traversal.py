from collections import deque


while True:
    try:
        line = input().strip()
    except EOFError:
        break

    if line == "":
        continue

    V, E, T = map(int, line.split())
    if V == 0 and E == 0 and T == 0:
        break

    graph = [[] for _ in range(0, V + 1)]
    for _ in range(0, E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V + 1):
        graph[i].sort()

    visited = [False] * (V + 1)
    order = []

    if T == 0:
        for start in range(1, V + 1):
            if visited[start]:
                continue
            visited[start] = True
            q = deque([start])

            while q:
                now = q.popleft()
                order.append(now)

                for nxt in graph[now]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        q.append(nxt)
    else:
        for start in range(1, V + 1):
            if visited[start]:
                continue
            stack = [start]

            while stack:
                now = stack.pop()

                if visited[now]:
                    continue

                visited[now] = True
                order.append(now)

                for nxt in graph[now]:
                    if not visited[nxt]:
                        stack.append(nxt)

    print(" ".join(map(str, order)))
