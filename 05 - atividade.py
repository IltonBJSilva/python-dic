T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    print((N % K) + (N // K))