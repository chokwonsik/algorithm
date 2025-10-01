"""
https://www.acmicpc.net/problem/10837
문제 이름: 동전 게임
출처: 정보올림피아드, 2015, 중등1, 고등1
알고리즘 분류:
"""

def solve1():
    # 문제 해설
    # 영희와 동수는 최대 K번 라운드로 동전을 번갈아 던집니다.
    # 동전 앞면이 나오면 1점, 뒷면이면 0점입니다.
    # 게임은 다음 중 하나가 발생하면 즉시 종료됩니다:
    #  1) 남은 라운드 수만큼 점수를 뒤집어도 상대 점수를 따라잡거나 앞설 수 없을 때
    #  2) 마지막 라운드 동수 차례까지 모두 진행된 후
    # 두 점수 M, N이 나올 수 있는 조건을 아래 수식으로 정리할 수 있습니다.
    #   gap = |M - N|    # 현재 점수 차이
    #   remain = K - max(M, N)  # 앞으로 남은 라운드 수 (영어 변수명 remain 사용)
    # 1) M == N: gap = 0 → 언제나 가능
    # 2) M < N: gap - remain <= 1 이어야 가능
    #    (동수가 앞선 상태에서 영희가 remain번 앞면을 얻어도 점수 차이가 1 이하로 내려야 함)
    # 3) M > N: gap - remain <= 2 이어야 가능
    #    (영희가 앞선 상태에서 동수가 remain번 앞면을 얻어도 점수 차이가 2 이하로 유지되어야 함)
    import sys
    input = sys.stdin.readline

    # K: 총 라운드 수, C: 질의 개수
    K = int(input().strip())
    C = int(input().strip())

    results = []
    for _ in range(C):
        M, N = map(int, input().split())
        # gap: 현재 점수 차이, remain: 앞으로 남은 라운드 수
        gap = abs(M - N)
        remain = K - max(M, N)

        if M == N:
            # 동점이면 gap=0 → 무조건 가능
            results.append("1")
        elif M < N:
            # 동수가 앞섰을 때
            # gap - remain <= 1 이면 영희가 remain번 앞면을 얻어 점수 차이를 좁힐 수 있음
            results.append("1" if gap - remain <= 1 else "0")
        else:
            # 영희가 앞섰을 때
            # gap - remain <= 2 이면 동수가 remain번 앞면을 얻어도 점수 차이를 좁히지 못함
            results.append("1" if gap - remain <= 2 else "0")

    # 결과를 한 번에 출력 (join 이용으로 print 호출 최소화)
    print("\n".join(results))


if __name__ == "__main__":
    solve1()

