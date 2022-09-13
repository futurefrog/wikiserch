K = int(input('K:\n'))
N = int(input('N:\n'))

print(min(N % K, K - N % K))