import sys

for line in sys.stdin:
    s = line.rstrip('\n')
    stack = [] 
    for c in s:
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
    print("SUCCESS" if not stack else "FAIL")