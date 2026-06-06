def is_tree(nodes, edges, parent, has_error):
    if len(nodes) == 0:
        return True, 0

    roots = []
    for node in nodes:
        if node not in parent:
            roots.append(node)

    if has_error or len(roots) != 1 or len(edges) != len(nodes) - 1:
        return False, None

    root = roots[0]
    graph = {}
    for a, b in edges:
        if a not in graph:
            graph[a] = []
        graph[a].append(b)

    visited = set()
    stack = [root]

    while stack:
        now = stack.pop()
        if now in visited:
            return False, None
        visited.add(now)

        for nxt in graph.get(now, []):
            stack.append(nxt)

    if len(visited) != len(nodes):
        return False, None

    return True, root


case = 1
nodes = set()
edges = []
parent = {}
has_error = False
finished = False

while not finished:
    try:
        line = input().strip()
    except EOFError:
        break

    if line == "":
        continue

    data = list(map(int, line.split()))

    for i in range(0, len(data), 2):
        a = data[i]
        b = data[i + 1]

        if a < 0 and b < 0:
            finished = True
            break

        if a == 0 and b == 0:
            ok, root = is_tree(nodes, edges, parent, has_error)

            if ok:
                print(f"Case {case} is a tree. Root is {root}.")
            else:
                print(f"Case {case} is not a tree.")

            case += 1
            nodes = set()
            edges = []
            parent = {}
            has_error = False
        else:
            nodes.add(a)
            nodes.add(b)
            edges.append((a, b))

            if b in parent:
                has_error = True
            parent[b] = a
