T = input()
T = int(T)
for _ in range(T):
    line_arr = input()
    s = 1
    total = 0
    for e in line_arr:
        if e == 'O':
            total+=s
            s+=1    
        else:
            s=1
    print(total)
    