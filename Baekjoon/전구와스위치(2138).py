# 입력: 첫 줄에 N, 두 번째 줄에 초기 상태, 세 번째 줄에 목표 상태
N = int(input().strip())
initial = list(map(int, list(input().strip())))
target = list(map(int, list(input().strip())))

# simulate 함수: 첫 번째 스위치를 누르는지 여부에 따라 전구 상태 변화 시뮬레이션
def simulate(first_pressed):
    count = 0
    bulbs = initial[:]  # 현재 전구 상태 복사

    # 첫 번째 스위치를 누르는 경우
    if first_pressed:
        count += 1
        # 1번 스위치 누름 → 인덱스 0, 1 전구 상태 반전
        bulbs[0] = 1 - bulbs[0]
        if N > 1:
            bulbs[1] = 1 - bulbs[1]
    # 2번 스위치부터 N번 스위치까지 순서대로 진행 (인덱스 1부터 N-1)
    for i in range(1, N):
        # 이전 전구(i-1)가 목표 상태와 다르면, i번 스위치를 눌러 수정
        if bulbs[i-1] != target[i-1]:
            count += 1
            # i번 스위치 누름 → 인덱스 i-1, i 전구 상태 반전
            bulbs[i-1] = 1 - bulbs[i-1]
            bulbs[i] = 1 - bulbs[i]
            # i번 스위치가 가운데 스위치면, 오른쪽 전구(i+1)도 반전 (단, i+1이 있으면)
            if i < N - 1:
                bulbs[i+1] = 1 - bulbs[i+1]
    # 최종 상태가 목표 상태와 같으면 누른 횟수 반환, 아니면 불가능으로 처리
    if bulbs == target:
        return count
    else:
        return float('inf')

# 두 경우 중 최소 횟수를 선택
res1 = simulate(first_pressed=True)
res2 = simulate(first_pressed=False)
result = min(res1, res2)

# 결과 출력: 만들 수 없으면 -1 출력
if result == float('inf'):
    print(-1)
else:
    print(result)
