"""
https://www.acmicpc.net/problem/28214
문제 이름: 크림빵
출처: 정보올림피아드 2023 1차대회 초등부 1번
알고리즘 분류: 구현
"""

def solve1():
    N, K, P = map(int, input().split())
    b = list(map(int, input().split()))

    result = 0
    for i in range(0, N * K, K):
        if b[i:i + K].count(0) < P:
            result += 1
    print(result)


if __name__ == "__main__":
    solve1()
