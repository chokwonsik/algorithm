"""
문제 이름:
출처:
알고리즘 분류:
"""

def solve1():
    from collections import Counter
    N = int(input())
    nums = list(map(int, input().split()))
    Q = int(input())

    for i in range(Q):
        start, end = map(int, input().split())
        nums_sl = nums[start-1: end]
        counts = Counter(nums_sl)

        # print(start-1, end-1)
        # print(counts)
        # 제출한 숫자가 1개인 경우
        filtered = {k: v for k, v in counts.items() if v < 2}
        #print(filtered)
        if not filtered:
            print(0)
        else:
            min_key = min(filtered)
            print(min_key)
        #print("----------")
    """
    슬라이싱을 하고 value값이 2 이상인것을 제외해야함
    """

if __name__ == "__main__":
    solve1()

"""
10
1 1 5 7 6 6 5 8 9 10
4
1 10
2 8
9 9
1 2
"""