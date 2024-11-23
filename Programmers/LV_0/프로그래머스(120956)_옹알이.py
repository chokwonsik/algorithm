# 솔루션1
# from itertools import permutations
# from collections import Counter
#
# def solution(babbling):
#     # 옹알이 가능한 범위를 초과한 경우는 제외
#     babbling = [item for item in babbling if len(item) < 11]
#
#     # 옹알이 목록
#     speak = ["aya", "ye", "woo", "ma"]
#
#     speak_permutations = []
#     # 옹알이 가능한 리스트 생성
#     for i in range(1, 5):
#         for item in permutations(speak, i):
#             speak_permutations.append("".join(item))
#
#     # babbling의 개수를 카운트(왜? 중복데이터를 효율적으로 처리하기 위함)
#     # babbling 데이터의 개수가 100개이고, 모두 동일한 값이라면?
#     babbling_count = Counter(babbling)
#
#     # speak_permutations의 아이템을 순회하면서 babbling_count에 있는지 확인
#     result = 0
#     for item in speak_permutations:
#         if item in babbling_count:
#             result += babbling_count[item]
#
#     return result

# 솔루션2
import re

def solution(babbling):
    regex = re.compile('^(aya|ye|woo|ma)+$')
    print(regex)
    cnt=0
    for e in babbling:
        if regex.match(e):
            cnt+=1
    return cnt