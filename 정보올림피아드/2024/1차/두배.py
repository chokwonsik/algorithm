def solve():
    "코드 작성"
    import sys, math
    input = sys.stdin.readline

    # 입력 처리
    n = int(input().strip())
    arr = list(map(int, input().split()))

    current = arr[0]
    total_ops = 0

    for i in range(1, n):
        value = arr[i]
        """
        문제풀이 설명:
        - 만약 현재 원소 'value'가 이전 값 'current'보다 크거나 같다면 변경 없이 진행.
        - 만약 value가 current보다 작다면, current/value의 비율을 log2로 계산해
          최소 두 배 연산 횟수 k를 구한다.
        - k번 두 배 연산을 적용하여 value를 업데이트하고 전체 연산 횟수에 더한다.
        """
        if value < current:
            ratio = current / value         # 두 배를 몇 번 해야 current 이상이 되는지 계산 위한 비율
            k = math.ceil(math.log2(ratio))   # 필요한 최소 두 배 연산 횟수 k 계산
            total_ops += k
            value *= (2 ** k)                 # k번 두 배 연산 후의 값
        current = value  # 다음 원소의 기준 업데이트

    # 결과 출력
    print(total_ops)

if __name__ == '__main__':
    solve()

"""
김이한
1. 31963 두배 
https://www.acmicpc.net/submit/31963/103816165
n = int(input())
cnt=[0]*n
l=list(map(int,input().split()))
for i in range(1,n):
    diff=0
    temp_prev = l[i-1]
    temp_curr = l[i]
    if temp_prev > temp_curr:
        while temp_prev > temp_curr:
            temp_curr *= 2
            diff += 1
    else: 
        # 100, 2, 4 
        # 100, 128, 128
        # 100, 128, 4 -> 16-> 32 (속도가 박살
        # 100, 2, 4 -> 1
        # 6-1 = 5
        # 지수만 계산 2^0, 2^6, 2^6
        while temp_prev * 2 <= temp_curr:
            temp_prev *= 2
            diff -= 1
    cnt[i] = max(0, cnt[i-1] + diff)
print(sum(cnt))
"""