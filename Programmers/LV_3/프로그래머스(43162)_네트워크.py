# Union - Find
# def get_parent(v, arr):
#     if arr[v] == v:
#         return v
#     else:
#         return get_parent(arr[v],arr)
#
# def union_parent(a, b, arr):
#     a = get_parent(a, arr)
#     b = get_parent(b, arr)
#     print(f"union_parent, a:{a}, b:{b}")
#     if a<b:
#         arr[b] = arr[a]
#     else:
#         arr[a] = arr[b]
#     print(arr)
#
# def find_parent(a,b, arr):
#     a = get_parent(a,arr)
#     b = get_parent(b,arr)
#     if a==b:
#         return 1
#     else:
#         return 0
#
# def solution(n, computers):
#     answer = 1
#     arr = []
#     for i in range(n):
#         arr.append(i)
#     print(f"arr1: {arr}")
#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 continue
#             elif computers[i][j] == 1:
#                 union_parent(i,j,arr)
#     print(f"arr2: {arr}")
#     ans = set()
#     for i in range(n):
#         ans.add(get_parent(i,arr))
#         print(ans, i, get_parent(i,arr))
#     return len(ans)
#
# n = 4
# computers = [
#     [1, 1, 0, 0],  # 0번과 1번만 연결
#     [1, 1, 0, 0],
#     [0, 0, 1, 1],  # 2번과 3번만 연결
#     [0, 0, 1, 1],
# ]
#
# print(solution(n, computers))


n = 4
computers = [
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 1]
]
# DFS
def solution(n, computers):
    answer = 0
    arr = [[] for i in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if computers[i][j] == 1:
                arr[i].append(j)
                arr[j].append(i)
    print(arr)


    def dfs(v,visited,arr):
        #방문 체크 코드
        if v not in visited:
            visited.append(v)
            print(f"append: {visited}")
        else:
            print(f"append else")

        for i in arr[v]:
            print(f"i: {i}")
            if i not in visited:
                visited = dfs(i,visited,arr)
        return visited

    visited = []
    count = 0
    for i in range(n): # 0, 1, 2, 4
        print(f"{i}, {visited}")
        # 방문하지 않은 컴퓨터
        if i not in visited:
            visited = dfs(i, visited, arr)
            count+=1


    return count

print(f"result {solution(n, computers)}")




# BFS
# from collections import deque
# def solution(n, computers):
#     answer = 0
#     arr = [[] for i in range(n)]
#     for i in range(n):
#         for j in range(i+1,n):
#             if computers[i][j] == 1:
#                 arr[i].append(j)
#                 arr[j].append(i)
#
#     def bfs(v, visited, arr):
#         queue = deque()
#         if v not in visited:
#             visited.append(v)
#             queue.append(v)
#         while queue:
#             target = queue.popleft()
#             for i in arr[target]:
#                 if i not in visited:
#                     queue.append(i)
#                     visited.append(i)
#         return visited
#     visited = []
#     for i in range(n):
#         if i not in visited:
#             visited = bfs(i, visited, arr)
#             answer+=1
#     return answer