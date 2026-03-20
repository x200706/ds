def infix_to_postfix(infix):
    # 運算子優先級：() > * / > + -，( 優先級設為0避免被彈出
    priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
    op_stack = []  # 運算子的堆疊
    post_list = []  # 後序運算式列表
    
    for c in infix:
        if c.isdigit():  # 數字：直接加入後序列表
            post_list.append(c)
        elif c == '(':  # 左括號：壓入堆疊，不處理
            op_stack.append(c)
        elif c == ')':  # 右括號：彈出堆疊頂部運算子直到遇到左括號
            top_op = op_stack.pop()
            while top_op != '(':
                post_list.append(top_op)
                top_op = op_stack.pop()  # 左括號彈出但不加入列表
        else:  # 普通運算子按優先級處理
            # 堆疊非空 且 堆頂運算子優先級≥當前運算子 → 彈出堆頂加入後序列表
            while op_stack and priority[op_stack[-1]] >= priority[c]:
                post_list.append(op_stack.pop())
            # 當前運算子壓入堆疊
            op_stack.append(c)
    
    # 遍歷結束，彈出堆疊中所有運算子
    while op_stack:
        post_list.append(op_stack.pop())
    
    return post_list

def calculate_step_by_step(post_list):
    """
    逐步計算後序運算式，嚴格匹配標準輸出格式
    核心：每次計算後保留未完成的運算子，只替換已計算的數字
    """
    # 複製後序列表，用於逐步修改
    current = post_list.copy()
    # 首行先輸出完整的初始後序式
    print(' '.join(current))
    
    while len(current) > 1:
        # 找到第一個出現的運算子（從左到右計算）
        op_idx = -1
        for i, elem in enumerate(current):
            if elem in '+-*/':
                op_idx = i
                break
        
        # 計算當前運算子對應的結果
        num1 = int(current[op_idx-2])
        num2 = int(current[op_idx-1])
        op = current[op_idx]
        
        if op == '+':
            res = num1 + num2
        elif op == '-':
            res = num1 - num2
        elif op == '*':
            res = num1 * num2
        elif op == '/':
            res = int(num1 / num2)  # 數學整除
        
        # 更新列表：刪除兩個數字+運算子，插入計算結果
        del current[op_idx-2:op_idx+1]
        current.insert(op_idx-2, str(res))
        
        # 輸出當前更新後的列表（空格分隔）
        print(' '.join(current))

# 主程式
if __name__ == "__main__":
    infix = input().strip()
    post_list = infix_to_postfix(infix)
    calculate_step_by_step(post_list)