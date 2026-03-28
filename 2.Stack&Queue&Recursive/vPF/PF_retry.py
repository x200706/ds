def count(m,n):
    if n==1:
        return m
    return 2*count(m,n-1)+m

while True:
    try:
        m = int(input())
        n = int(input())
        print(count(m,n))
    except EOFError:
        break