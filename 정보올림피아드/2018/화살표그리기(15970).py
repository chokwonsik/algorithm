# 화살표 그리기
# https://www.acmicpc.net/problem/15970
# 2018 초등부 2번

def solve1():
    """
    1) 색별 위치 모으기
    2) sort
    3) for/while로 diffs 생성 및 인접비교
    """
    import sys
    from collections import defaultdict
    input = sys.stdin.readline

    N = int(input().strip())
    buckets = defaultdict(list)
    for _ in range(N):
        pos, color = map(int, input().split())
        buckets[color].append(pos)

    total = 0
    for positions in buckets.values():
        positions.sort()
        length = len(positions)
        if length <= 1:
            continue

        # 인접 거리 구하기
        diffs = []
        idx = 0
        while idx < length - 1:
            diffs.append(positions[idx+1] - positions[idx])
            idx += 1

        # 맨 앞
        total += diffs[0]
        # 중간
        idx = 1
        while idx < length - 1:
            if diffs[idx-1] <= diffs[idx]:
                total += diffs[idx-1]
            else:
                total += diffs[idx]
            idx += 1
        # 맨 뒤
        total += diffs[-1]

    print(total)

def solve2():
    n = int(input())
    t = [[] for _ in range(n)]
    for i in range(n):
        a, b = map(int, input().split())
        t[b - 1].append(a)

    result = 0

    for i in t:
        i.sort()
        if len(i) > 2:
            for j in range(1, len(i) - 1):
                result += min(abs(i[j - 1] - i[j]), abs(i[j] - i[j + 1]))
            result += abs(i[0] - i[1])
            result += abs(i[-1] - i[-2])
        elif len(i) != 0:
            result += abs(i[0] - i[-1]) * 2
    print(result)


if __name__ == '__main__':
    solve1()
    #solve2()
