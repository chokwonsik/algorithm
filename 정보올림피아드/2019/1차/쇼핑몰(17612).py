"""
https://www.acmicpc.net/problem/17612
쇼핑몰
2019년 1차대회 고등부 1번

문제
대형 쇼핑몰에서 쇼핑을 마친 N명의 고객들이 계산을 하고 쇼핑몰을 떠나고자 계산대 앞에 줄을 서 있다.
각 고객은 커다란 짐수레(cart)에 물건을 담아 계산대로 간다.
쇼핑몰에는 K개의 계산대가 병렬로 배치되어 있고, 안내원은 고객을 가장 빨리 계산할 수 있는 계산대로 안내한다.
여러분은 고객 N명의 정보(회원번호, 물건 개수)를 알고 있을 때, 계산을 마친 순서로 쇼핑몰을 나가는 고객들의 회원번호를 계산하여 가중합을 구해야 한다.
tip: 새치기는 안된다.
"""

def solve1():
    """
    풀이
    1) 고객 N명과 계산대 K개의 정보를 입력받습니다.
    2) 첫 K명의 고객을 각 계산대(1~K)에 배정하고, counters에 [끝나는 시간, 계산대 번호, 회원번호] 형식으로 저장합니다.
    3) 반복문을 돌며 counters가 빌 때까지 다음 단계를 수행합니다:
       3-1) 가장 먼저 끝나는 시간 t를 찾고,
       3-2) 모든 계산대 중 종료 시간이 t인 계산대를 분리합니다.
       3-3) 동시에 끝난 손님들은 계산대 번호가 큰 순서대로 exit_order에 기록합니다.
       3-4) freed 계산대(완료된 계산대) 번호를 작은 순서로 정렬하여, 남은 손님을 재배정하며 새로운 종료 시간을 계산합니다.
    4) 퇴장 순서 exit_order에서 i×회원번호 합을 구해 결과를 출력합니다.
    """
    import sys
    input = sys.stdin.readline

    # 1) 입력: 고객 수 N, 계산대 수 K
    N, K = map(int, input().split())
    # 고객 정보: (회원번호, 물건 개수) 튜플로 저장
    customers = [tuple(map(int, input().split())) for _ in range(N)]

    # 2) 초기 계산대 상태 구성
    #    첫 K명의 고객을 각 계산대(1~K)에 배정
    #    counters의 각 요소: [끝나는 시간, 계산대 번호, 회원번호]
    counters = []
    for desk, (cid, w) in enumerate(customers[:K], start=1):
        # 시작 시간은 0, 계산 소요 dd시간 w이 끝나는 시간을 의미
        counters.append([w, desk, cid])
    idx = K  # 다음에 대기 중인 고객 인덱스

    exit_order = []  # 퇴장 순서대로 회원번호 기록
    # 3) 모든 고객이 계산을 마dd칠 때까지 반복
    while counters:
        # 3-1) 가장 먼저 끝나는 계산대의 시간 t 찾기 (O(K))
        t = min(finish for finish, _, _ in counters)

        # 3-2) t 시간에 끝난 계산대들 분리
        finished = [c for c in counters if c[0] == t]
        # 남은 계산대 리스트 갱신: 아직 계산 중인 것만 남김
        counters = [c for c in counters if c[0] != t]

        # 3-3) 동시에 끝난 손님들은 계산대 번호 큰 순으로 퇴장
        #      같은 시간, 높은 계산대 번호 먼저 나감
        finished.sort(key=lambda x: x[1], reverse=True)
        for _, desk, cid in finished:
            exit_order.append(cid)

        # 3-4) 빈 계산대(finished의 desk) 작은 번호 순으로 새 고객 배정
        #      sorted로 작은 desk부터 순차 재할당
        for desk in sorted(desk for _, desk, _ in finished):
            if idx < N:
                cid, w = customers[idx]
                # 새 고객의 끝나는 시간은 현재 시간 t + 계산 시간 w
                counters.append([t + w, desk, cid])
                idx += 1

    # 4) 결과: 퇴장 순서 i(1~N)에 해당 회원번호 cid 곱해 합산
    result = sum(i * cid for i, cid in enumerate(exit_order, start=1))
    print(result)

def solve2():
    import heapq
    n, k = map(int, input().split())
    visit = [list(map(int, input().split())) for _ in range(n)]
    min_heap = [(0, i) for i in range(1, k + 1)]
    result = []
    heapq.heapify(min_heap)

    for i, j in visit:
        x, y = heapq.heappop(min_heap)
        endtime = x + j
        result.append((endtime, y, i))
        heapq.heappush(min_heap, (endtime, y))
        # print(min_heap)

    result.sort(key=lambda x: (x[0], -x[1]))
    # print(result)
    print(sum((i + 1) * result[i][2] for i in range(n)))

if __name__ == '__main__':
    solve1()
    #solve2()
