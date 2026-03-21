import sys

def hanoi_recursive(m, n):
    if n == 1:
        return m
    return 2 * hanoi_recursive(m, n-1) + m

lines = []
for line in sys.stdin:
    stripped_line = line.strip()
    if stripped_line:
        lines.append(stripped_line)

i = 0
while i < len(lines):
    m = int(lines[i])
    n = int(lines[i+1])
    i += 2
    res = hanoi_recursive(m, n)
    print(res)