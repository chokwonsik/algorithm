"""
문제 설명

-----------
두 정삼각형 서브태스크 문제에서는,
두 개의 정삼각형 A와 B가 주어진다.
삼각형은 첫 번째 줄에 1개, 두 번째 줄에 2개, …, N번째 줄에 N개의 숫자가 있는 형태이다.
각 숫자는 0 또는 1이다.

A는 다음과 같이 변환할 수 있다.
1. 120도 시계방향 또는 반시계방향 회전
2. 좌우 대칭 (반전)

목표는 A를 원하는 만큼 회전하거나 대칭하여,
B와 겹쳤을 때 서로 다른 위치의 수(차이)가 최소가 되도록 하는 것이다.

입력:
- 첫 번째 줄: 삼각형의 크기 N (1 ≤ N ≤ 10)
- 다음 N줄: 삼각형 A의 숫자들 (i번째 줄에 i개의 정수)
- 다음 N줄: 삼각형 B의 숫자들 (i번째 줄에 i개의 정수)

출력:
- A를 변환하여 B와의 차이의 최솟값을 출력

예를 들어,
A와 B를 비교하여 차이가 1이 되는 경우가 있을 때, 1을 출력하면 된다.
"""

"""
함수: rotate_120
설명: 주어진 정삼각형을 120도 회전, 상세 설명은 맨 아래
입력:
  - triangle: 원래 정삼각형 (리스트로 구성)
  - N: 삼각형의 크기 (행의 개수)
출력:
   - 120도 회전된 정삼각형 (새로운 리스트로 반환)
"""
def rotate_120(triangle, N):
    # 회전 후 삼각형을 저장할 빈 리스트 생성 (N개의 빈 행)
    new_triangle = [[] for _ in range(N)]
    # 모든 행과 열을 순회하며 새로운 위치에 값을 배정
    for i in range(N):
        for j in range(i + 1):
            # 회전 후의 위치는 원본의 특정 위치에서 값을 가져온다.
            new_triangle[i].append(triangle[N - j - 1][i - j])
    return new_triangle

"""
함수: reflect_triangle
설명: 주어진 정삼각형을 좌우로 대칭시킨다.
입력:
  - triangle: 원래 정삼각형
  - N: 삼각형의 크기 (실제로 N은 사용되지 않음)
출력:
  - 좌우 대칭된 정삼각형 (각 행의 순서를 뒤집어 반환)
"""
def reflect_triangle(triangle, N):
    # 각 행을 뒤집어 좌우 대칭 효과를 만든다.
    return [row[::-1] for row in triangle]

"""
함수: triangle_difference
설명: 두 정삼각형 A와 B를 비교하여 서로 다른 숫자의 개수를 센다.
입력:
  - A: 첫 번째 정삼각형
  - B: 두 번째 정삼각형
  - N: 삼각형의 크기 (행의 개수)
출력:
  - 두 삼각형에서 다른 숫자가 있는 위치의 개수 (차이)
"""
def triangle_difference(A, B, N):
    diff = 0  # 차이를 저장할 변수
    # 각 행의 각 숫자를 비교
    for i in range(N):
        for j in range(i + 1):
            if A[i][j] != B[i][j]:
                diff += 1  # 값이 다르면 차이 1 증가
    return diff


#입력 처리
N = int(input().strip())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]


#A의 변환 가능한 모든 형태 생성
A1 = A                        # 원래 상태
A2 = rotate_120(A1, N)   # 원래 상태를 120도 회전
A3 = rotate_120(A2, N)   # 원래 상태를 240도 회전 (120도를 두 번 회전)
A4 = reflect_triangle(A1, N)      # 원래 상태를 좌우 대칭
A5 = rotate_120(A4, N)   # 좌우 대칭한 상태를 120도 회전
A6 = rotate_120(A5, N)   # 좌우 대칭한 상태를 240도 회전

# 모든 변환된 A와 B의 차이를 계산후 최소값
min_diff = min(
    triangle_difference(A1, B, N),
    triangle_difference(A2, B, N),
    triangle_difference(A3, B, N),
    triangle_difference(A4, B, N),
    triangle_difference(A5, B, N),
    triangle_difference(A6, B, N)
)

# 최소 차이를 출력
print(min_diff)

"""
rotate_120 함수 상세 설명:
def rotate_120(triangle, N):
    new_triangle = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i + 1):
            new_triangle[i].append(triangle[N - j - 1][i - j])
    return new_triangle

기존 삼각형 A
A = [
    [0],       # A[0][0] = 0
    [1, 0],    # A[1][0] = 1, A[1][1] = 0
    [1, 0, 0]  # A[2][0] = 1, A[2][1] = 0, A[2][2] = 0
]
120도 회전된 삼각형 A
new_triangle = [
    [1],
    [0, 1],
    [0, 0, 0]
]

요약: 각 new_triangle[i][j]는 아래와 같이 이동:
- new[0][0] <- A[2][0]
- new[1][0] <- A[2][1]
- new[1][1] <- A[1][0]
- new[2][0] <- A[2][2]
- new[2][1] <- A[1][1]
- new[2][2] <- A[0][0]
이 함수는 새 삼각형의 각 위치 new_triangle[i][j]에 대해,
원래 삼각형의 triangle[N - j - 1][i - j] 값을 복사한다.

아래는 각 new_triangle의 원소가 어떤 원본 인덱스에서 오는지 단계별로 정리한 것이다.

1. new_triangle의 행은 i, 열은 j로 두자.
   (새 삼각형은 0번 행부터 N-1번 행까지, 각 행 i는 0번 열부터 i번 열까지 있다.)

2. 원본 삼각형 A의 인덱스는 (row, col) 형태이며,
   new_triangle[i][j] = A[N - j - 1][i - j]로 결정된다.

--- i = 0 인 경우 ---
i = 0일 때, 내부 for문은 j in range(0+1) 즉, j=0 하나만 진행.

(a) i=0, j=0:
    - 계산: N - j - 1 = 3 - 0 - 1 = 2, 그리고 i - j = 0 - 0 = 0
    - 따라서 new_triangle[0][0] = A[2][0]
    - A[2][0] 값은 1.

결과: new_triangle[0] = [1]

--- i = 1 인 경우 ---
i = 1일 때, j in range(1+1) 즉, j=0, 1 진행.

(a) i=1, j=0:
    - 계산: N - j - 1 = 3 - 0 - 1 = 2, i - j = 1 - 0 = 1
    - new_triangle[1][0] = A[2][1]
    - A[2][1] 값은 0.

(b) i=1, j=1:
    - 계산: N - j - 1 = 3 - 1 - 1 = 1, i - j = 1 - 1 = 0
    - new_triangle[1][1] = A[1][0]
    - A[1][0] 값은 1.

결과: new_triangle[1] = [0, 1]

--- i = 2 인 경우 ---
i = 2일 때, j in range(2+1) 즉, j=0, 1, 2 진행.

(a) i=2, j=0:
    - 계산: N - j - 1 = 3 - 0 - 1 = 2, i - j = 2 - 0 = 2
    - new_triangle[2][0] = A[2][2]
    - A[2][2] 값은 0.

(b) i=2, j=1:
    - 계산: N - j - 1 = 3 - 1 - 1 = 1, i - j = 2 - 1 = 1
    - new_triangle[2][1] = A[1][1]
    - A[1][1] 값은 0.

(c) i=2, j=2:
    - 계산: N - j - 1 = 3 - 2 - 1 = 0, i - j = 2 - 2 = 0
    - new_triangle[2][2] = A[0][0]
    - A[0][0] 값은 0.

결과: new_triangle[2] = [0, 0, 0]

이와 같이 함수는 내부의 두 for문을 통해
원본 삼각형의 각 요소를 새로운 위치로 복사하여 120도 회전 효과를 만든다.
"""

