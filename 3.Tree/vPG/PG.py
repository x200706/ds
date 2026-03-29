def build_postorder(pre, ino):
    if not pre:
        return ''
    root = pre[0]
    idx = ino.index(root)
    left = build_postorder(pre[1:1+idx], ino[:idx])
    right = build_postorder(pre[1+idx:], ino[idx+1:])
    return left + right + root

def solve():
    T = int(input())
    for _ in range(T):
        # 同一行有 3 個值：n 前序 中序
        parts = input().split()
        n = parts[0]
        pre = parts[1]
        ino = parts[2]
        print(build_postorder(pre, ino))

solve()