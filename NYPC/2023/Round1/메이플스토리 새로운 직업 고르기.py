"""

문제 이름:
출처:
알고리즘 분류:
"""


def solve1():
    N = int(input())
    a_set = set(input() for _ in range(N))

    K = int(input())
    k_set = set(input() for _ in range(K))

    result = a_set - k_set

    print(len(result))
    print(' '.join(result))


if __name__ == "__main__":
    solve1()

"""
2
Hero
Paladin
1
Hero
"""