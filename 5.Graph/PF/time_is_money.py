import heapq


T = int(input())

for _ in range(0, T):
    V, E, S = map(int, input().split())

    graph = [[] for _ in range(0, V + 1)]
    for _ in range(0, E):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))

    INF = 10**18
    dist = [INF] * (V + 1)
    dist[S] = 0
    heap = [(0, S)]

    while heap:
        cost, now = heapq.heappop(heap)

        if cost != dist[now]:
            continue

        for nxt, w in graph[now]:
            new_cost = cost + w
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(heap, (new_cost, nxt))

    print(" ".join(map(str, dist[1:])))
