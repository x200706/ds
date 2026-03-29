from collections import deque
while True:
    try:
        n = int(input())
        l = [0]*(n+1)
        r = [0]*(n+1)
        for i in range(1, n+1): # 要從一開始
            l[i], r[i] = map(int,input().split())
        
        max_d = 0
        q = deque()
        q.append((1,1))

        while q:
            u,d = q.popleft()
            if l[u] == 0 and r[u] == 0:
                max_d=max(max_d,d)
            if l[u] != 0:
                q.append((l[u],d+1))
            if r[u] != 0:
                q.append((r[u],d+1))
        print(max_d)
    except EOFError:
        break