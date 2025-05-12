def find_cycle_length(N, P):
    remainder_map = {}  # 딕셔너리를 사용해 나머지를 기록
    a = (N * N) % P
    cnt = 1

    while a not in remainder_map:
        remainder_map[a] = cnt  # 현재 나머지와 해당 순서 저장
        a = (a * N) % P
        cnt += 1

    print(cnt - remainder_map[a])
    print(remainder_map[list(remainder_map.keys())[-1]])  # 사이클 길이 반환
    print(remainder_map[next(reversed(remainder_map))])
    print(remainder_map.popitem()[1])
# 입력 받기
N, P = map(int, input().split())
find_cycle_length(N, P)
