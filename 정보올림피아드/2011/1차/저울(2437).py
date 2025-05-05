N = int(input().strip())  # 추의 개수
weights = list(map(int, input().split()))
weights.sort()

target = 1  # 현재까지 측정 가능한 무게의 범위: [1, target-1]
for weight in weights:
    # 만약 현재 추가 target보다 크다면, target은 측정할 수 없는 최소 무게
    if weight > target:
        break
    target += weight

print(target)