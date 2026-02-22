N = int(input())
A = [0] + list(map(int, input().split()))

D = [0 for _ in range(N+1)]

for i in range(1, N+1):
    r = D[i-1]
    x = A[i]
    for j in range(i-1, 0, -1):
        x = A[j] - x
        if x < 0: break
        if 0 == x and r <= D[j-1]:
            r = D[j-1] + 1
    D[i] = r

print(N - D[N])