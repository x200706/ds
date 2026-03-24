import sys

def build_postorder(pre, ino):
    if not pre:
        return ''
    root = pre[0]
    idx = ino.index(root)
    left = build_postorder(pre[1:1+idx], ino[:idx])
    right = build_postorder(pre[1+idx:], ino[idx+1:])
    return left + right + root

def solve():
    data = sys.stdin.read().split()
    idx = 0
    c = int(data[idx]); idx += 1
    results = []
    for _ in range(c):
        n = int(data[idx]); idx += 1
        pre = data[idx]; idx += 1
        ino = data[idx]; idx += 1
        results.append(build_postorder(pre, ino))
    print('\n'.join(results))

solve()