def solution(code):
    answer = []
    mode = False  # 처음에는 mode가 False로 시작 (mode 0)

    for idx, char in enumerate(code):
        if char == "1":  # 현재 문자가 "1"이면 mode를 전환
            mode = not mode
        else:
            if mode:  # mode 1일 때
                if idx % 2 == 1:  # 홀수 인덱스일 때만 추가
                    answer.append(char)
            else:  # mode 0일 때
                if idx % 2 == 0:  # 짝수 인덱스일 때만 추가
                    answer.append(char)

    # answer가 비어있으면 "EMPTY", 아니면 리스트를 문자열로 변환하여 반환
    return ''.join(answer) if answer else "EMPTY"
