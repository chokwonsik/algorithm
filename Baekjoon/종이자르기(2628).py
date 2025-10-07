"""
https://www.acmicpc.net/problem/2628
문제 이름: 종이자르기
출처: KOI 2002 초등부 1번
알고리즘 분류: 구현, 정렬
"""


# 문제: 종이자르기 (백준 2628)
# 접근 방식:
# 1. 가로로 자르는 점선과 세로로 자르는 점선을 각각 다른 리스트에 저장한다.
# 2. 각 리스트에 종이의 경계선(0과 전체 길이)을 추가한다. (이게 핵심!)
# 3. 두 리스트를 각각 오름차순으로 정렬한다.
# 4. 정렬된 리스트에서 인접한 원소들의 차이(잘린 조각의 길이)를 계산하여 최댓값을 찾는다.
# 5. 가로 조각 최댓값과 세로 조각 최댓값을 곱하여 최종 넓이를 구한다.

def solve():
    # 1. 입력 받기
    width, height = map(int, input().split())
    num_cuts = int(input())

    # 가로/세로 점선 위치를 저장할 리스트
    # 꿀팁: 처음부터 경계선을 넣어두면 코드가 깔끔해져!
    horizontal_cuts = [0, height]
    vertical_cuts = [0, width]

    for _ in range(num_cuts):
        cut_type, cut_pos = map(int, input().split())
        if cut_type == 0: # 0이면 가로로 자르는 점선
            horizontal_cuts.append(cut_pos)
        else: # 1이면 세로로 자르는 점선
            vertical_cuts.append(cut_pos)

    # 2. 정렬하기
    horizontal_cuts.sort()
    vertical_cuts.sort()

    # 3. 최대 길이 찾기
    max_height = 0
    for i in range(1, len(horizontal_cuts)):
        # 현재 점선 위치 - 이전 점선 위치 = 조각의 높이
        h = horizontal_cuts[i] - horizontal_cuts[i-1]
        max_height = max(max_height, h)

    max_width = 0
    for i in range(1, len(vertical_cuts)):
        # 현재 점선 위치 - 이전 점선 위치 = 조각의 너비
        w = vertical_cuts[i] - vertical_cuts[i-1]
        max_width = max(max_width, w)

    # 4. 최종 넓이 출력
    print(max_width * max_height)


if __name__ == "__main__":
    solve()
