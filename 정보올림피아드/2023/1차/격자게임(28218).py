"""
https://www.acmicpc.net/submit/28218/91426631
문제 이름: 격자게임
출처:한국정보올림피아드 > KOI 2023 1차대회 > 중등부 2번
알고리즘 분류: DP, 게임이론
"""

def solve1():
    import sys
    input = sys.stdin.readline

    N, M, K = map(int, input().split())
    board = [list(input().rstrip())[::-1] for i in range(N)][::-1]
    dp = [[False for i in range(M)] for j in range(N)]

    for i in range(N):
        for j in range(M):
            if i != 0 and board[i - 1][j] == '.': dp[i][j] |= not dp[i - 1][j]
            if j != 0 and board[i][j - 1] == '.': dp[i][j] |= not dp[i][j - 1]

            for k in range(1, K + 1):
                if i - k >= 0 and j - k >= 0:
                    if board[i - k][j - k] == '.':
                        dp[i][j] |= not dp[i - k][j - k]
                else:
                    break

    result = []
    for i in range(N):
        result.append(dp[i][::-1])
    result.reverse()

    ans = []
    Q = int(input())
    for i in range(Q):
        x, y = map(int, input().split())
        ans.append('First' if result[x - 1][y - 1] else 'Second')

    print('\n'.join(ans))


if __name__ == "__main__":
    solve1()
