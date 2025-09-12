# 종이 접기
# https://www.acmicpc.net/problem/20187
def row_changer(row, direction):
    """
    각 행의 구멍 번호를 접힘 방향에 따라 변환하는 함수.
    좌우 접기의 경우: 0→1, 1→0, 2→3, 3→2
    상하 접기의 경우: 0→2, 1→3, 2→0, 3→1
    """
    if direction in ['L', 'R']:
        mapping = {0: 1, 1: 0, 2: 3, 3: 2}
    else:  # 'U' 또는 'D'
        mapping = {0: 2, 1: 3, 2: 0, 3: 1}
    return [mapping[num] for num in row]

def solve1():
    # 입력 받기
    k = int(input())
    folds = input().split()
    hole = int(input())

    # 접은 순서를 역순으로 만들어 unfold 순서로 진행
    folds.reverse()

    # 초기 1×1 격자 (구멍 번호 포함)
    result = [[hole]]

    # unfold 단계: 각 접기 방향에 따라 종이를 펼치기
    for direction in folds:
        if direction == 'R':
            # 오른쪽 접기: 왼쪽에, row_changer 적용 후 열 순서를 뒤집어 붙임
            result = [row_changer(row, 'R')[::-1] + row for row in result]
        elif direction == 'L':
            # 왼쪽 접기: 오른쪽에, row_changer 적용 후 열 순서를 뒤집어 붙임
            result = [row + row_changer(row, 'L')[::-1] for row in result]
        elif direction == 'U':
            # 위쪽 접기: 현재 격자의 행 순서를 뒤집은 후, 각 행에 row_changer('U') 적용하여 밑에 붙임
            result = result + [row_changer(row, 'U') for row in reversed(result)]
        elif direction == 'D':
            # 아래쪽 접기: 현재 격자의 행 순서를 뒤집은 후, 각 행에 row_changer('D') 적용하여 위에 붙임
            result = [row_changer(row, 'D') for row in reversed(result)] + result

    # 최종 결과 출력
    for row in result:
        print(*row)


def solve2():
    """
    종이접기 문제 리스트 기반 풀이
    초기 1×1 격자에서 시작하여, 접은 순서의 역순으로 unfolding 함.
    각 unfold 단계에서 접힘 방향에 따라 구멍 번호가 바뀌고,
    최종적으로 2^k × 2^k 격자에 뚫린 구멍 번호를 출력한다.
    """
    import sys
    input = sys.stdin.readline

    # 입력 받기: k, 접기 순서, 그리고 구멍 번호
    k = int(input())
    folds = input().split()
    hole = int(input())

    # 역순으로 unfolding 진행 (마지막에 접은 것이 처음 펼쳐짐)
    folds.reverse()

    # 초기 1×1 격자 생성
    grid = [[hole]]

    # unfolding 단계: 접기 방향에 따라 격자 확장
    for d in folds:
        new_grid = []
        if d == 'R':
            # 오른쪽 접기:
            # 각 행에서: 왼쪽 부분 = 행을 변환한 후 좌우 반전, 오른쪽 부분 = 기존 행
            for row in grid:
                new_row = row_changer(row, 'R')[::-1] + row
                new_grid.append(new_row)
            grid = new_grid
        elif d == 'L':
            # 왼쪽 접기:
            # 각 행에서: 왼쪽 부분 = 기존 행, 오른쪽 부분 = 행을 변환한 후 좌우 반전
            for row in grid:
                new_row = row + row_changer(row, 'L')[::-1]
                new_grid.append(new_row)
            grid = new_grid
        elif d == 'U':
            # 위쪽 접기:
            # 아래 부분 = 기존 격자의 행 순서를 뒤집은 후 각 행 변환, 위쪽에 기존 격자 유지
            lower = []
            for row in reversed(grid):
                lower.append(row_changer(row, 'U'))
            grid = grid + lower
        elif d == 'D':
            # 아래쪽 접기:
            # 위쪽 부분 = 기존 격자의 행 순서를 뒤집은 후 각 행 변환, 아래쪽에 기존 격자 유지
            upper = []
            for row in reversed(grid):
                upper.append(row_changer(row, 'D'))
            grid = upper + grid

    # 최종 격자 출력: 각 행의 숫자를 공백으로 구분하여 출력
    for row in grid:
        print(*row)


if __name__ == '__main__':
    solve1()
    #solve2()
