"""
https://www.acmicpc.net/problem/25381
ABBC
2022 1차대회, 고등부 2번
"""
def solve1(S):
    from collections import Counter
    #S = input()

    abc_count = list(Counter(S).values())
    print(abc_count)
    # 1차 0 제거
    for idx,value in enumerate(abc_count):
        if value == 0:
            abc_count.pop(idx)
    min1 = min(abc_count)
    for i in range(len(abc_count)):
        abc_count[i] -= abc_count[i] - min1



    result = 0

if __name__ == '__main__':
    solve1('ABCBA')