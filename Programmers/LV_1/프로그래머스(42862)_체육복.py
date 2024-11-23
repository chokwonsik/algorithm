def solution(n, lost, reserve):
    # 중복된 값을 제거한 lost와 reserve 리스트
    lost_set = list(set(lost) - set(reserve))
    reserve_set = list(set(reserve) - set(lost))
    for i in lost_set:
        # 첫 번째 학생과 마지막 학생의 경우 따로 처리
        if i == 1:
            if (i + 1) in reserve_set:
                reserve_set.remove(i + 1)
            else:
                n -= 1
        elif i == 30:
            if (i - 1) in reserve_set:
                reserve_set.remove(i - 1)
            else:
                n -= 1
        else:
            # 일반적인 경우
            if (i - 1) in reserve_set:
                reserve_set.remove(i - 1)
            elif (i + 1) in reserve_set:
                reserve_set.remove(i + 1)
            else:
                n -= 1

    return n


# #도난 학생이 여벌옷을 빌려 줄 친구 찾기(마음이 급함..)
# def solution(n, lost, reserve):
#     # 중복된 값을 제거한 lost와 reserve 리스트
#     lost_set = sorted(set(lost) - set(reserve))
#     reserve_set = sorted(set(reserve) - set(lost))

#     # 체육복을 빌려 줄 수 잇는 사람 찾기
#     for l in lost_set:
#         if l - 1 in reserve_set:
#             reserve_set.remove(l - 1)
#         elif l + 1 in reserve_set:
#             reserve_set.remove(l + 1)
#         else:
#             n -= 1

#     # 최종적으로 체육복을 잃어버린 학생 수
#     return n


# 여벌옷이 있는 학생이 도난당한 친구 찾기 (착한 아이)
# 잃어버린 아이들의 목록을 제거하기
# def solution(n, lost, reserve):
#     # 중복된 값을 제거한 lost와 reserve 리스트
#     lost_set = sorted(set(lost) - set(reserve))
#     reserve_set = sorted(set(reserve) - set(lost))

#     # 각 학생의 체육복을 빌려주는 로직
#     for r in reserve_set:
#         if r - 1 in lost_set:
#             lost_set.remove(r - 1)
#         elif r + 1 in lost_set:
#             lost_set.remove(r + 1)

#     # 전체 학생수 - 체육복을 잃어버린 학생 수 -> 수업 들을 수 있는 학생의 수
#     return n  - len(lost_set)
"""
3, 2, 4
4, 5, 6
"""

"""
체육복을 빌려 주려고 하는데, 양옆에 잃어 버린 사람이 없는 경우 -> 빌려줄 사람이 없음
잃어 버린 사람 양 옆에 체육복을 빌려줄 사람이 없는 경우      -> 빌릴 사람이 없음, n -= 1
"""
