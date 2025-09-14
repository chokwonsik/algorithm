# 햄버거 분배
# https://www.acmicpc.net/problem/19941

def solve1():
    import sys
    input = sys.stdin.readline

    # 입력: N은 벤치 길이, K는 햄버거 도달 가능 거리
    N, K = map(int, input().split())
    bench = list(input().strip())  # 벤치를 리스트로 변환

    count = 0  # 햄버거를 먹은 사람 수

    # 벤치의 모든 위치를 순회
    for i in range(N):
        if bench[i] == 'P':  # 사람이 있으면
            # 사람 i가 도달할 수 있는 범위: max(i-K, 0) 부터 min(i+K, N-1)
            start = max(i - K, 0)
            end = min(i + K, N - 1)
            # 해당 범위에서 햄버거('H') 찾기
            for j in range(start, end + 1):
                if bench[j] == 'H':
                    count += 1  # 햄버거 먹음
                    bench[j] = 'X'  # 해당 햄버거는 먹혔다고 표시
                    break  # 한 사람당 햄버거 한 개
    print(count)


def solve2():
    import sys
    input = sys.stdin.readline

    N, K = map(int, input().split())
    s = input().strip()  # 벤치 문자열

    people = []  # 사람 위치 저장 리스트
    hamburgers = []  # 햄버거 위치 저장 리스트

    # 벤치를 순회하며 사람과 햄버거의 위치를 따로 저장
    for index, char in enumerate(s):
        if char == 'P':
            people.append(index)
        elif char == 'H':
            hamburgers.append(index)

    count = 0  # 햄버거를 먹은 사람 수
    i, j = 0, 0  # 각 리스트에 대한 포인터

    # 두 리스트를 동시에 순회
    while i < len(people) and j < len(hamburgers):
        if abs(people[i] - hamburgers[j]) <= K:
            # 현재 사람과 햄버거 매칭 가능 -> 할당 후, 둘 다 한 칸씩 이동
            count += 1
            i += 1
            j += 1
        elif hamburgers[j] < people[i] - K:
            # 현재 햄버거가 사람 도달 범위보다 더 왼쪽에 있으므로 햄버거 포인터 이동
            j += 1
        else:
            # 현재 사람이 햄버거 도달 범위보다 더 왼쪽에 있으면 사람 포인터 이동
            i += 1
    print(count)


if __name__ == '__main__':
    solve1()
    #solve2()