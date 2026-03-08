import sys

def check_gene(a, b):
    # 邊界1：長度不同直接False（題目可能隱含長度相同，但需防呆）
    if len(a) != len(b):
        return False
    # 邊界2：空字符串直接False
    if len(a) == 0:
        return False
    # 條件1：字符組成完全相同（排序比對）
    if sorted(a) != sorted(b):
        return False
    # 條件2：統計不同位置數量
    diff_pos = []
    for i in range(len(a)):
        if a[i] != b[i]:
            diff_pos.append(i)
            # 超過2個直接返回False，優化效率
            if len(diff_pos) > 2:
                return False
    # 關鍵修正：僅有2個不同位置，且交換後相等
    if len(diff_pos) == 2:
        i, j = diff_pos
        return a[i] == b[j] and a[j] == b[i]
    # 其他情況（0/1個不同位置）返回False
    return False

# 逐行讀取輸入，處理多測資
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    # 分割A和B（兼容多空格分隔）
    parts = line.split()
    if len(parts) != 2:
        print("False")
        continue
    a, b = parts
    # 嚴格按題目要求輸出：首字母大寫的True/False
    print("True" if check_gene(a, b) else "False")