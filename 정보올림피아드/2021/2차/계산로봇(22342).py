def solve1():
    # 1. 격자 크기 입력
    M, N = map(int, input().split())

    # 2. 파이썬 최적화: list(map())보다 리스트 컴프리헨션이 미세하게 더 빠르고 직관적임
    grid = [[int(char) for char in input().strip()] for _ in range(M)]

    # 3. DP 배열 초기화: '이전 열(j-1)'의 출력값들 (초기값은 첫 열의 가중치)
    prev_output = [grid[i][0] for i in range(M)]
    max_storage = 0  # 우리가 찾고자 하는 최종 정답 (최대 저장값)

    # 4. 시간(j, 열)의 흐름에 따른 시뮬레이션
    for j in range(1, N):
        curr_output = [0] * M

        # 공간(i, 행)의 모든 세포(로봇) 업데이트
        for i in range(M):
            # [입력 단계] 이전 열에서 내게 올 수 있는 3갈래 길 중 가장 큰 눈덩이(저장값) 찾기
            best_input = prev_output[i]  # 바로 왼쪽
            if i > 0:
                best_input = max(best_input, prev_output[i - 1])  # 왼쪽 위
            if i < M - 1:
                best_input = max(best_input, prev_output[i + 1])  # 왼쪽 아래

            # [출력 단계] 내 저장값에 가중치를 더해 다음으로 보낼 눈덩이(출력값) 갱신
            curr_output[i] = best_input + grid[i][j]

            # [정답 갱신] 로봇의 '저장값'들 중 역사상 최고로 큰 값 기록
            max_storage = max(max_storage, best_input)

        # 다음 시간을 위해 상태 넘겨주기 (Rolling DP)
        prev_output = curr_output

    print(max_storage)

def solve2(): #김이한
    # 계산 로봇
    n, m = map(int, input().split())
    l = []
    for _ in range(n):
        l.append(list(map(int, input().strip())))
    ma = 0
    answer = [[0 for _ in range(m)] for _ in range(n)]
    for k in range(n):
        answer[k][0] = l[k][0]
    for j in range(1, m):
        for i in range(n):
            c_ma = 0
            for a in range(max(0, i - 1), min(n, i + 2)):
                if answer[a][j - 1] >= c_ma:
                    c_ma = answer[a][j - 1]
                answer[i][j] = c_ma + l[i][j]
            if c_ma >= ma:
                ma = c_ma
    print(ma)


def solve3(): #오민영
    # 계산 로봇
    m, n = map(int, input().split())  # 3 4
    arr = [[0] * (n + 1)] + [[0] + [int(char) for char in input().strip()] for _ in range(m)]
    mx = 0

    prev_dp = [0 for _ in range(m + 2)]
    m_value = 0

    for j in range(1, n + 1):
        curr_dp = [0 for _ in range(m + 2)]
        for i in range(1, m + 1):
            if i == 1:
                curr_dp[i] = max(prev_dp[i], prev_dp[i + 1])
            elif i == m:
                curr_dp[i] = max(prev_dp[i], prev_dp[i - 1])
            else:
                curr_dp[i] = max(prev_dp[i], prev_dp[i - 1], prev_dp[i + 1])
            m_value = max(m_value, curr_dp[i])
            curr_dp[i] += arr[i][j]
        prev_dp = curr_dp
    print(m_value)
if __name__ == '__main__':
    solve1()