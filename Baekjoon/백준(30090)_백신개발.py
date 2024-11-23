from itertools import permutations
# 두 문자열의 겹치는 부분을 찾아 병합하는 함수
def merge_strings(a, b):
    max_overlap = 0
    for k in range(1, min(len(a), len(b)) + 1):
        print((a[-k:], b[:k]))
        if a[-k:] == b[:k]:
            max_overlap = k
    return a + b[max_overlap:]

# # 입력 받기
n = int(input())
strings = [input() for _ in range(n)]

# 가능한 모든 순열에 대해 처리
min_length = float('inf')
for perm in permutations(strings):
    merged_string = perm[0]
    for i in range(1, n):
        merged_string = merge_strings(merged_string, perm[i])
        print(merged_string)
    min_length = min(min_length, len(merged_string))

# 결과 출력
print(min_length)

print(list(permutations(strings)))