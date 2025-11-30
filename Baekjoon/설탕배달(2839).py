"""
https://www.acmicpc.net/problem/2839
문제 이름: 설탕 배달
출처: 수학, DP, 그리디
알고리즘 분류: DP
"""
def solve1():
    N = int(input())

    # 불가능한 상태를 나타내는 큰 값 (N은 최대 5000이므로 5001이면 충분)
    INF = 5001
    dp = [INF] * (N + 5)  # N이 3보다 작을 때를 대비해 배열 넉넉히 생성

    # 기저 상태 (Base cases) 설정
    dp[3] = 1
    dp[5] = 1
    # 6kg부터 Nkg까지 차근차근 점화식으로 쌓아 올림
    for i in range(6, N + 1):
        dp[i] = min(dp[i - 3], dp[i - 5]) + 1

    # Nkg을 만드는 게 불가능하면 기존 초기값(INF) 이상일 것임
    if dp[N] >= INF:
        print(-1)
    else:
        print(dp[N])

def solve2():
    N = int(input())
    count = 0

    while N >= 0:
        if N % 5 == 0:  # 5의 배수가 되면
            count += (N // 5)  # 5kg 봉지로 다 담고 끝냄
            print(count)
            break
        N -= 3  # 5의 배수가 아니면 3kg 봉지 하나 추가
        count += 1
    else:
        # N이 음수가 되어 while문이 정상 종료되면 (break를 만나지 못하면)
        print(-1)

def solve3():
    # 오민영 설탕 배달
    n = int(input())
    dp = [10001 for _ in range(n + 5001)]

    dp[3] = 1
    dp[5] = 1
    for i in range(6, n + 1):
        dp[i] = min(dp[3] + dp[i - 3], dp[5] + dp[i - 5], dp[i - 3] + dp[i - 5])

    if dp[n] >= 10001:
        print(-1)
    else:
        print(dp[n])

def solve4():
    # 김이한 AI
    n = int(input())
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for sugar in [3, 5]:
        for i in range(sugar, n + 1):
            dp[i] = min(dp[i], dp[i - sugar] + 1)
    if dp[n] == float('inf'):
        print(-1)
    else:
        print(dp[n])

if __name__ == "__main__":
    solve1()
    #solve2()
