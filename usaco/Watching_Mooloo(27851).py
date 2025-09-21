"""
문제 이름: Watching Mooloo
출처: USACO 2023 February Contest > Bronze 3번
알고리즘 분류: 그리디
"""


def solve():
    import sys
    input = sys.stdin.readline

    N, K = map(int, input().split())
    days = list(map(int, input().split()))

    # 첫 구독 켜기
    cost = K + 1
    last = days[0]

    for d in days[1:]:
        gap = d - last
        if gap > K + 1:
            # 구독 만료 → 새로 결제
            cost += K + 1
        else:
            # 아직 구독 중 → 연장 비용
            cost += gap
        last = d

    print(cost)


if __name__ == '__main__':
    solve()

