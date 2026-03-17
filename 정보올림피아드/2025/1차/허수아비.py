# 문제: 허수아비 서브태스크
# 핵심 접근: '정예 허수아비 클럽' 모델링 (Greedy + Priority Queue)
# 클럽의 목표는 P 이상의 방어력을 '최소 인원'으로 유지하는 것.

import sys
import heapq


def solve():

    N, P = map(int, sys.stdin.readline.input().split())
    A = list(map(int, sys.stdin.readline.input().split()))

    results = []

    # '정예 클럽'의 멤버 리스트 (가장 약한 멤버를 바로 찾기 위해 최소 힙 사용)
    club_members_pq = []

    # 클럽 멤버들의 현재 방어력 총합
    club_total_power = 0

    # i번째 허수아비가 도전자(challenger)로 등장
    for challenger_power in A:

        # 1. 새로운 도전자를 일단 클럽에 임시로 받아준다.
        club_total_power += challenger_power
        heapq.heappush(club_members_pq, challenger_power)

        # 2. 멤버 재조정: 클럽의 힘이 과도하면 가장 약한 멤버부터 방출시킨다.
        #    "가장 약한 멤버(club_members_pq[0])가 없어도 목표(P) 달성이 가능한가?"
        while club_members_pq and club_total_power - club_members_pq[0] >= P:
            # 가능하다면, 가장 약한 멤버를 방출하여 클럽을 최소 인원으로 만든다.
            weakest_member = heapq.heappop(club_members_pq)
            club_total_power -= weakest_member

        # 3. 현재 클럽 상태를 보고한다.
        #    목표 달성이 가능한가?
        if club_total_power >= P:
            # 가능하다면, 현재 클럽의 인원 수가 최소 개수.
            results.append(len(club_members_pq))
        else:
            # 불가능하다면, 정예 클럽 결성 실패.
            results.append(-1)

    print(*results)


if __name__ == "__main__":
    solve()