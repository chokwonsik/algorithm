def main():
    # 입력 받기: 도로 길이 L, 가로등 개수 N, 출력할 개수 K
    L, N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # K가 최대 500,000이므로 고려할 어두움 값의 범위를 K+1 정도로 잡습니다.
    D = K + 1

    # diff 배열: 중간 구간(두 가로등 사이)에서 d (d>=1) 값의 등장 횟수를 구간 덧셈 방식으로 기록합니다.
    diff = [0] * (D + 2)  # 인덱스 0부터 D+1까지 사용 (실제로는 1 ~ D 사용)

    # 인접한 두 가로등 사이의 구간에 대해 어두움 값의 빈도를 diff 배열로 업데이트
    for i in range(N - 1):
        gap = A[i + 1] - A[i]  # 두 가로등 사이의 거리
        m = gap // 2  # 중앙에 해당하는 어두움 값
        if m >= 1:
            if m > 1:
                # 어두움 값 1부터 m-1까지는 각 값이 두 번씩 등장합니다.
                hi = m if m <= D else D + 1
                diff[1] += 2
                diff[hi] -= 2
            # 중앙 어두움 값 m은 gap이 홀수이면 2번, 짝수이면 1번 등장합니다.
            if m <= D:
                diff[m] += (2 if gap % 2 == 1 else 1)

    # diff 배열을 누적합하여 각 어두움 값 d (1<=d<=D) 에서 중간 구간의 기여량을 계산합니다.
    gapContrib = [0] * (D + 1)
    current = 0
    for d in range(1, D + 1):
        current += diff[d]
        gapContrib[d] = current

    # 함수 f(d): 어두움 값 d가 전체 도로에서 몇 번 등장하는지 계산합니다.
    def f(d):
        if d == 0:
            return N  # 가로등 위치에서는 어두움이 0 (총 N개)
        cnt = gapContrib[d]
        # 좌측 구간: 0부터 첫 가로등 위치 A[0]까지
        if d <= A[0]:
            cnt += 1
        # 우측 구간: 마지막 가로등 위치 A[-1]부터 L까지
        if d <= (L - A[-1]):
            cnt += 1
        return cnt

    # 어두움 값 0부터 차례대로, f(d)만큼 등장하는 것으로 보고 K개를 출력합니다.
    remain = K
    d = 0
    results = []
    while remain > 0:
        cnt = f(d)
        if cnt > 0:
            take = cnt if cnt <= remain else remain
            results.extend([str(d)] * take)
            remain -= take
        d += 1

    print("\n".join(results))


if __name__ == '__main__':
    main()
