def solution(quiz):
    answer = []
    for char in quiz:
        ev_data = char.split("=")
        if eval(ev_data[0]) == int(ev_data[1]):
            answer.append("O")
        else:
            answer.append("X")

    return answer