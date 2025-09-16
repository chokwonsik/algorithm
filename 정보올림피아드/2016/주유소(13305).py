"""
https://www.acmicpc.net/problem/13305
문제 이름: 주유소
출처: 정보올림피아드, 2016, 중등부 2번
알고리즘 분류: 그리디 알고리즘
"""

def solve1():
    """
    문제 핵심:
    - N개의 도시, 인접 도로 길이 roads[i], 기름 가격 price[i].
    - 자동차는 1km당 1ℓ, 처음엔 기름 0ℓ.
    - 무제한 연료, 최소 비용으로 마지막 도시까지 이동.

    풀이 전략 (그리디):
    - 지금까지 본 도시 중 최저가 min_price를 유지.
    - 각 구간 i: roads[i]만큼 연료를 min_price로 구매해서 ans에 더함.
    - i번째 도시 방문 후 min_price = min(min_price, price[i]).

    시간 복잡도: O(N)
    공간 복잡도: O(N)
    """
    import sys
    input = sys.stdin.readline

    N = int(input().strip())
    roads = list(map(int, input().split()))
    price = list(map(int, input().split()))

    ans = 0
    min_price = float('inf')# 아주 큰 수로 시작

    # i는 0부터 N-2까지(roads 인덱스 맞춤)
    for i in range(N - 1):
        # 지금까지 본 도시 중 최저가로 갱신
        min_price = min(min_price, price[i])
        # i번째 도로(roads[i])만큼 기름 채우기
        ans += roads[i] * min_price

    print(ans)

if __name__ == "__main__":
    solve1()