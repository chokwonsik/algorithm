"""
https://www.acmicpc.net/problem/28325
호숫가의 개미굴
2023-2차대회, 초등부3번, 중등부2번
"""

def solve1():
    #리스트를 순회하면서 처음 등장항 쪽방을 맨 우측으로 이동
    import sys
    input = sys.stdin.readline

    # 입력 받기
    N = int(input().strip())
    arr = list(map(int, input().split()))

    total = sum(arr)
    if total == 0:
        print(N // 2)
        return

    # 1) 첫 non-zero 인덱스 찾기
    idx = 0
    for idx, a in enumerate(arr):
        if a:
            break

    # 2) 그 다음 위치부터 맨 앞으로 붙여서 회전하기
    #    절단점(첫 non-zero 방)이 배열의 맨 뒤에 오도록
    arr = arr[idx + 1:] + arr[:idx + 1]

    chk = [0] * N

    for i in range(N):
        if arr[i] or chk[i]:
            continue

        for j in range(i, N):
            if arr[j]:
                break

            chk[j] = 1
        total += (j - i + 1) // 2
    print(total)

def solve2():
    #solve1과 매우 유사, 파이썬 함수 활용 버전
    import sys
    from itertools import groupby

    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))

    total = sum(arr)
    if total == 0:
        print(n // 2)
        return

    # 첫번째 non-zero 뒤로 회전
    idx = next(i for i, x in enumerate(arr) if x > 0)
    arr = arr[idx+1:] + arr[:idx+1]

    ans = total
    # 0으로 이루어진 구간 길이마다 (L+1)//2 보너스 추가
    for val, group in groupby(arr):
        if val == 0:
            length = sum(1 for _ in group)
            ans += (length + 1) // 2

    print(ans)

def solve3():
    import sys
    input = sys.stdin.readline
    INF = -float('inf')

    n = int(input())
    C = list(map(int, input().split()))

    # Case 1: 첫 번째 방을 선택하지 않은 경우 (u_1 = 0)
    # 초기값: 첫 번째 방에 개미를 놓지 않으면 쪽방에 모두 배치할 수 있으므로 C[0] 마리 가능
    dp0 = C[0]
    dp1 = INF  # 첫 번째 방을 선택하는 경우는 배제
    for i in range(1, n):
        new_dp0 = max(dp0, dp1) + C[i]  # i번째 방에 개미를 놓지 않으면 쪽방에 모두 배치
        new_dp1 = dp0 + 1  # i번째 방에 개미를 놓으면 이전 방은 반드시 비어있어야 함
        dp0, dp1 = new_dp0, new_dp1
    ans1 = max(dp0, dp1)

    # Case 2: 첫 번째 방을 선택한 경우 (u_1 = 1)
    dp0 = INF
    dp1 = 1  # 첫 번째 방 선택 시 가치 1
    for i in range(1, n):
        new_dp0 = max(dp0, dp1) + C[i]
        new_dp1 = dp0 + 1
        dp0, dp1 = new_dp0, new_dp1
    ans2 = dp0  # u_1이 1이면 마지막 방은 반드시 0 (dp0)여야 한다.

    print(max(ans1, ans2))


if __name__ == '__main__':
    solve1()
    #solve2()
    #solve3()
