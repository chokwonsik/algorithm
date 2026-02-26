# 문제 설명:
# KOI 마을에 N개의 집이 있고, 각 집의 위치는 (X, Y) 좌표로 주어진다.
# 두 집 사이의 거리는 맨해튼 거리로 정의되며, 이는 두 좌표의 x좌표 차이와 y좌표 차이의 합이다.
# 재난 발생 시 주민들이 대피할 수 있도록 K개의 집에 대피소를 설치할 계획이다.
# 대피소가 설치되지 않은 각 집은 가장 가까운 대피소까지 이동해야 한다.
# 우리의 목표는, 대피소로부터 각 집까지의 이동 거리가 모두 가능한 한 짧아지도록,
# "집에서 가장 가까운 대피소까지의 거리 중 가장 긴 값(최악의 거리)"가 최소가 되는 대피소 배치를 찾는 것이다.
#
# 입력:
# 첫 번째 줄에는 집의 개수 N과 대피소로 설치할 집의 개수 K가 주어진다.
# 다음 N개의 줄에는 각 집의 좌표 (X, Y)가 공백으로 구분되어 주어진다.
#
# 출력:
# 모든 가능한 대피소 배치 중에서, 집에서 가장 가까운 대피소까지의 거리 중
# 가장 먼 값(최악의 거리)이 최소가 되는 값을 출력한다.
#
# 제한:
# 1 ≤ K ≤ 3, K ≤ N ≤ 50, 0 ≤ X, Y ≤ 100,000
# 모든 집의 좌표는 서로 다르다.
#
# 문제 해결 아이디어:
# 1. 모든 집 중에서 K개의 집을 대피소로 선택하는 모든 경우(조합)를 탐색한다.
# 2. 각 조합마다 대피소가 아닌 집들에 대해, 해당 집과 가장 가까운 대피소까지의 거리를 계산한다.
# 3. 그 거리들 중 가장 긴 거리(최악의 거리)를 구한다.
# 4. 모든 조합에 대해 최악의 거리의 최솟값을 찾으면, 그것이 문제에서 요구하는 답이다.
#
# 시간 복잡도:
# K가 최대 3, N이 최대 50이므로 가능한 조합 수는 C(50, 3) = 19600 이하이다.
# 각 조합마다 거리를 계산하는 작업은 충분히 빠르게 처리 가능하다.

from itertools import combinations  # 여러 집에서 K개의 집을 고르는 조합을 구하기 위해 itertools의 combinations 함수 사용

def manhattan(a, b):
    # 두 점 a와 b 사이의 맨해튼 거리를 계산하는 함수
    # a와 b는 (x, y) 형태의 튜플이며, 맨해튼 거리는 |x1 - x2| + |y1 - y2|로 구함
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# 입력 받기:
# 첫 번째 줄에서 집의 개수 N과 대피소로 선택할 집의 개수 K를 입력받는다.
N, K = map(int, input().split())  # 예를 들어, "5 2"를 입력받으면 N = 5, K = 2

# 집들의 좌표를 저장할 집합(set)을 생성
# 집합을 사용하면 중복 없이 각 집의 좌표를 저장할 수 있음 (문제 조건에 따라 좌표는 모두 다름)
home = set()
for i in range(N):
    # 각 줄에 입력되는 좌표를 공백으로 분리한 후, 정수로 변환하여 튜플 형태로 home 집합에 추가
    home.add(tuple(map(int, input().split())))

# result 변수는 모든 조합 중 "최악의 거리"의 최소값을 저장할 변수로, 초기값을 무한대로 설정
result = float('inf')

# 모든 가능한 대피소 배치를 탐색:
# home 집합에서 K개의 집을 대피소로 선택하는 모든 조합을 반복문을 통해 확인
for shelter_combo in combinations(home, K):

    selected = set(shelter_combo)
    not_selected = home - selected

    worst_list = []
    # 모든 대피소가 아닌 집에 대해 반복하면서, 해당 집과 가장 가까운 대피소 사이의 거리를 계산
    for point in not_selected:

        distances = []
        for shelter in selected:
            distances.append(manhattan(point, shelter))
        current_min = min(distances)
        worst_list.append(current_min)

    # 현재 조합의 "최악의 거리"는 모든 대피소가 아닌 집들 중 가장 먼 (즉, 가장 큰 최소 거리) 값이다.
    if worst_list:
        worst = max(worst_list)
    else:
        # 만약 모든 집이 대피소로 선택된 경우 (즉, not_selected가 빈 집합이면),
        # 모든 집이 대피소이므로 이동해야 할 거리가 없으므로 worst는 0이다.
        worst = 0

    # 현재 조합의 최악의 거리가 지금까지의 result보다 작으면 result를 업데이트한다.
    if worst < result:
        result = worst

# 최종 결과 출력:
# result에는 모든 조합 중 최악의 거리(집에서 가장 가까운 대피소까지의 거리 중 가장 긴 값)의 최소값이 저장되어 있다.
print(result)
