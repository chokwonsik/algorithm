# 양팔 저울
# https://www.acmicpc.net/problem/17610

def solve1():
    import sys
    input = sys.stdin.readline

    # 입력 받기
    k = int(input().strip())
    weights = list(map(int, input().split()))

    # 초기 가능한 차이값 집합: 0부터 시작
    possible_values = {0}

    # 각 추에 대해 집합을 갱신
    for weight in weights:
        new_values = set()
        for diff in possible_values:
            # 추를 사용하지 않는 경우: diff 그대로
            new_values.add(diff)
            # 추를 오른쪽에 올리는 경우: diff + weight
            new_values.add(diff + weight)
            # 추를 왼쪽에 올리는 경우: diff - weight
            new_values.add(diff - weight)
        possible_values = new_values  # 새롭게 가능한 차이값 집합으로 갱신
        print(possible_values)

    # 전체 추 무게의 합 S 계산
    S = sum(weights)
    unreachable = 0
    # 1부터 S까지 검사하여 존재하지 않으면 카운트 증가
    for x in range(1, S + 1):
        if x not in possible_values:
            unreachable += 1

    # 결과 출력
    print(unreachable)

def solve2():
    """
    1. sys.stdin.readline을 이용해 입력을 빠르게 받아옴
    """
    import sys
    import itertools
    input = sys.stdin.readline

    """
    2. 입력 받기
       k: 추의 개수
       weights: 각 추의 무게 리스트
    """
    k = int(input().strip())
    weights = list(map(int, input().split()))

    """
    3. 가능한 차이값 집합 생성
       각 추마다 0 (사용 안 함), 1 (오른쪽), -1 (왼쪽) 선택하여 모든 조합을 생성
       각 조합에 대해 총 차이값 = sum(선택값 * 추 무게)
    """
    possible_values = set()
    for choices in itertools.product([0, 1, -1], repeat=k):
        total = 0
        for i, choice in enumerate(choices):
            total += choice * weights[i]
        possible_values.add(total)

    """
    4. 전체 추 무게 합 S 계산 및 1부터 S까지 측정 불가능한 경우의 수 카운트
    """
    S = sum(weights)
    unreachable = 0
    for x in range(1, S + 1):
        if x not in possible_values:
            unreachable += 1

    # 결과 출력
    print(unreachable)

def solve3():
    """
    1. sys.stdin.readline을 이용해 입력을 빠르게 받아옴
    """
    import sys
    from itertools import combinations
    input = sys.stdin.readline

    """
    2. 입력 받기
       k: 추의 개수
       weights: 각 추의 무게 리스트
    """
    k = int(input().strip())
    weights = list(map(int, input().split()))
    n = len(weights)

    """
    3. 가능한 차이값 집합 생성
       - 먼저 추 인덱스 전체 집합에서 왼쪽 그룹으로 올릴 조합을 만듦.
       - 왼쪽 그룹에 선정한 후, 남은 추들 중에서 오른쪽 그룹으로 올릴 조합을 선택.
       - 차이값 = (오른쪽 그룹의 합) - (왼쪽 그룹의 합)
       - 왼쪽, 오른쪽 둘 다 공집합인 경우도 포함됨.
    """
    possible_values = set()
    for left_count in range(0, n + 1):
        for left in combinations(range(n), left_count):
            sum_left = sum(weights[i] for i in left)
            # 왼쪽 그룹으로 고른 후 나머지 인덱스들
            remaining = [i for i in range(n) if i not in left]
            for right_count in range(0, len(remaining) + 1):
                for right in combinations(remaining, right_count):
                    sum_right = sum(weights[i] for i in right)
                    diff = sum_right - sum_left
                    possible_values.add(diff)

    """
    4. 전체 추 무게 합 S 계산 및 1부터 S까지 측정 불가능한 경우의 수 카운트
    """
    S = sum(weights)
    unreachable = 0
    for x in range(1, S + 1):
        if x not in possible_values:
            unreachable += 1

    # 결과 출력
    print(unreachable)

if __name__ == '__main__':
    solve1()
   # solve2()
    #solve3()

