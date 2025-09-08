# 누적거리
# https://www.acmicpc.net/problem/22345

N, Q = map(int, input().split())
house = [list(map(int, input().split())) for i in range(N)]
#print(house)
# 누적 합 계산


# 누적 거리 계산
for i in range(Q):
    q = int(input())
    result = 0
    for a, x in house:
        result += a*abs(x-q)
        print(result)