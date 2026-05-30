import sys
input = sys.stdin.readline

# 演算法：位元運算（XOR）
# 將 A 補足 24 bits，分割後做 XOR，取中間 8 bits 轉十進位。

def get_bits(val, total):
    return format(val, f'0{total}b')

try:
    while True:
        line = input().strip()
        if not line:
            break
        A = int(line)
        bits = get_bits(A, 24)

        # h1: A1 (12 bits) XOR A2 (12 bits)，取中間 8 bits
        A1 = bits[:12]
        A2 = bits[12:]
        xor12 = int(A1, 2) ^ int(A2, 2)
        xor12_bits = get_bits(xor12, 12)
        h1 = int(xor12_bits[2:10], 2)

        # h2: (B1 XOR B3) XOR B2，各 8 bits
        B1 = bits[0:8]
        B2 = bits[8:16]
        B3 = bits[16:24]
        h2 = int(B1, 2) ^ int(B3, 2) ^ int(B2, 2)

        print(h1, h2)
except EOFError:
    pass
