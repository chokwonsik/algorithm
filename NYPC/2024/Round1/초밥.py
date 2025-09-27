"""

문제 이름:
출처:
알고리즘 분류:
"""
def solve2():
    import sys
    input=sys.stdin.readline

    T=int(input())
    for _ in range(T):
        A,B=map(int,input().split())
        low, high = 1, min(A,B)
        ans = None

        while low <= high:
            mid = (low+high)//2
            if 4*mid >= A+B:
                ans = mid
                high = mid-1
            else:
                low = mid+1

        print(ans if ans is not None else -1)

def solve1():
    import sys
    input=sys.stdin.readline
    T=int(input())
    for _ in range(T):
        A,B=map(int,input().split())
        # 1) 최소 상자 수
        k = (A+B + 3)//4       # ceil((A+B)/4)
        # 2) 가능한지 검사
        if k <= min(A,B):
            print(k)
        else:
            print(-1)

if __name__ == '__main__':
    solve1()
    #solve2()



