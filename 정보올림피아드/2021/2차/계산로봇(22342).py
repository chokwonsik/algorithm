def solve1():
    """
    Rolling DP 방식으로 문제를 해결하는 코드.
    각 행에서 이전 열의 출력값(자기 자신, 위, 아래 중 최댓값)을 이용해 현재 열의 출력값을 구함.
    저장 값은 (출력값 - 가중치)이며, 이 중 최댓값을 구하는 게 최종 목표.
    """
    # 1. 격자의 행(M)과 열(N)을 입력받음.
    M, N = map(int, input().split())

    # 2. 각 행의 숫자 문자열을 입력받아 한 글자씩 정수로 변환하여 2차원 리스트(격자)를 생성
    # 예시: "1234" -> [1, 2, 3, 4]
    grid = [list(map(int, list(input().strip()))) for _ in range(M)]

    # 3. 첫 번째 열의 출력값은 입력값(0)에 가중치를 더한 값이므로,
    # 각 행의 첫 열 출력값은 grid[i][0] 그대로임.
    prev = [grid[i][0] for i in range(M)]

    # 4. 최대 저장값(출력값 - 가중치)을 저장할 변수 ans 초기화
    ans = 0

    # 5. 두 번째 열부터 마지막 열까지 반복하며 DP 계산 수행
    for j in range(1, N):
        # 현재 열의 출력값을 저장할 리스트를 초기화 (행의 개수만큼 0으로 채움)
        cur = [0] * M

        # 각 행 i에 대해 처리
        for i in range(M):
            # 이전 열에서 현재 행(i)의 값, 위 행(i-1)값, 아래 행(i+1)값 중 최댓값을 구함
            best = prev[i]  # 우선 자기 자신 값을 선택
            if i > 0:
                best = max(best, prev[i - 1])  # 위쪽 행이 있으면 비교
            if i < M - 1:
                best = max(best, prev[i + 1])  # 아래쪽 행이 있으면 비교

            # 6. 현재 행(i)의 출력값 = 현재 열 가중치(grid[i][j]) + best
            cur[i] = best + grid[i][j]

            # 7. 저장값 중 최댓값(ans)을 갱신.
            ans = max(ans, best)

        # 8. 다음 열 계산을 위해 현재 열의 결과(cur)를 이전 열 값(prev)로 업데이트
        prev = cur

    # 9. 최종 최대 저장값을 출력
    print(ans)


def solve2():
    # 1. 행(M), 열(N) 입력
    M, N = map(int, input().split())
    grid = [list(map(int, list(input().strip()))) for _ in range(M)]

    # 2. dp 테이블 초기화 (M x N)
    dp = [[0] * N for _ in range(M)]
    for i in range(M):
        dp[i][0] = grid[i][0]  # 첫 열은 가중치 그대로

    ans = 0
    # 3. dp 채우기: 두 번째 열부터
    for j in range(1, N):
        for i in range(M):
            best = dp[i][j - 1]
            if i > 0:
                best = max(best, dp[i - 1][j - 1])
            if i < M - 1:
                best = max(best, dp[i + 1][j - 1])
            dp[i][j] = best + grid[i][j]
            ans = max(ans, best)
    print(ans)


if __name__ == '__main__':
    #!!!! pypy3로 제출!!!!
    #solve1()
    solve2()

