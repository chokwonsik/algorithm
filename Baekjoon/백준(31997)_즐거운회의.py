# import sys

# 빠른 입력을 위해 sys.stdin.readline 사용
# input = sys.stdin.readline

n, m, t = map(int, input().split())

# 각 시간대별로 회의에 참석하는 사람을 저장할 리스트
in_meeting = [[] for _ in range(t + 1)]

# 각 시간대별로 회의에서 떠나는 사람을 저장할 리스트
out_meeting = [[] for _ in range(t + 1)]

# 각 사람의 친구 관계를 저장할 인접 리스트
friends = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    a, b = map(int, input().split())
    in_meeting[a].append(i)
    out_meeting[b].append(i)
print(in_meeting, out_meeting, sep="\n")

for _ in range(m):
    u, v = map(int, input().split())
    friends[u].append(v)
    friends[v].append(u)
print(friends)

# 현재 회의에 참석 중인 사람을 표시하는 리스트
joined = [False] * (n + 1)
print(joined)

# 현재 친구 관계 쌍의 총 수
total_relations = 0

for i in range(t):
    # 현재 시간에 회의에서 떠나는 사람들 처리
    for u in out_meeting[i]:
        joined[u] = False  # 사람이 회의에서 떠남

        # 친구 목록을 순회하며 현재 회의에 참석 중인 친구를 찾음
        for v in friends[u]:
            if joined[v]:
                total_relations -= 1  # 친구 쌍의 수 감소

    # 현재 시간에 회의에 참석하는 사람들 처리
    for u in in_meeting[i]:
        joined[u] = True  # 사람이 회의에 참석

        # 친구 목록을 순회하며 현재 회의에 참석 중인 친구를 찾음
        for v in friends[u]:
            if joined[v]:
                total_relations += 1  # 친구 쌍의 수 증가

    # 현재 시간에 친구 관계 쌍의 총 수를 출력
    print(total_relations)