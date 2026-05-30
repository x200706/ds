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


T = int(input())

for _ in range(0, T):
    V, E = map(int, input().split())

    edges = []
    for _ in range(0, E):
        a, b, w = map(int, input().split())
        edges.append((w, a, b))

    edges.sort()
    dsu = DSU(V)
    total = 0

    for w, a, b in edges:
        if dsu.union(a, b):
            total += w

    print(total)
