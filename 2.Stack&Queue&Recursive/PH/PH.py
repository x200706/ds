import sys

def generate_sequence(n):
    current = "1"
    for _ in range(n):
        from itertools import groupby
        next_str = ''.join(str(len(list(g))) + k for k, g in groupby(current))
        current = next_str
    return current

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n = int(line)
    if n == -1:
        break
    print(generate_sequence(n))
