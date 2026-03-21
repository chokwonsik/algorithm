"""
https://www.acmicpc.net/problem/34200
문제 이름: 장애물
출처: 2025 정보올림피아드 2차대화
알고리즘 분류: 수학, 그리디
"""


def solve1():
    """
    idx+2 값이 input에 없다면 점프
    있으면 걷기(idx+1
    """
    N = int(input())
    hurdle =set(map(int, input().split()))

    sorted_list = sorted(list(hurdle))
    for i in range(len(sorted_list) - 1):
        if sorted_list[i + 1] - sorted_list[i] == 1:
            print(-1)
            return 0

    idx = 0
    count = 0
    hurdle_end = max(hurdle)
    while idx < hurdle_end:
        if idx + 2 not in hurdle:
            idx += 2
        else:
            idx += 1
        count +=1
    print(count)

if __name__ == "__main__":
    solve1()
