def count(num):
    if num == 1:
        return 1
    if num % 2 == 1:
        return count(3*num+1)+1
    else:
        return count(num/2)+1

while True:
    try:
        num = int(input())
        print(count(num))
    except EOFError:
        break