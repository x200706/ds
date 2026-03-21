import sys

def count_string(s):
    if not s:  # 如果字串是空的，返回空
        return ""
    next_str = ""
    target_char = s[0]  # 先盯第一個數字
    count = 1
    
    # 一個一個數
    for char in s[1:]:
        if char == target_char:
            count += 1
        else:
            next_str += str(count) + target_char
            target_char = char
            count = 1
    # 把最後一組數字加進去
    next_str += str(count) + target_char
    return next_str

def generate_sequence_recursive(n):
    if n == 0:
        return "1"
    # 遞迴核心：先拿到n-1代的數列，再數它得到n代
    prev_sequence = generate_sequence_recursive(n - 1)
    current_sequence = count_string(prev_sequence)
    return current_sequence

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n = int(line)
    if n == -1:
        break
    result = generate_sequence_recursive(n)
    print(result)