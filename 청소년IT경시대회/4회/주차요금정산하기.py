"""
문제 이름:주차 요금 정산하기
출처: 한국정보기술진흥원 > 제4회 청소년 IT경시대회 > 초등부 1번
알고리즘 분류: 수학, 사칙연산
"""

def solve1():
    A, B, C = map(int, input().split())
    T = int(input())

    # 30분 이하로 주차
    if T <= 30:
        print(A)
    else:
        # 나누어 떨어지지 않음
        if (T-30)%B != 0:
            print(A + (((T-30)//B) + 1) *C)
        else:
            print(A + ((T-30)//B) *C)



if __name__ == "__main__":
    solve1()
