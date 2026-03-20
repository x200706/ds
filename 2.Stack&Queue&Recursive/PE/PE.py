from collections import deque
import sys

lines = [line.strip() for line in sys.stdin if line.strip()]
idx = 0
while idx < len(lines):
    N = int(lines[idx])
    idx += 1
    if N == 0:
        break
    tasks = list(map(int, lines[idx].split()))
    idx += 1
    input_q = deque(tasks)
    process_q = deque()
    limit = N  
    
    # 核心调度逻辑
    while input_q:
        if len(process_q) < limit:
            process_q.append(input_q.popleft())
        else:
            input_head = input_q.popleft()
            process_head = process_q[0]
            if input_head > process_head:
                input_q.append(process_head)
                process_q.popleft()
                process_q.appendleft(input_head)
            else:
                input_q.append(input_head)
            limit += 1 
    
    print(' '.join(map(str, process_q)))
