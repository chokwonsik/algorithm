"""
https://www.acmicpc.net/problem/17609
회문
"""

def solve1():
    def is_palindrome(s, left, right,c):
        #두 포인터로 s의 부분 문자열 [left, right]가 회문인지 확인
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    import sys
    input = sys.stdin.readline
    T = int(input().strip())
    for _ in range(T):
        s = input().strip()
        left, right = 0, len(s) - 1
        result = 0  # 기본값은 회문 (0)
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # 두 가지 경우를 체크: 왼쪽 문자를 건너뛴 경우, 오른쪽 문자를 건너뛴 경우
                if is_palindrome(s, left + 1, right,"L") or is_palindrome(s, left, right - 1,"R"):
                    result = 1  # 유사회문
                else:
                    result = 2  # 일반 문자열
                break  # 한 번 차이가 발생하면 판별 완료
        print(result)


def solve2():
    import sys
    input = sys.stdin.readline

    T = int(input().strip())
    for _ in range(T):
        s = input().strip()
        left, right = 0, len(s) - 1
        result = 0  # 기본값은 회문 (0)

        # 두 포인터를 이용해 문자열의 양 끝부터 비교
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # 왼쪽 문자를 제거한 경우의 부분 문자열
                left_removed = s[left + 1:right + 1]
                # 오른쪽 문자를 제거한 경우의 부분 문자열
                right_removed = s[left:right]

                # 두 경우 중 하나라도 회문이면 유사회문
                if left_removed == left_removed[::-1] or right_removed == right_removed[::-1]:
                    result = 1  # 유사회문
                else:
                    result = 2  # 일반 문자열 (회문도 유사회문도 아님)
                break  # 한 번 불일치가 발생하면 더 이상 반복할 필요 없음

        print(result)


def solve3():
    #시간초과가 발생하는 이유는?
    import sys, copy
    input = sys.stdin.readline

    T = int(input().strip())
    for _ in range(T):
        origin_str = input().strip()
        reverse_str = origin_str[::-1]
        if origin_str == reverse_str:
            print(0)
            continue

        loop_count = len(origin_str)//2
        if len(origin_str)%2==1:
            loop_count +=1

        for i in range(loop_count):
            if origin_str[:i]+origin_str[i+1:] == (origin_str[:i]+origin_str[i+1:])[::-1]:
                break
            if reverse_str[:i]+reverse_str[i+1:] == (reverse_str[:i]+reverse_str[i+1:])[::-1]:
                break
        else:
            print(2)

if __name__ == '__main__':
    solve1()
    #solve2()
    #solve3()
