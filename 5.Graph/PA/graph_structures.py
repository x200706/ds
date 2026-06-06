first_case = True

while True:
    try:
        line = input().strip()
    except EOFError:
        break

    if line == "":
        continue

    V, E, DS = map(int, line.split())
    if V == 0 and E == 0 and DS == 0:
        break

    edges = []
    for _ in range(0, E):
        a, b, w = map(int, input().split())
        edges.append((a, b, w))

    if not first_case:
        print()
    first_case = False

    if DS == 0:
        graph = [[100] * (V + 1) for _ in range(0, V + 1)]

        for i in range(1, V + 1):
            graph[i][i] = 0

        for a, b, w in edges:
            graph[a][b] = w
            graph[b][a] = w

        for i in range(1, V + 1):
            print(" ".join(f"{graph[i][j]:3d}" for j in range(1, V + 1)))
    else:
        graph = [[] for _ in range(0, V + 1)]

        for a, b, w in edges:
            graph[a].append((b, w))
            graph[b].append((a, w))

        for i in range(1, V + 1):
            ans = [str(i)]
            for to, w in sorted(graph[i]):
                ans.append(str(to))
                ans.append(str(w))
            print(" ".join(ans))
