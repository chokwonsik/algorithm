# 솔루션 1
# from collections import deque
# def solution(maps):
#     # 상하좌우 이동을 위한 좌표 변화 설정
#     directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

#     # 맵 크기 계산
#     rows, cols = len(maps), len(maps[0])

#     # BFS 함수 정의
#     def bfs():
#         queue = deque([(0, 0, 1)])  # 시작점 (x, y, 거리)
#         visited = [[False] * cols for _ in range(rows)]  # 방문한 곳을 기록할 맵
#         visited[0][0] = True  # 시작점 방문 처리

#         while queue:
#             x, y, distance = queue.popleft()

#             # 도착점(오른쪽 아래)에 도착하면 경로 반환
#             if x == rows - 1 and y == cols - 1:
#                 return distance

#             # 상하좌우 이동
#             for dx, dy in directions:
#                 nx, ny = x + dx, y + dy

#                 # 유효한 좌표인지 확인 (맵 범위 내에 있고, 벽이 아니며, 방문하지 않은 곳)
#                 if 0 <= nx < rows and 0 <= ny < cols and maps[nx][ny] == 1 and not visited[nx][ny]:
#                     visited[nx][ny] = True  # 방문 처리
#                     queue.append((nx, ny, distance + 1))  # 큐에 새로운 좌표와 거리 추가

#         return -1  # 도착할 수 없는 경우 -1 반환

#     # BFS 실행하여 결과 반환
#     return bfs()

# 솔루션2
from collections import deque


def solution(maps):
    x_move = [1, 0, -1, 0]
    y_move = [0, 1, 0, -1]

    x_h, y_h = (len(maps[0]), len(maps))
    queue = deque([(0, 0, 1)])

    while queue:
        x, y, d = queue.popleft()

        for i in range(4):
            nx = x + x_move[i]
            ny = y + y_move[i]

            if nx > -1 and ny > -1 and nx < x_h and ny < y_h:
                if maps[ny][nx] == 1 or maps[ny][nx] > d + 1:
                    maps[ny][nx] = d + 1
                    if nx == x_h - 1 and ny == y_h - 1:
                        return d + 1

                    queue.append((nx, ny, d + 1))

    return -1