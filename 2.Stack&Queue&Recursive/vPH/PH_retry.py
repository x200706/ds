def count(s):
    if not s:
        return ''
    next_str = ''
    target_c = s[0]
    counter = 1
    for c in s[1:]:
        if c == target_c:
            counter+=1
        else:
            next_str+= str(counter)+target_c
            target_c = c
            counter=1
    next_str += str(counter) + target_c
    return next_str


def rec_to_create_seq(n):
    if n == 0:
        return "1"
    prev = rec_to_create_seq(n-1)
    curr = count(prev)
    return curr

while True:
    n = int(input())
    if n == -1:
        break
    res = rec_to_create_seq(n)
    print(res)