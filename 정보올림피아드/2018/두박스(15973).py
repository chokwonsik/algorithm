"""
https://www.acmicpc.net/problem/15973
문제 이름: 두 박스
출처: 정보올림피아드, 2018, 중등부 1번
알고리즘 분류: 수학, 기하학, 많은 조건 분기
"""

def solve1():
    """
    1) NULL: 완전 분리
    2) POINT: 꼭짓점 한 점만 만남
    3) LINE: 한 변(선분)에서 만남
    4) FACE: 내부 면적으로 겹침
    """
    # 박스 A 좌표
    ax1, ay1, ax2, ay2 = map(int, input().split())
    # 박스 B 좌표
    bx1, by1, bx2, by2 = map(int, input().split())

    # 1) NULL: 가로나 세로 중 하나라도 완전 분리될 때
    if ax2 < bx1 or bx2 < ax1 or ay2 < by1 or by2 < ay1:
        print("NULL")
        return

    # 2) POINT: x축 경계와 y축 경계가 둘 다 딱 붙을 때
    if (ax2 == bx1 or bx2 == ax1) and (ay2 == by1 or by2 == ay1):
        print("POINT")
        return

    # 3) LINE: 한 변(선분)에서 만남
    #   3-1) 세로 선분 만남: x가 딱 붙고, y 구간이 실제로 겹쳐야 함
    if (ax2 == bx1 or bx2 == ax1) and max(ay1, by1) < min(ay2, by2):
        print("LINE")
        return
    #   3-2) 가로 선분 만남: y가 딱 붙고, x 구간이 실제로 겹쳐야 함
    if (ay2 == by1 or by2 == ay1) and max(ax1, bx1) < min(ax2, bx2):
        print("LINE")
        return

    # 4) FACE: 나머지 경우 (내부 면적 겹침)
    print("FACE")

def solve2():
    f_rec = list(map(int, input().split()))
    s_rec = list(map(int, input().split()))
    x_point = [(f_rec[0], f_rec[2]), (s_rec[0], s_rec[2])]
    y_point = [(f_rec[1], f_rec[3]), (s_rec[1], s_rec[3])]
    x_point.sort()
    y_point.sort()
    if x_point[0][1] == x_point[1][0] and y_point[0][1] == y_point[1][0]:
        print("POINT")
    elif x_point[0][1] == x_point[1][0] and y_point[0][1] > y_point[1][0]:
        print("LINE")
    elif y_point[0][1] == y_point[1][0] and x_point[0][1] > x_point[1][0]:
        print("LINE")
    elif x_point[0][1] > x_point[1][0] and y_point[0][1] > y_point[1][0]:
        print("FACE")
    else:
        print("NULL")

if __name__ == '__main__':
    #solve1()
    solve2()

