from itertools import combinations
import math


def count_good_triplets(N, C, points):
    # 중복된 점 제거 (set을 사용하여 중복 제거 후 정렬)
    unique_points = sorted(set(points))
    N = len(unique_points)  # 중복 제거된 점 개수

    # 각 점을 각도로 변환 (원의 중심 기준)
    angles = [(2 * math.pi * p / C) for p in unique_points]

    def ccw(x1, y1, x2, y2, x3, y3):
        # 세 점이 CCW(반시계 방향)인지 확인
        return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1) > 0

    def is_origin_inside(p1, p2, p3):
        # 원점(0, 0)이 삼각형 내부에 포함되는지 확인
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        ccw1 = ccw(0, 0, x1, y1, x2, y2)
        ccw2 = ccw(0, 0, x2, y2, x3, y3)
        ccw3 = ccw(0, 0, x3, y3, x1, y1)
        return ccw1 == ccw2 == ccw3

    def polar_to_cartesian(angle):
        # 각도를 직교 좌표로 변환
        return (math.cos(angle), math.sin(angle))

    # 각도를 직교 좌표로 변환하여 저장
    cartesian_points = [polar_to_cartesian(angle) for angle in angles]

    # 가능한 조합 중 조건에 맞는 triplet 수 계산
    count = 0
    for a, b, c in combinations(range(N), 3):
        if is_origin_inside(cartesian_points[a], cartesian_points[b], cartesian_points[c]):
            count += 1

    return count


# 예제 입력
N = 8
C = 10
points = [0, 2, 5, 5, 6, 9, 9, 0]

# 결과 출력
result = count_good_triplets(N, C, points)
print(result)
