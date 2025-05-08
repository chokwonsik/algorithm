# 도화지의 크기를 100x100으로 초기화
paper = [[0] * 5 for _ in range(5)]

# 색종이의 수 입력 받기
n = int(input())

# 색종이 붙이기
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 2): #x 이동 -> 세로라인 1칸 점프 -> 아래로 1칸
        for j in range(y, y + 2): #y 이동 -> 가로라인 1칸 점프 -> 우측으로 1칸
            print(i,j)
            paper[i][j] = 1
            for k in paper:
                print(k)
            print("---------------")

# 검은 영역의 넓이 계산
black_area = 0
for i in range(5):
    for j in range(5):
        if paper[i][j] == 1:
            black_area += 1

# 결과 출력
print(black_area)