# 문제 요약: N일간의 여행에서 두 사람의 교통비 최소화 문제
# 핵심 접근 방식:
# 다이나믹 프로그래밍(DP)을 사용하여 문제를 해결.
# DP 상태를 dp[day][hankook_coverage][jeongol_coverage]로 정의.
# dp[i][j][k] = i일까지의 일정을 모두 소화했을 때,
# 한국이의 티켓이 j일, 정올이의 티켓이 k일 더 유효한 상태에서의 최소 비용.
# 각 날짜마다 티켓을 사지 않는 경우, 각자 사는 경우, 묶음권을 사는 경우 등
# 모든 가능한 선택지를 고려하여 DP 테이블을 채워나감.

import sys

# 빠른 입력을 위한 설정
input = sys.stdin.readline
# 큰 값(무한대)을 나타내기 위함
INF = float('inf')

def solve():
    # --- 입력 처리 ---
    N = int(input())
    A_str = input().strip()
    B_str = input().strip()
    p1, p3, p5, p_pair = map(int, input().split())

    # 문자열을 정수 리스트로 변환하여 사용하기 편하게 함
    A = [int(c) for c in A_str]
    B = [int(c) for c in B_str]

    # --- DP 테이블 초기화 ---
    # dp[i][j][k]
    # i: 날짜 (0일부터 N일까지)
    # j: 한국이 티켓 남은 유효 기간 (최대 5일권이므로 넉넉하게 6)
    # k: 정올이 티켓 남은 유효 기간
    dp = [[[INF] * 6 for _ in range(6)] for _ in range(N + 1)]
    
    # 시작점 초기화: 0일차, 둘 다 티켓 없음, 비용 0
    dp[0][0][0] = 0

    # --- DP 계산 (Bottom-Up) ---
    # 0일부터 N-1일까지 순회 (i는 현재 날짜를 의미)
    for i in range(N):
        # 한국이와 정올이의 현재 티켓 유효 기간 상태 순회
        for j in range(6):
            for k in range(6):
                # 현재 상태(dp[i][j][k])가 도달 불가능한 상태면 건너뜀
                if dp[i][j][k] == INF:
                    continue
                
                current_cost = dp[i][j][k]
                
                # 다음 날(i+1일차)에 티켓을 새로 사지 않았을 때, 남게 되는 유효기간
                # 오늘 하루가 지났으므로 유효기간이 1일씩 줄어듦
                next_j = max(0, j - 1)
                next_k = max(0, k - 1)
                
                # --- 경우의 수 계산 ---

                # 1. 아무도 티켓을 새로 구매하지 않는 경우
                # 한국이가 여행을 안 가거나, 이미 유효한 티켓이 있는 경우
                hankook_ok = (A[i] == 0) or (j > 0)
                # 정올이가 여행을 안 가거나, 이미 유효한 티켓이 있는 경우
                jeongol_ok = (B[i] == 0) or (k > 0)

                if hankook_ok and jeongol_ok:
                    dp[i+1][next_j][next_k] = min(dp[i+1][next_j][next_k], current_cost)
                
                # 2. 한국이만 1인용 티켓을 구매하는 경우
                if jeongol_ok:
                    # 1일권 구매: 다음 날 유효기간 0일 남음
                    dp[i+1][max(next_j, 0)][next_k] = min(dp[i+1][max(next_j, 0)][next_k], current_cost + p1)
                    # 3일권 구매: 다음 날 유효기간 2일 남음
                    dp[i+1][max(next_j, 2)][next_k] = min(dp[i+1][max(next_j, 2)][next_k], current_cost + p3)
                    # 5일권 구매: 다음 날 유효기간 4일 남음
                    dp[i+1][max(next_j, 4)][next_k] = min(dp[i+1][max(next_j, 4)][next_k], current_cost + p5)

                # 3. 정올이만 1인용 티켓을 구매하는 경우
                if hankook_ok:
                    dp[i+1][next_j][max(next_k, 0)] = min(dp[i+1][next_j][max(next_k, 0)], current_cost + p1)
                    dp[i+1][next_j][max(next_k, 2)] = min(dp[i+1][next_j][max(next_k, 2)], current_cost + p3)
                    dp[i+1][next_j][max(next_k, 4)] = min(dp[i+1][next_j][max(next_k, 4)], current_cost + p5)

                # 4. 둘 다 각자 1인용 티켓을 구매하는 경우 (다양한 조합)
                # 한국(1일)/정올(1일)
                dp[i+1][max(next_j, 0)][max(next_k, 0)] = min(dp[i+1][max(next_j, 0)][max(next_k, 0)], current_cost + 2 * p1)
                # 한국(1일)/정올(3일)
                dp[i+1][max(next_j, 0)][max(next_k, 2)] = min(dp[i+1][max(next_j, 0)][max(next_k, 2)], current_cost + p1 + p3)
                # ... (모든 9가지 조합을 고려)
                # 한국(5일)/정올(5일)
                dp[i+1][max(next_j, 4)][max(next_k, 4)] = min(dp[i+1][max(next_j, 4)][max(next_k, 4)], current_cost + 2 * p5)


                # 5. 묶음권을 구매하는 경우
                # 4일권 구매: 다음 날 유효기간 3일 남음
                dp[i+1][max(next_j, 3)][max(next_k, 3)] = min(dp[i+1][max(next_j, 3)][max(next_k, 3)], current_cost + p_pair)


    # --- 최종 결과 계산 ---
    # N일차까지 모두 마친 후, 모든 유효기간 상태(dp[N][j][k]) 중 최소 비용 찾기
    min_cost = INF
    for j in range(6):
        for k in range(6):
            min_cost = min(min_cost, dp[N][j][k])
            
    print(min_cost)

if __name__ == "__main__":
    solve()