"""

문제 이름:
출처:
알고리즘 분류:
"""


def solve1():
    # +, 0, -
    N = int(input())
    U = list(map(int, input().split()))
    D = list(map(int, input().split()))
    result = []
    money = 0
    for i in D:
        if i != -1:
            money += i

    for idx, j in enumerate(U):
        print(idx, j)
        if j != -1:
            #업글 가능
            if j <= money-D[idx]:
                money -= j
                money -= D[idx]
                result.append("+")
            else:
                result.append("-")
        else:
            result.append(0)
    print(result)


if __name__ == "__main__":
    solve1()
