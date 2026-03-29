T = int(input())

def build_post(s_1,s_2):
    # 遞迴停止點
    # 如果前序是空的，代表已經沒有節點了（子樹不存在）
    # 這時候不能再取 s_1[0]，不然會報錯
    if len(s_1) == 0:
        return ''
    
    # 找根節點
    # 前序規則：第一個字永遠是「根節點」
    # 所以 root = 這一層子樹的根
    root = s_1[0]

    # 在中序找到根的位置
    # 中序規則：根的「左邊」= 左子樹
    #          根的「右邊」= 右子樹
    # root_idx = 根在中序字串裡的「索引(位置)」
    root_idx = s_2.index(root)

    # 遞迴建立「左子樹」
    # s_1[1 : 1+root_idx]
    #   前序：跳過根(從1開始)，取 root_idx 個字 → 這是左子樹的前序
    # s_2[:root_idx]
    #   中序：根的左邊全部 → 這是左子樹的中序
    left = build_post(s_1[1:1+root_idx], s_2[:root_idx])

    # 遞迴建立「右子樹」
    # s_1[1+root_idx:]
    #   前序：根 + 左子樹 取完後，剩下的全部 → 這是右子樹的前序
    # s_2[root_idx+1:]
    #   中序：根的右邊全部 → 這是右子樹的中序
    right = build_post(s_1[1+root_idx:], s_2[root_idx+1:])

    # 後序 = 左子樹 + 右子樹 + 根
    return left + right + root


for _ in range(0,T):
    n, s_1, s_2 = input().split()
    print(build_post(s_1,s_2))