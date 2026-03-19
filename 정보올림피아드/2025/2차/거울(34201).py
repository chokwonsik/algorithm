"""
https://www.acmicpc.net/problem/34201
문제 이름: 거울
출처: 2025 2차 초등부2, 중등부1
알고리즘 분류: 수학, 그리디, 애드 혹
"""

def solve1():
    import sys
    input = sys.stdin.readline
    N, s = map(int, input().split())
    A = list(map(int, input().split()))

    # 뺄 그룹과 더할 그룹의 개수
    num_neg = N // 2
    num_pos = N - num_neg

    # 슬라이싱으로 각 그룹의 합을 구함
    sum_large = sum(A[N - num_pos:])  # A[-num_pos:] 와 동일
    sum_small = sum(A[:num_neg])

    # 교대합 계산
    alternating_sum = sum_large - sum_small

    # 최종 위치 계산
    if N % 2 == 0:
        result = 2 * alternating_sum + s
    else:
        result = 2 * alternating_sum - s

    print(result)


if __name__ == "__main__":
    solve1()
