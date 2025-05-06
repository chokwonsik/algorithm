"""
https://www.acmicpc.net/problem/15969
문제 이름: 행복
출처: 정보올림피아드, 2018, 초등부, 1번
알고리즘 분류: 수학, 구현, 사칙연산
"""

def solve():
    N = int(input())
    score = list(map(int, input().split()))
    print(max(score) - min(score))




if __name__ == '__main__':
    solve()