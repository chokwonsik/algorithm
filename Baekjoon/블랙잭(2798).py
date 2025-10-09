"""

문제 이름: 블랙잭
출처: https://www.acmicpc.net/problem/2798
알고리즘 분류: 브루트포스 알고리즘
"""


def solve1():
    import itertools
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    result = 0
    for i in itertools.combinations(num,3):
        if sum(i) <= M:
            result = max(result, sum(i))
    print(result)

def solve2():
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    result = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1 ,N):
                current_sum = num[i] + num[j] + num[k]
                if current_sum <= M:
                    result = max(result, current_sum)
    print(result)


if __name__ == "__main__":
    #solve1()
    solve2()
