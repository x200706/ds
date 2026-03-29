# 建立霍夫曼編碼表
def build_code(tree, index, current_code, encode_table):
    if index >= len(tree):
        return
    
    val = tree[index]
    if val != '0':
        encode_table[val] = current_code
    
    # 左邊走 0
    build_code(tree, 2 * index + 1, current_code + "0", encode_table)
    # 右邊走 1
    build_code(tree, 2 * index + 2, current_code + "1", encode_table)

# 解碼 01 字串
def decode_bits(tree, msg):
    result = []
    current_node = 0
    
    for bit in msg:
        if bit == "0":
            current_node = 2 * current_node + 1
        else:
            current_node = 2 * current_node + 2
        
        if current_node < len(tree) and tree[current_node] != "0":
            result.append(tree[current_node])
            current_node = 0
    
    return "".join(result)

# 編碼文字
def encode_chars(encode_table, msg):
    encoded = []
    for char in msg:
        encoded.append(encode_table[char])
    return "".join(encoded)

# 主迴圈
while True:
    try:
        # 1. 讀樹
        tree_line = input().strip()
        tree = tree_line.split()
        
        # 建立編碼表
        encode_table = {}
        build_code(tree, 0, "", encode_table)
        
        # 2. 讀訊息數量
        M = int(input())
        
        # 3. 讀 M 個訊息並處理
        for _ in range(M):
            msg = input().strip()
            
            # 判斷是 01 解碼 或 文字編碼
            is_binary = True
            for c in msg:
                if c not in "01":
                    is_binary = False
                    break
            
            if is_binary:
                print(decode_bits(tree, msg))
            else:
                print(encode_chars(encode_table, msg))
    
    except EOFError:
        break

