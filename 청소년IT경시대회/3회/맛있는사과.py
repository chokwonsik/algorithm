def solve():
    import sys
    input = sys.stdin.readline
    from bisect import bisect_left

    # N: 사과의 개수, Q: 질문의 개수를 입력받습니다.
    N, Q = map(int, input().split())
    t = list(map(int, input().split()))
    s = list(map(int, input().split()))

    # 사과의 품질(t)와 크기(s)를 하나의 튜플로 묶어서 리스트를 만듭니다.
    apples = list(zip(t, s))
    # 품질 기준으로 오름차순 정렬합니다.
    apples.sort(key=lambda x: x[0])

    # 정렬된 사과의 품질만 따로 저장합니다. (이진 탐색을 위해)
    qualities = [apple[0] for apple in apples]

    # suffix 배열: 인덱스 i부터 끝까지의 사과 중,
    # 가장 큰 사과의 크기와 그 크기가 몇 개 있는지를 저장합니다.
    n = len(apples)
    suffix = [None] * n
    # 마지막 사과는 자기 자신이 최대이므로
    suffix[n - 1] = (apples[n - 1][1], 1)

    # 뒤에서부터 suffix 배열을 채웁니다.
    for i in range(n - 2, -1, -1):
        current_size = apples[i][1]
        next_max, next_count = suffix[i + 1]
        # 현재 사과의 크기가 더 크면 새로 최대값
        if current_size > next_max:
            suffix[i] = (current_size, 1)
        # 같은 크기라면 개수를 더해줍니다.
        elif current_size == next_max:
            suffix[i] = (next_max, next_count + 1)
        # 작으면 이전의 최대값을 그대로 사용합니다.
        else:
            suffix[i] = (next_max, next_count)

    output = []
    # 각 질문에 대해 이진 탐색으로 품질이 p 이상인 사과의 시작 인덱스를 찾습니다.
    for _ in range(Q):
        p = int(input())
        idx = bisect_left(qualities, p)
        if idx < n:
            # suffix[idx]에 저장된 정보에서 사과의 개수를 가져옵니다.
            _, count_apple = suffix[idx]
            output.append(str(count_apple))
        else:
            # p 이상의 품질을 가진 사과가 없으면 0을 출력합니다.
            output.append("0")

    print("\n".join(output))


if __name__ == '__main__':
    solve()
