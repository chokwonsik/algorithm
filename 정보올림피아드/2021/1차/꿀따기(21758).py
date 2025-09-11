def max_honey(n, data):
    # 누적합 리스트 생성
    s = [0] * n
    s[0] = data[0]  # 맨 앞칸 지정
    for i in range(1, n):
        s[i] = s[i - 1] + data[i]  # 누적합 계산
        print(s)
    ans = 0

    # 벌통과 벌 위치에 따른 최대 꿀 계산
    for i in range(1, n - 1):
        left = 0
        right = n - 1

        # 벌통이 맨 왼쪽에 있는 경우
        case1 = (s[right] - data[left] - data[i]) + (s[right] - s[i])
        # 9 9 4 1 4 9 9
        # [9, 18, 22, 23, 27, 36, 45]
        # X                   1   2
        # 45 - 9 - 18 -> 18
        # 45 - 9      -> 36
        #  1 -> 27
        #  2 -> 27
        print(case1)

        # 벌통이 맨 오른쪽에 있는 경우
        case2 = (s[i - 1]) + (s[right] - data[i] - data[right])

        # 벌통이 가운데 있는 경우
        case3 = (s[i] - data[left]) + (s[right] - s[i - 1] - data[right])

        # 세 경우 중 최대값 갱신
        ans = max(ans, case1, case2, case3)
    return ans


# 입력 처리
n = int(input())  # 장소의 수 입력
data = list(map(int, input().split()))  # 각 장소의 꿀 양 입력
# 결과 출력
print(max_honey(n, data))