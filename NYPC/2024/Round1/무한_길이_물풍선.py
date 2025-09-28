"""
https://www.biko.kr/problem/4688
문제 이름:무한 길이 물풍선
출처: NYPC 2024 Round1 2번
알고리즘 분류:
"""


def solve1():
    from collections import defaultdict
    N = int(input())
    x_pos = defaultdict(int)
    y_pos = defaultdict(int)
    for i in range(N):
        x, y = map(int, input().split())
        x_pos[x] += + 1
        y_pos[y] += + 1
    count = sum(1 for v in x_pos.values() if v >= 2)
    count += sum(1 for v in y_pos.values() if v >= 2)
    print(count)

if __name__ == "__main__":
    solve1()
