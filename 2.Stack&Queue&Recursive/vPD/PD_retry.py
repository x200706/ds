from collections import deque
T = int(input())
for _ in range(0,T):
    student_num = int(input())
    student_arr = input().split()
    student_deque = deque(student_arr)
    while len(student_deque)>1:
        student_deque.append(student_deque.popleft())
        student_deque.append(student_deque.popleft())
        student_deque.popleft()
    print(student_deque[0])