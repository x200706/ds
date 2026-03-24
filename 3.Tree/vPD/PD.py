import sys

def solve(line):
    tokens = line.split()
    if not tokens:
        return
    n = len(tokens)
    value = [None if t == 'None' else int(t) for t in tokens]
    results = []

    def dfs(idx, path):
        if idx >= n or value[idx] is None:
            return
        path.append(idx)
        left, right = 2*idx+1, 2*idx+2
        left_ok = left < n and value[left] is not None
        right_ok = right < n and value[right] is not None
        if not left_ok and not right_ok:
            total = sum(value[i] for i in path)
            results.append(('->'.join(str(i) for i in path), total))
        else:
            if left_ok: dfs(left, path)
            if right_ok: dfs(right, path)
        path.pop()

    dfs(0, [])
    for route, total in results:
        print(f"The route {route} took {total}.")

for line in sys.stdin:
    line = line.rstrip('\n')
    if line == 'EOF':
        break
    solve(line)