# =====================================================================
# 🏆 [특성화고/정올 대비] 파이썬 알고리즘 마스터 워크북 (All-in-One)
# =====================================================================
# 이 파일은 코딩 테스트의 기초 문법부터 실전 2차원 배열 제어까지
# 모든 필수 스킬과 문제-정답이 100% 압축된 마스터 파일입니다.
# 눈으로 보지 말고, 손가락이 기억할 때까지 반복해서 타이핑하세요.

import sys
import math
import copy
from collections import deque, Counter, defaultdict
import itertools
import bisect

# =====================================================================
# 챕터 1. 입출력 및 파이썬 필수 스킬 (Input & Pythonic Skills)
# [설명] 코테에서 시간 초과를 피하고, 코드를 짧게 만드는 기본기입니다.
# =====================================================================
print("--- [챕터 1. 입출력 및 스킬] ---")

# 1. 빠른 입력 세팅 (무조건 암기)
input = sys.stdin.readline  # 백준 제출 시 주석 해제하여 사용하세요.

# 1-1. 재귀 한도 해제 (DFS 필수 공식) ★★★
# 파이썬은 재귀(DFS)를 1000번 이상 돌면 런타임 에러(RecursionError)가 납니다.
sys.setrecursionlimit(10 ** 6)

# 2. 리스트 요소를 하나의 문자열로 합치기 (join)
a_list = [1, 2, 3, 4, 5]
print("리스트 합치기:", "".join(map(str, a_list)))  # 12345

# 3. enumerate (인덱스와 값을 동시에 추출)
arr = ['apple', 'banana', 'cherry']
for i, v in enumerate(arr):
    print(f"인덱스 {i}: {v}")

# 4. 가변 객체(List)의 얕은 복사 함정 피하기 (deepcopy)
original = [1, 2, 3]
copied = copy.deepcopy(original)  # 그냥 copied = original 하면 원본이 오염됩니다.

# 5. 암시적 조건문 (비어있는지 확인할 때 len() 쓰지 않기)
empty_list = []
if not empty_list:
    print("리스트가 비어있습니다 (파이써닉한 방법)")

# =====================================================================
# 챕터 2. 반복문 & 조건문 맛있게 먹어보기
# [설명] 논리적 사고력의 뼈대입니다. 모든 문제를 내장 함수와 구현으로 풉니다.
# =====================================================================
print("\n--- [챕터 2. 반복문 & 조건문] ---")

# 문제 1: 1부터 20까지 홀수 출력
print("Q1:", [i for i in range(1, 21, 2)])

# 문제 2: 2~9단 구구단 출력
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f"{i}*{j}={i*j}")

# 문제 3: 숫자 뒤집기 (문자열 슬라이싱 활용이 가장 빠름)
num_str = "12345"
print("Q3 숫자 뒤집기:", num_str[::-1])

# 문제 4 & 12: 팩토리얼 계산
n = 5
print(f"Q4 팩토리얼({n}!):", math.factorial(n))


# 문제 5: 소수 판별하기 (O(√N) 최적화 방식)
def is_prime(num):
    if num < 2: return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0: return False
    return True


print("Q5 7은 소수인가?:", is_prime(7))

# 문제 6: 피보나치 수열 n개 출력
n_fibo = 10
fibo = [1, 1]
for i in range(2, n_fibo):
    fibo.append(fibo[i - 1] + fibo[i - 2])
print("Q6 피보나치:", fibo)

# 문제 8: 특정 문자 개수 세기
s = "aaabbc"
print("Q8 b의 개수:", s.count('b'))

# 문제 9: 가장 큰 수 찾기
rand_list = [3, 7, 2, 9, 1]
print("Q9 최댓값:", max(rand_list))

# 문제 13: 리스트 중복 값 제거
dup_list = [1, 2, 2, 3, 4, 4, 5]
print("Q13 중복 제거:", list(set(dup_list)))

# 문제 14: 리스트 요소 모두 곱하기
print("Q14 모두 곱하기:", math.prod(rand_list))

# =====================================================================
# 챕터 3. 1차원 리스트 맛있게 먹어보기
# [설명] 파이썬 리스트의 슬라이싱과 내장 함수를 자유자재로 다루는 훈련입니다.
# =====================================================================
print("\n--- [챕터 3. 1차원 리스트] ---")

# 문제 2: 최댓값과 최솟값의 차이를 2로 나눈 값
b = [5, 2, 8, 1, 9, 3, 7, 4, 6]
print("Q2 (최대-최소)/2 :", (max(b) - min(b)) / 2)

# 문제 3: 각 문자열의 길이 출력
c = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print("Q3 길이 리스트:", [len(x) for x in c])

# 문제 4: 음수인 값들의 합
d = [-1, 2, -3, 4, -5, 6]
print("Q4 음수 합:", sum(x for x in d if x < 0))

# 문제 5: 짝수 인덱스의 값들을 역순 정렬
e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Q5 짝수 인덱스 역순:", e[::2][::-1])  # [9, 7, 5, 3, 1]

# 문제 6: 각 문자열의 첫 글자와 마지막 글자
print("Q6 첫/마지막 글자:")
for word in c:
    print(word[0], word[-1])

# 문제 7: 양수인 값들의 평균
g = [5, -2, 8, 2, -3, 7, 1, -4, 6]
pos_g = [x for x in g if x > 0]
print("Q7 양수 평균:", sum(pos_g) / len(pos_g) if pos_g else "리스트에 양수가 없습니다.")

# 문제 8: 두 리스트의 교집합
list1, list2 = [1, 2, 3, 4, 5], [4, 5, 6, 7, 8]
print("Q8 교집합:", list(set(list1) & set(list2)))

# 문제 9: 주어진 구간 합 구하기 (인덱스 2부터 7까지)
print("Q9 구간 합:", sum(e[2:8]))

# =====================================================================
# 챕터 4. 2중 반복문을 맛있게 먹어보자 (패턴 및 별찍기)
# [설명] 2차원 공간 감각(행/열)을 기르기 위한 필수 훈련입니다.
# =====================================================================
print("\n--- [챕터 4. 2중 반복문 (별찍기 & 패턴)] ---")

n = 5
print("Q 별찍기 1 (직각 삼각형):")
for i in range(1, n + 1):
    print("*" * i)

print("Q 별찍기 3 (우측 정렬 삼각형):")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)

print("Q 별찍기 5 (피라미드):")
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

print("Q 숫자 8 (행과 열 지그재그 채우기 5x5):")
num = 1
for i in range(n):
    row_nums = [str(x) for x in range(num, num + n)]
    if i % 2 == 1:
        row_nums.reverse()  # 홀수 행은 역방향
    print(" ".join(row_nums))
    num += n

# =====================================================================
# 챕터 5. 2차원 리스트를 맛있게 먹어보자 (코테 핵심 Simulation)
# [설명] 정올/코테의 킬러 문항인 배열 돌리기, 썰기, 뒤집기입니다.
# =====================================================================
print("\n--- [챕터 5. 2차원 리스트 심화] ---")

matrix = [
    [10, 2, 3],
    [4, 50, 6],
    [7, 8, 900]
]

# 1. 2차원 리스트 각 열의 최댓값 (zip 활용)
print("Q1 각 열의 최댓값:", [max(col) for col in zip(*matrix)])  # [10, 50, 900]

# 2. 대각선(\ 방향) 요소의 합
diag_sum1 = sum(matrix[i][i] for i in range(len(matrix)))
print("Q2 대각선(\\) 합:", diag_sum1)

# 3. 대각선(/ 방향) 요소의 합
diag_sum2 = sum(matrix[i][len(matrix) - 1 - i] for i in range(len(matrix)))
print("Q3 대각선(/) 합:", diag_sum2)

# 4. 행렬 전치 (가로 세로 뒤집기)
transposed = list(map(list, zip(*matrix)))
print("Q4 전치 행렬:", transposed)

# 5. 90도 오른쪽 회전
rotated = list(map(list, zip(*matrix[::-1])))
print("Q5 90도 회전:", rotated)

# 6. 부분 행렬 합 (row1, col1) ~ (row2, col2)
# (예: (1, 1) 부터 (2, 2) 까지)
r1, c1, r2, c2 = 1, 1, 2, 2
sub_sum = sum(matrix[r][c] for r in range(r1, r2 + 1) for c in range(c1, c2 + 1))
print("Q6 부분 행렬 합:", sub_sum)

# 6-1. 2차원 맵 탐색의 절대 공식 (방향 벡터, 델타 탐색) ★★★
# 코테에서 상하좌우로 이동할 때 절대 if문 4개를 쓰지 마세요!
dx = [-1, 1, 0, 0]  # 행 이동 (상, 하)
dy = [0, 0, -1, 1]  # 열 이동 (좌, 우)
x, y = 1, 1  # 현재 위치 (1, 1)

print("Q6-1 (1,1)에서 상하좌우 이동 가능한 좌표:")
for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 맵을 벗어나는지 반드시 체크 (N=3 크기의 맵이라고 가정)
    if 0 <= nx < 3 and 0 <= ny < 3:
        print(f"이동 가능: ({nx}, {ny})")


# 7. 스파이럴(달팽이) 원소 출력 (가장 중요 ★)
def spiral_print(n):
    arr = [[0] * n for _ in range(n)]
    num = 1
    start_r, end_r, start_c, end_c = 0, n - 1, 0, n - 1

    while start_r <= end_r and start_c <= end_c:
        for i in range(start_c, end_c + 1):  # 우
            arr[start_r][i] = num;
            num += 1
        start_r += 1
        for i in range(start_r, end_r + 1):  # 하
            arr[i][end_c] = num;
            num += 1
        end_c -= 1
        if start_r <= end_r:
            for i in range(end_c, start_c - 1, -1):  # 좌
                arr[end_r][i] = num;
                num += 1
            end_r -= 1
        if start_c <= end_c:
            for i in range(end_r, start_r - 1, -1):  # 상
                arr[i][start_c] = num;
                num += 1
            start_c += 1
    return arr


print("Q7 달팽이 배열 (3x3):")
for row in spiral_print(3):
    print(" ".join(f"{x:2d}" for x in row))

# =====================================================================
# 챕터 6. 자료구조의 3대장 (Stack, Queue, Priority Queue)
# =====================================================================
print("\n--- [챕터 6. 스택, 큐, 우선순위 큐] ---")

# 1. 스택 (Stack)
# [정의] 나중에 들어간 게 먼저 나오는 구조 (LIFO: 프링글스 통)
# [WHY] 괄호 짝맞추기, 뒤로 가기, DFS 구현 등에 쓰입니다. 파이썬은 list가 스택입니다.
stack = []
stack.append(1);
stack.append(2)
print("Q1 스택 pop:", stack.pop())  # 가장 마지막에 넣은 2가 나옴

# 2. 큐 (Queue)
# [정의] 먼저 들어간 게 먼저 나오는 구조 (FIFO: 매표소 줄서기)
# [WHY] 대기열 처리, BFS(너비 우선 탐색)에 필수입니다. 무조건 deque를 써야 O(1)로 빠릅니다.
queue = deque([1, 2, 3])
queue.append(4)
print("Q2 큐 popleft:", queue.popleft())  # 가장 먼저 넣은 1이 나옴

# 3. 우선순위 큐 (Priority Queue / Heap)
# [정의] 들어간 순서 상관없이 '가장 작은(또는 큰) 값'이 먼저 나오는 마법의 주머니
# [WHY] 매번 최솟값을 찾기 위해 sort()를 쓰면 O(N log N)이지만, Heap은 O(log N)으로 압도적으로 빠릅니다. 다익스트라(최단경로)의 핵심입니다.
import heapq

pq = []
heapq.heappush(pq, 5)
heapq.heappush(pq, 1)
heapq.heappush(pq, 3)
print("Q3 우선순위 큐 (최솟값 팝):", heapq.heappop(pq))  # 1

# 3-1. 최대 힙 (Max-Heap) 구하기 팁 ★
# 파이썬의 heapq는 무조건 '가장 작은 값'만 나옵니다.
# 가장 큰 값을 뽑으려면 값을 넣을 때 마이너스(-)를 붙이고, 뺄 때 다시 마이너스(-)를 붙이세요.
max_pq = []
heapq.heappush(max_pq, -5)
heapq.heappush(max_pq, -1)
print("Q3-1 우선순위 큐 (최댓값 팝):", -heapq.heappop(max_pq))  # 5

# =====================================================================
# 챕터 7. 딕셔너리의 진화 (DefaultDict)
# =====================================================================
print("\n--- [챕터 7. DefaultDict] ---")

# [정의] 키(Key)가 없어도 에러(KeyError)를 내지 않고, 기본값을 알아서 세팅해 주는 딕셔너리.
# [WHY] 그래프의 연결 관계(인접 리스트)를 만들거나, 특정 조건의 데이터를 그룹화할 때 코드가 획기적으로 짧아집니다.
graph_dict = defaultdict(list)
graph_dict['A'].append('B')  # 'A'키가 없지만 에러 없이 빈 리스트를 만들고 'B'를 넣음
print("Q1 디폴트 딕셔너리:", dict(graph_dict))

# =====================================================================
# 챕터 8. 완전 탐색의 무기 (순열과 조합)
# =====================================================================
print("\n--- [챕터 8. 순열(Permutation) & 조합(Combination)] ---")

# [정의] 순열은 '순서를 신경 써서' 뽑는 경우의 수, 조합은 '순서 상관없이' 뽑는 경우의 수.
# [WHY] 10개 중 3개를 뽑아 비밀번호를 맞추는 등 '모든 경우의 수'를 다 해봐야 할 때(완전 탐색), 3중 4중 for문 대신 1줄로 끝냅니다.
items = ['A', 'B', 'C']

# 순열: A,B 와 B,A 는 다르다!
perms = list(itertools.permutations(items, 2))
print("Q1 순열 (2개 뽑기):", perms)

# 조합: A,B 와 B,A 는 같다! (순서 무관)
combs = list(itertools.combinations(items, 2))
print("Q2 조합 (2개 뽑기):", combs)

# =====================================================================
# 챕터 9. 탐색의 제왕 (이분 탐색 - Binary Search)
# =====================================================================
print("\n--- [챕터 9. 이분 탐색] ---")

# [정의] 정렬된 데이터에서 '업다운 게임'처럼 반씩 버려가며 값을 찾는 알고리즘.
# [WHY] 10억 개의 데이터에서 값을 찾을 때 for문(O(N))은 10억 번, 이분탐색(O(log N))은 단 30번 만에 찾습니다.
sorted_arr = [1, 3, 5, 7, 9, 11, 13]
target = 7


# 직접 구현하는 방법
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


print("Q1 이분 탐색 직접 구현 (인덱스 반환):", binary_search(sorted_arr, target))

# 내장 라이브러리 (bisect) 활용 - 코테의 치트키
# bisect_left: 값이 들어갈 수 있는 가장 왼쪽 인덱스 반환
import bisect

print("Q2 이분 탐색 내장 모듈 (인덱스 반환):", bisect.bisect_left(sorted_arr, target))

# =====================================================================
# 챕터 10. 그래프와 트리, 그리고 DFS/BFS
# =====================================================================
print("\n--- [챕터 10. 그래프, 트리, DFS, BFS] ---")

# [정의] 그래프: 정점(Node)과 간선(Edge)으로 연결된 네트워크. 트리는 '사이클(회전)이 없는' 그래프.
# DFS(깊이 우선 탐색): 한 놈만 패는 방식. 끝을 볼 때까지 깊게 들어감. (스택/재귀 사용)
# BFS(너비 우선 탐색): 주변부터 샅샅이 뒤지는 방식. 물결처럼 퍼져나감. (큐 사용)
# [WHY] 바이러스 확산, 미로 찾기, 최단 거리 구하기 등 코딩 테스트의 가장 핵심입니다.

# 그래프 표현 (인접 리스트 형태)
# 보통 노드 번호가 1번부터 시작하므로 인덱스 0은 비워둡니다.
graph_data = [
    [],
    [2, 3],  # 1번 노드와 연결된 노드들
    [1, 4, 5],  # 2번 노드와 연결된 노드들
    [1, 6],  # 3번 노드와 연결된 노드들
    [2],  # 4번
    [2],  # 5번
    [3]  # 6번
]


# DFS 구현 (재귀 함수)
# [경고] def dfs(v, visited=[]): 처럼 파라미터에 빈 리스트를 넣으면 절대 안 됩니다! (파이썬 안티 패턴)
def dfs(v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=" ")

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph_data[v]:
        if not visited[i]:  # O(1) 탐색
            dfs(i, visited)


# BFS 구현 (큐 사용)
def bfs(start, visited):
    q = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while q:
        v = q.popleft()
        print(v, end=" ")

        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph_data[v]:
            if not visited[i]:  # O(1) 탐색
                q.append(i)
                visited[i] = True  # ★ 큐에 넣을 때 방문 처리해야 중복 삽입을 막습니다.


print("Q1 DFS 탐색 순서: ", end="")
visited_dfs = [False] * 7  # 노드 개수(6) + 1
dfs(1, visited_dfs)

print("\nQ2 BFS 탐색 순서: ", end="")
visited_bfs = [False] * 7
bfs(1, visited_bfs)
print()

# =====================================================================
# 챕터 11. 알고리즘의 꽃 (동적 계획법 - DP)
# =====================================================================
print("\n--- [챕터 11. 동적 계획법 (DP)] ---")

# [정의] 복잡한 문제를 작은 문제로 나누어 풀고, 그 결과를 '기억(Memoization)'해 두었다가 재사용하는 기법.
# [WHY] 피보나치 수열을 그냥 재귀로 풀면 O(2^N)이 걸려 N=40만 되어도 컴퓨터가 터집니다. DP(배열에 저장)를 쓰면 O(N)으로 0.01초 만에 끝납니다.

# 문제: 피보나치 수열 10번째 값 구하기 (DP 테이블 작성)
dp = [0] * 100
dp[1] = 1
dp[2] = 1
n = 10

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]  # 이전 기억을 재활용

print(f"Q1 DP로 구한 피보나치 {n}번째 수:", dp[n])