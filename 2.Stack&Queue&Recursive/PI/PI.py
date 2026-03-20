import sys

def collatz_count(init_k, limit):
    count = 1
    current = init_k
    while True:
        if current == 1:
            break

        if current % 2 == 0:
            next_num = current // 2
        else:
            next_num = 3 * current + 1

        if next_num > limit:
            break

        current = next_num
        count += 1
    return count

lines = [line.strip() for line in sys.stdin if line.strip()]
case_num = 1
for line in lines:
    k, l = map(int, line.split())
    if k < 0 and l < 0:
        break
    num_terms = collatz_count(k, l)
    print(f"Case {case_num}: K = {k}, limit = {l}, number of terms = {num_terms}")
    case_num += 1