N = int(input())
a = [0 for _ in range(N)]
for y in range(N):
    x = int(input()) - 1
    a[x] = (N + 1) - (y + 1)
print(a)

