import sys

lines = [l for l in sys.stdin.read().splitlines() if l.strip()]
i = 0

while i < len(lines):
    tree = lines[i].split(); i += 1
    encode = {}

    def build(idx, code):
        if idx >= len(tree): return
        if tree[idx] != '0': encode[tree[idx]] = code
        build(2*idx+1, code+'0')
        build(2*idx+2, code+'1')

    build(0, '')
    M = int(lines[i]); i += 1

    for _ in range(M):
        msg = lines[i]; i += 1
        if all(c in '01' for c in msg):
            result, node = [], 0
            for bit in msg:
                node = 2*node+1 if bit == '0' else 2*node+2
                if node < len(tree) and tree[node] != '0':
                    result.append(tree[node]); node = 0
            print(''.join(result))
        else:
            print(''.join(encode[c] for c in msg))