from collections import deque
import sys

lines = [line.strip() for line in sys.stdin if line.strip()]
idx = 0
n = int(lines[idx]) 
idx += 1
for _ in range(n):
    k = int(lines[idx])
    idx += 1
    names = lines[idx].split()
    idx += 1
    q = deque(names)
    while len(q) > 1:
        q.append(q.popleft())
        q.append(q.popleft())
        q.popleft()
    print(q[0])