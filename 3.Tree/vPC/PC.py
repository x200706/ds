from collections import deque
import sys

def solve():
    while True:
        try:
            n = int(input())
            
            left = [0] * (n + 1)
            right = [0] * (n + 1)
            
            for node in range(1, n + 1):
                l, r = map(int, input().split())
                left[node] = l
                right[node] = r
            
            max_depth = 0
            q = deque()
            q.append((1, 1))
            
            while q:
                u, d = q.popleft()
                if left[u] == 0 and right[u] == 0:
                    max_depth = max(max_depth, d)
                if left[u] != 0:
                    q.append((left[u], d + 1))
                if right[u] != 0:
                    q.append((right[u], d + 1))
            
            print(max_depth)
        
        except EOFError:
            break

solve()