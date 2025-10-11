"""
https://www.acmicpc.net/problem/2513
문제 이름: 통학버스
출처: 정보올림피아드, 2012, 초등부 3번
알고리즘 분류: 그리디, 정렬
"""

def solve():
    """
    풀이1: 그리디 + 정렬
    1) 학교 위치 S를 기준으로 왼쪽과 오른쪽 아파트를 나눈다.
       - 왼쪽: (S - pos, 학생 수)
       - 오른쪽: (pos - S, 학생 수)
    2) 각 쪽을 학교에서 먼 거리 순(내림차순)으로 정렬한다.
    3) 먼 곳부터 버스에 학생을 태우며(rem을 현재 버스에 탄 학생 수라 함),
       - rem += 해당 단지 학생 수
       - 만약 rem > K라면, 초과된 만큼 버스를 몇 번 왕복해야 하는지 계산:
         trips = (rem - 1) // K
       - rem -= trips * K
       - ans += trips * dist  (한 번 가면 dist, 돌아와야 하므로 최종에 2배)
    4) 왼쪽과 오른쪽을 각각 처리한 뒤, ans * 2를 출력한다.
    """
    import sys
    input = sys.stdin.readline

    N, K, S = map(int, input().split())
    left, right = [], []
    for _ in range(N):
        pos, cnt = map(int, input().split())
        if pos < S:
            left.append((S - pos, cnt))
        else:
            right.append((pos - S, cnt))

    # 학교에서 먼 순서대로 정렬
    left.sort(reverse=True)
    right.sort(reverse=True)

    ans = 0
    # 왼쪽 처리
    rem = K  # rem: 현재 버스에 태워진 학생 수 (처음엔 빈 버스이므로 K명 태울 수 있다는 의미로 K)
    for dist, cnt in left:
        rem += cnt
        if rem > K:
            trips = (rem - 1) // K
            rem -= trips * K
            ans += trips * dist

    # 오른쪽 처리
    rem = K
    for dist, cnt in right:
        rem += cnt
        if rem > K:
            trips = (rem - 1) // K
            rem -= trips * K
            ans += trips * dist

    # 왕복 거리이므로 2배
    print(ans * 2)


if __name__ == '__main__':
    solve()

