T = int(input())

def solve(S):
    for i in range(len(S)):
        if S[i:] == S[i:][::-1]:
            if i == 0:
                break
            S += S[i - 1:: -1]
            break
    return S


for _ in range(T):
    S = input()
    print(solve(S))