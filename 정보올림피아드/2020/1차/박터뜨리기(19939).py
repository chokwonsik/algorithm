# 박 터뜨리기
# https://www.acmicpc.net/problem/19939

def solve1():
    # 입력 받기: N은 총 공의 개수, K는 바구니(팀)의 수
    N, K = map(int, input().split())

    # 각 바구니에 최소로 들어가야 하는 공의 개수는 1, 2, ..., K
    # 최소 필요한 공의 총합 S 계산
    S = K * (K + 1) // 2

    # 남는 공의 개수 X
    X = N - S

    # 만약 남는 공이 음수라면 규칙에 맞게 분배 불가능
    if X < 0:
        print(-1)
        return

    # 여분 공을 모든 바구니에 균등하게 더할 수 있으면 (나머지가 0이면)
    if X % K == 0:
        # 분배 후 가장 많은 공 - 가장 적은 공 = (K + d) - (1 + d) = K - 1
        print(K - 1)
    else:
        # 일부 바구니에 한 개씩 추가해야 하므로 최대값이 1 커져 차이가 K가 됨
        print(K)


def solve2():
    # 입력 받기: N은 총 공의 개수, K는 바구니의 수
    N, K = map(int, input().split())

    # 최소 분배: 각 바구니에 최소 들어가야 하는 공의 개수는 1, 2, ..., K
    baskets = [i for i in range(1, K + 1)]
    S = sum(baskets)  # 최소 필요한 공의 총합

    # 만약 N이 최소합보다 작으면 규칙에 맞게 분배 불가능
    if N < S:
        print(-1)
        return

    # 남는 공의 개수
    extra = N - S

    # 모든 바구니에 extra//K 만큼 추가
    add_all = extra // K
    baskets = [b + add_all for b in baskets]

    # 남은 extra % K개의 공은 가장 큰 바구니들에 한 개씩 추가
    remainder = extra % K
    # 마지막 remainder 개 바구니에 추가 (인덱스 K - remainder 부터 끝까지)
    for i in range(K - remainder, K):
        baskets[i] += 1

    # 최종 분배된 공의 개수 차이 계산 (가장 큰 바구니 - 가장 작은 바구니)
    diff = max(baskets) - min(baskets)
    print(diff)


if __name__ == '__main__':
    #solve1()
    solve2()
