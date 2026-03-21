def cycle_length(n):
    if n == 1:
        return 1
    if n % 2 == 1:
        return cycle_length(3 * n + 1) + 1
    else:
        return cycle_length(n // 2) + 1

while True:
    try: 
        n = int(input())
        print(cycle_length(n))
    except EOFError:
        break