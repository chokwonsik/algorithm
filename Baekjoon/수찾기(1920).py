"""
https://www.acmicpc.net/problem/1920
문제 이름: 수찾기
출처: 백준
알고리즘 분류: set
핵심 접근: A 리스트를 set으로 변환하여 탐색 시간을 O(1)으로 단축시킨다.
set 자료구조는 내부적으로 해시 테이블로 구현되어 있어 특정 원소의 존재 여부를 매우 빠르게 확인할 수 있다.
"""
import sys

def solve():
    # 입력을 빠르게 받기 위한 설정
    input = sys.stdin.readline

    # N 입력
    N = int(input())
    # A를 list가 아닌 set으로 저장. 중복은 자동 제거되고, 탐색 속도가 엄청나게 빨라짐.
    A_set = set(map(int, input().split()))

    # M 입력
    M = int(input())
    # 찾아야 할 숫자들 입력
    targets = list(map(int, input().split()))

    # 각 target에 대해 반복
    for target in targets:
        # set에서 원소의 존재 여부 확인은 평균 시간 복잡도 O(1)
        if target in A_set:
            # 존재하면 1 출력
            print(1)
        else:
            # 존재하지 않으면 0 출력
            print(0)

if __name__ == "__main__":
    solve()