"""
https://www.acmicpc.net/problem/10164
문제 이름:격자상의 경로
출처: 정보올림피아드, 2014, 중등1, 초등3
알고리즘 분류: 수학, DP, 조합론
"""


def solve1():
    import sys
    N, M, K = map(int, sys.stdin.readline().split())
    def coord(x):
        return ((x-1)//M + 1, (x-1)%M + 1)
    # dp 구하는 함수
    def calc(sr, sc, er, ec):
        dp = [[0]*(M+1) for _ in range(N+1)]
        dp[sr][sc] = 1
        for i in range(sr, er+1):
            for j in range(sc, ec+1):
                if i==sr and j==sc: continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[er][ec]
    if K == 0:
        print(calc(1,1, N, M))
    else:
        kr, kc = coord(K)
        print(calc(1,1, kr, kc) * calc(kr, kc, N, M))

if __name__ == '__main__':
    solve1()

