"""
https://www.acmicpc.net/problem/10166
문제 이름:관중석
출처:정보올림피아드, 2014, 중등2, 고등1
알고리즘 분류:수학, 정수론 유클리드 호제법
"""


import sys, math

def solve1():
    """
    풀이2: 약수 + 토티언트 활용
    각 r마다 약수 q를 통해 가려지지 않는 좌석을 φ(
    q) 개 단위로 계산
    시간복잡도: O(N log log N + N sqrt N)
    """
    input = sys.stdin.readline
    D1, D2 = map(int, input().split())
    N = D2
    # 1) 토티언트 배열 φ 초기화 (에라토스테네스 방식)
    phi = list(range(N + 1))
    for i in range(2, N + 1):
        if phi[i] == i:
            for j in range(i, N + 1, i):
                phi[j] -= phi[j] // i

    ans = 0
    # 2) 각 반지름 r에 대해 약수 q 검사
    for r in range(D1, D2 + 1):
        limit = int(math.isqrt(r))
        for q in range(1, limit + 1):
            if r % q == 0:
                # q가 약수인 경우
                if ((D1 + q - 1) // q) * q >= r:
                    ans += phi[q]
                # 짝약수 q2 처리
                q2 = r // q
                if q2 != q and ((D1 + q2 - 1) // q2) * q2 >= r:
                    ans += phi[q2]

    print(ans)


def solve2():
    """
    풀이2: 브루트포스 시뮬레이션
    모든 좌석을 직접 검사해 가려지지 않는지 판별
    시간복잡도: O(∑r)=O(N^2)
    """
    input = sys.stdin.readline
    D1, D2 = map(int, input().split())
    ans = 0
    for r in range(D1, D2 + 1):
        for k in range(r):
            # r, k의 gcd로 간격 q 계산
            g = math.gcd(r, k)
            q = r // g
            # D1 이상의 첫 좌석이 r 위치 이상인지 확인
            if ((D1 + q - 1) // q) * q >= r:
                ans += 1

    print(ans)


if __name__ == '__main__':
    # 기본으로 더 효율적인 solve1() 실행
    solve1()

    #solve2()
