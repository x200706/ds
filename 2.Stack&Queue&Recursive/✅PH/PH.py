import sys

def generate_sequence(n):
    current = "1"
    
    for _ in range(n):
        next_str = ""
        if not current:
            break
        
        target_char = current[0]
        count = 1
        
        for char in current[1:]:
            # 如果和目標數字一樣，計數+1
            if char == target_char:
                count += 1
            # 如果不一樣，就把數量+數字拼起來，然後換新目標
            else:
                next_str += str(count) + target_char
                target_char = char  # 換成新的要數的數字
                count = 1           # 重新開始數
        
        # 把最後一組數字也拼進去
        next_str += str(count) + target_char
        
        # 把新數列變成當前數列，準備下一輪
        current = next_str
    
    # 最後回傳生成好的數列
    return current

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n = int(line)
    if n == -1:
        break
    result = generate_sequence(n)
    print(result)