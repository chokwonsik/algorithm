"""
https://www.acmicpc.net/problem/11399
문제 이름: ATM
출처:
알고리즘 분류: 그리디, 정렬
"""


def solve1():
    N = input()
    result = 0
    num_sum = 0
    people = list(map(int, input().split()))
    people.sort()
    for i in people:
        num_sum += i
        result += num_sum

    print(result)
if __name__ == "__main__":
    solve1()
