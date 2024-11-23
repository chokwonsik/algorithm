# 솔루션1
# def solution(data):
#     rules = ["aya", "ye", "woo", "ma"]  # 허용된 단어 목록이에요!
#     count = 0  # 규칙을 지킨 문자열의 개수를 셀 변수를 준비해요.
#
#     for s in data:  # 문자열 하나씩 검사해요.
#         current_index = 0  # 문자열에서 어디를 보고 있는지 나타내요.
#         last_word = ""  # 마지막으로 사용한 단어를 기억해요.
#         is_valid = True  # 이 문자열이 규칙을 지키는지 확인해요.
#
#         while current_index < len(s):  # 문자열 끝까지 검사해요.
#             found_match = False  # 단어를 찾았는지 확인해요.
#
#             for rule in rules:  # 규칙 단어 중 하나를 찾을 거예요.
#                 # 현재 위치에서 규칙 단어와 같다면
#                 if s[current_index:current_index + len(rule)] == rule:
#                     if last_word == rule:  # 마지막 단어와 같으면
#                         is_valid = False  # 연속된 단어 금지! 잘못된 문자열이에요.
#                         break  # 더 볼 필요 없어요.
#                     found_match = True  # 단어를 찾았어요!
#                     last_word = rule  # 이 단어를 마지막 단어로 기억해요.
#                     current_index += len(rule)  # 단어 길이만큼 다음으로 이동해요.
#                     break  # 다른 단어는 더 볼 필요 없어요.
#
#             if not found_match:  # 규칙 단어를 찾지 못했다면
#                 is_valid = False  # 규칙 위반! 잘못된 문자열이에요.
#                 break  # 더 볼 필요 없어요.
#
#         if is_valid:  # 규칙을 지켰다면
#             count += 1  # 유효한 문자열 개수를 하나 증가해요.
#
#     return count  # 조건을 만족한 문자열의 개수를 돌려줘요!

# 솔루션2
def solution(babbling):  # 함수 이름은 solution이고, 검사할 단어들의 목록을 받아요.
    answer = 0  # 규칙에 맞는 단어의 개수를 셀 변수를 준비해요.

    for i in babbling:  # 문자열 목록에서 하나씩 가져와서 검사해요.
        for j in ['aya', 'ye', 'woo', 'ma']:  # 규칙에 있는 네 가지 단어를 하나씩 확인해요.
            if j * 2 not in i:  # 같은 단어가 두 번 연속(`j*2`)으로 나오지 않았다면
                i = i.replace(j, ' ')  # 그 단어를 문자열에서 ' '으로 바꿔요.

        if len(i.strip()) == 0:  # 남아있는 글자가 없다면 (빈 문자열이라면)
            answer += 1  # 규칙에 맞는 단어니까 개수를 하나 더해요.

    return answer  # 규칙을 만족한 단어의 총 개수를 돌려줘요.