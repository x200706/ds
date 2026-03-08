T = int(input())
for _ in range(T):
    N = int(input())
    names = []
    for _ in range(N):
        name = input().strip()
        names.append(name)
    print(f"Hello {', '.join(names)}")