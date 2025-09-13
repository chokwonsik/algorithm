"""
[자신의 왼쪽에 있는 수 중 선택된 수의 개수]는 주어지는 자연수의 값들과는 관계 없이 k 값에 따라 일정하다.

그러므로 자연수들을 내림차순하여 정렬한 뒤, 큰 순서대로 k개의 수들을 선택하여 합한다.
이후 선택된 수의 개수를 빼주면 답이된다.
"""

n, k = map(int, input().split())
number = list(map(int, input().split()))  # 자연수 리스트 입력

# 리스트를 내림차순 정렬
number.sort(reverse=True)

# 점수 계산
# k개의 큰 수들(number[i]) - 선택된 수들의 개수(i)
sum_val = 0
for i in range(k):
    sum_val += number[i] - i

# 결과 출력
print(sum_val)