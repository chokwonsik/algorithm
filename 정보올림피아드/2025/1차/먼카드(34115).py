"""
https://www.acmicpc.net/problem/34115
문제 이름: 먼카드
출처: 2025 1차 초등부1
알고리즘 분류:구현, 브루트포스
"""

def solve1():
    N = int(input())
    cards = list(map(int, input().split()))
    result = 0
    for target in range(1, N+1):
        first_idx = cards.index(target)
        last_idx = len(cards) - 1 - cards[::-1].index(target)
        result = max(result, last_idx - first_idx-1)
    print(result)

def solve2():

    N = int(input())
    cards = list(map(int, input().split()))

    # N+1 크기의 리스트를 생성하고, 방문하지 않았다는 의미로 -1로 초기화
    first_seen = [-1] * (N + 1)
    max_dist = 0

    # 카드의 총개수는 N이 아니라 2N이므로 루프 범위를 2N으로 설정
    for i in range(2 * N):
        card = int(cards[i])

        # 만약 메모장에 이미 적힌 카드라면? (첫 방문 위치가 -1이 아니라면)
        if first_seen[card] != -1:
            # 두 카드 사이의 개수 = 현재 인덱스 - 첫 인덱스 - 1
            dist = i - first_seen[card] - 1
            # 최대 거리 갱신
            if dist > max_dist:
                max_dist = dist
        # 처음 보는 카드라면?
        else:
            # 현재 인덱스를 메모장에 기록
            first_seen[card] = i

    print(max_dist)

if __name__ == "__main__":
    #solve1()
    solve2()