"""
https://www.acmicpc.net/problem/1132
문제 이름: 합
출처: 백준
알고리즘 분류: 그리디
"""


def solve1():
    """
    풀이1: 그리디 알고리즘
    1) 글자별 무게 계산
    2) 사용 글자 10개면 앞자리에 안 쓰인 글자 중 최소 무게에 0 배정
    3) 나머지 글자 무게 큰 순서로 9→1 배정
    4) 모든 단어에 배정된 숫자 대입해 합 계산
    시간복잡도: O(N·L + K log K), 공간복잡도: O(K)
    """
    import sys
    input = sys.stdin.readline

    N = int(input().strip())
    words = [input().strip() for _ in range(N)]

    # 1) 글자별 무게 계산, 앞글자 기록
    weight = {}
    first_used = set()
    for w in words:
        first_used.add(w[0])
        L = len(w)
        for i, ch in enumerate(w):
            weight[ch] = weight.get(ch, 0) + 10 ** (L - i - 1)
    letters = list(weight.keys())
    K = len(letters)
    #print(weight)
    #print(letters)
    print(first_used)

    # 2) 0 배정 문자 찾기 (글자 10개일 때만)
    zero_char = None
    if K == 10:
        candidates = [ch for ch in letters if ch not in first_used]
        zero_char = min(candidates, key=lambda x: weight[x])
    #print(candidates)
    print(zero_char)
    # 3) 나머지에 9→1 배정
    order_desc = sorted(letters, key=lambda x: weight[x], reverse=True)
    assign = {}
    num = 9
    print(order_desc)
    for ch in order_desc:
        if ch == zero_char:
            continue
        assign[ch] = num
        num -= 1
    if zero_char:
        assign[zero_char] = 0

    # 4) 합 계산
    total = 0
    for w in words:
        v = 0
        for ch in w:
            v = v * 10 + assign[ch]
        total += v

    print(total)


def solve2():
    """
    풀이2: 정렬 + 인덱스 활용
    1) 글자별 무게 계산
    2) 무게 오름차순 리스트(items) 생성, 10개 글자면 앞자리에 안 쓰인 글자에 0 배정
    3) 무게 내림차순 리스트(items_desc)로 9→1 배정
    4) 곱셈 누적해 합 출력
    시간복잡도: O(N·L + K log K), 공간복잡도: O(K)
    """
    import sys
    input = sys.stdin.readline

    N = int(input().strip())
    words = [input().strip() for _ in range(N)]

    # 1) 글자별 무게 계산, 앞글자 기록
    wt = {}
    first = set()
    for w in words:
        first.add(w[0])
        l = len(w)
        for i, c in enumerate(w):
            wt[c] = wt.get(c, 0) + 10 ** (l - i - 1)

    items = sorted(wt.items(), key=lambda x: x[1])  # (글자, 무게) 오름차순
    K = len(items)

    # 2) 0 배정 문자 찾기
    zero = None
    if K == 10:
        for ch, _ in items:
            if ch not in first:
                zero = ch
                break

    # 3) 무게 내림차순으로 9→1 배정, zero는 0 처리
    items_desc = sorted(items, key=lambda x: x[1], reverse=True)
    result = 0
    num = 9
    for ch, w in items_desc:
        if ch == zero:
            continue
        result += w * num
        num -= 1

    print(result)


if __name__ == '__main__':
    # 기본 실행: 그리디 풀이
    solve1()
    # 정렬+인덱스 풀이를 실행하려면 아래 주석 해제
    #solve2()
