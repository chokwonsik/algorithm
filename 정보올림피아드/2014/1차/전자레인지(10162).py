"""
https://www.acmicpc.net/problem/10162
문제 이름: 전자레인지
출처: 정보올림피아드/2014/초등부 1번
알고리즘 분류: 수학, 구현, 그리디
"""


def solve1():
    t = int(input())
    a, b, c = 300, 60, 10
    x = t // a
    t %= a
    y = t // b
    t %= b
    z = t // c
    t %= c
    if t != 0:
        print(-1)
    else:
        print(x, y, z)


if __name__ == "__main__":
    solve1()
