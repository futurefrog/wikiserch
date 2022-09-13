a = int(input())
b = int(input())

if (a + b) % 3 != 0:
    print(-1)
else:
    n = (a + b) // 3
    if a >= n and b >= n:
        print(a - n, b - n)
    else:
        print(-1)