"""
https://www.acmicpc.net/problem/1003
문제 이름:피보나치 함수
출처:백준
알고리즘 분류:DP
"""
def fn1(n: int, memo: dict):
    if n in memo:
        return memo[n]
    if n == 0:
        return (1, 0)
    if n == 1:
        return (0, 1)
    a, b = fn1(n-1, memo)
    c, d = fn1(n-2, memo)
    memo[n] = (a+c, b+d)
    return memo[n]

def solve1():
    N = int(input())
    for i in range(N):
        num = int(input())
        memo = {}
        a, b = fn1(num, memo)
        print(a, b)

if __name__ == "__main__":
    solve1()