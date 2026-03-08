import sys

all_input = sys.stdin.read().split()
ptr = 0
T = int(all_input[ptr])
ptr += 1
for _ in range(T):
    N = int(all_input[ptr])
    ptr += 1
    nums = list(map(int, all_input[ptr:ptr+N]))
    ptr += N
    
    current_arr = [] 
    sum_median = 0 
    
    for num in nums:
        current_arr.append(num)
        current_arr.sort()
        n = len(current_arr)
        if n % 2 == 1:
            med = current_arr[n // 2]
        else:
            med = (current_arr[n//2 - 1] + current_arr[n//2]) // 2
        sum_median += med 
    
    print(sum_median)
