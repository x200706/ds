while True:
    try:
        line = list(input())
        stack = []
        for e in line:
            if stack and e == stack[-1]:
                stack.pop()
            else:
                stack.append(e)
        if stack:
            print("FAIL")
        else:
            print("SUCCESS")
    except EOFError:
        break