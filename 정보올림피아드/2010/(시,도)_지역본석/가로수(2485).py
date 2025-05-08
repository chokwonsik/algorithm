import math



# 입력 받기
N = int(input())
positions = [int(input()) for _ in range(N)]

# 각 가로수 사이의 간격 계산
diffs = [positions[i] - positions[i - 1] for i in range(1, N)]
print(diffs)
# 간격들의 최대공약수 계산
gcd = diffs[0]
for diff in diffs[1:]:
    print(gcd, diff)
    gcd = math.gcd(gcd, diff)
    print(gcd)

# 추가로 심어야 하는 가로수의 수 계산
total_trees = 0
for diff in diffs:
    total_trees += (diff // gcd) - 1

# 결과 출력
print(total_trees)