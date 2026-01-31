"""
https://www.acmicpc.net/problem/13301
문제 이름: 타일 장식물
출처: 정올 2016 초등부 2번
알고리즘 분류: 수학, DP
"""


def solve1():
    def f(n):
        # 피보나치 수열 초기값
        d = [0] * (n + 2)  # n+2 크기의 배열 생성
        d[1], d[2] = 1, 1

        # 피보나치 수열 계산
        for i in range(3, n + 2):
            d[i] = d[i - 1] + d[i - 2]

        # 둘레 계산
        return 2 * (d[n] + d[n + 1])

    # 입력 및 출력
    n = int(input())
    print(f(n))


if __name__ == "__main__":
    solve1()
