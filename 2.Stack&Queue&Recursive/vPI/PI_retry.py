def count_c(current, limit, count=1):
    if current  == 1:
        return count
    if current % 2 == 1:
        next = 3*current+1
    else:
        next = current//2
    if next > limit:
        return count
    return count_c(next,limit,count+1)

case_num = 1    
while True:
    try:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break
        num_terms = count_c(a,b)
        print(f"Case {case_num}: K = {a}, limit = {b}, number of terms = {num_terms}")
        case_num += 1
    except EOFError:
        break