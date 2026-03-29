def build_post(cal):
    priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
    op_stack = []
    post = []
    for e in cal:
        if e.isdigit():
            post.append(e)
        elif e == '(':
            op_stack.append(e)
        elif e == ')':
            peek = op_stack.pop()
            while peek != '(':
                post.append(peek)
                peek = op_stack.pop()
        else:
            while op_stack and priority[op_stack[-1]] >= priority[e]:
                post.append(op_stack.pop())
            op_stack.append(e)
    return post

def calu(post):
    print(' '.join(post))
    while len(post) > 1:
        for i, elem in enumerate(post):
            if elem in '+-*/':
                op_idx = i
                break
                # 計算當前運算子對應的結果
        num1 = int(post[op_idx-2])
        num2 = int(post[op_idx-1])
        op = post[op_idx]
        if op == '+':
            res = num1 + num2
        elif op == '-':
            res = num1 - num2
        elif op == '*':
            res = num1 * num2
        elif op == '/':
            res = int(num1 / num2)  # 數學整除
        
        # 更新列表：刪除兩個數字+運算子，插入計算結果
        del post[op_idx-2:op_idx+1]
        post.insert(op_idx-2, str(res))
        
        # 輸出當前更新後的列表（空格分隔）
        print(' '.join(post))


while True:
    try:
        cal = list(input())
        post = build_post(cal)
        calu(post)
    except EOFError:
        break