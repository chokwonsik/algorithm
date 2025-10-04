#1
def solution(participant, completion):
    participant.sort()  # 참가자 이름 정렬
    completion.sort()  # 완주자 이름 정렬

    for i in range(len(completion)):  # 완주자 명단 길이만큼 반복
        if participant[i] != completion[i]:  # 두 이름이 다르면
            return participant[i]  # 완주하지 못한 사람 발견
    return participant[-1]  # 마지막 남은 참가자 반환

#2
import collections
def solution(participant, completion):
    counts = collections.Counter(participant)  # 참가자 이름 개수 세기
    for name in completion:
        counts[name] -= 1  # 완주자의 이름 개수 줄이기

    for name, count in counts.items():  # 남은 이름 중 개수가 1인 사람 찾기
        if count > 0:
            return name

#3
def solution(participant, completion):
    counts = {}  # 참가자의 이름과 개수를 저장
    for name in participant:
        counts[name] = counts.get(name, 0) + 1  # 참가자의 이름 개수 세기

    for name in completion:
        counts[name] -= 1  # 완주자의 이름 개수 줄이기

    for name, count in counts.items():  # 남은 이름 중 개수가 1인 사람 찾기
        if count > 0:
            return name
