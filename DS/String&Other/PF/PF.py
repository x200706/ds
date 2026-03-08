T = int(input())
for _ in range(T):
    s = input().strip() 
    current = 0 
    total = 0 
    for c in s:
        if c == 'O':
            current += 1
            total += current
        else:
            current = 0 
    print(total)