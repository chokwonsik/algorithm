def solution(n):
    # n x n 크기의 나선형 배열 초기화
    spiral_array = [[_ for _ in range(n)] for _ in range(n)]

    num = 1  # 배열에 채울 숫자
    start_row, end_row = 0, n - 1  # 행의 시작과 끝 인덱스
    start_col, end_col = 0, n - 1  # 열의 시작과 끝 인덱스

    while start_row <= end_row and start_col <= end_col:
        # 1. 오른쪽으로 이동
        for i in range(start_col, end_col + 1):
            spiral_array[start_row][i] = num
            num += 1
        start_row += 1  # 다음 행으로 이동

        # 2. 아래쪽으로 이동
        for i in range(start_row, end_row + 1):
            spiral_array[i][end_col] = num
            num += 1
        end_col -= 1  # 다음 열로 이동

        # 3. 왼쪽으로 이동 (유효한 경우에만)
        if start_row <= end_row:
            for i in range(end_col, start_col - 1, -1):
                spiral_array[end_row][i] = num
                num += 1
            end_row -= 1  # 다음 행으로 이동

        # 4. 위쪽으로 이동 (유효한 경우에만)
        if start_col <= end_col:
            for i in range(end_row, start_row - 1, -1):
                spiral_array[i][start_col] = num
                num += 1
            start_col += 1  # 다음 열로 이동

    return spiral_array
