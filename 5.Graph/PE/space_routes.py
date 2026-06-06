class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(0, n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            return False

        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1

        return True


while True:
    try:
        line = input().strip()
    except EOFError:
        break

    if line == "":
        continue

    n, e = map(int, line.split())

    edges = []
    for _ in range(0, e):
        x, y, p = map(int, input().split())
        edges.append((p, x, y))

    edges.sort()
    dsu = DSU(n)
    total = 0

    for p, x, y in edges:
        if dsu.union(x, y):
            total += p

    print(total)
