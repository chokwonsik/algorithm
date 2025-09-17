"""
https://www.acmicpc.net/problem/13302
문제 이름: 리조트
출처: 정보올림피아드/2016/고등1, 초등3
알고리즘 분류: DP
"""

def solve1():
    """
    풀이1: 재귀+메모
    f(i,c) = i일부터 N일까지 이용할 최소 비용, 현재 쿠폰 c장
    1) i>N: 0원
    2) i가 불가능일: f(i+1, c)
    3) 가능일:
       a) 하루권: 10000 + f(i+1, c)
       b) 쿠폰 사용: if c>=3 → f(i+1, c-3)
       c) 3일권: 25000 + f(i+3, c+1)
       d) 5일권: 37000 + f(i+5, c+2)
    return min(a,b,c,d)
    """
    import sys
    sys.setrecursionlimit(10000)
    input=sys.stdin.readline

    N,M=map(int,input().split())
    closed=[False]*(N+2)
    if M:
        for x in map(int,input().split()):
            closed[x]=True

    from functools import lru_cache
    @lru_cache(None)
    def f(i,c):
        if i>N: return 0
        if closed[i]:
            return f(i+1, c)
        res=10_000+f(i+1,c)              # 하루권
        if c>=3:
            res=min(res, f(i+1, c-3))    # 쿠폰 3장 사용
        # 3일권
        res=min(res, 25_000 + f(i+3, c+1))
        # 5일권
        res=min(res, 37_000 + f(i+5, c+2))
        return res

    print(f(1,0))


def solve2():
    """
    풀이2: 그래프 탐색
    상태 = (day, coupon)
    간선:
     - (i,c)->(i+1,c) cost=10000 (하루권)
     - (i,c)->(i+1,c-3) cost=0 if c>=3 (쿠폰 사용)
     - (i,c)->(i+3,c+1) cost=25000 (3일권)
     - (i,c)->(i+5,c+2) cost=37000 (5일권)
    단, i가 불가능일이면 (i,c)->(i+1,c)만 허용
    시작 (1,0), 목표 day>N 최소 비용 → 다익스트라
    """
    import sys,heapq
    input=sys.stdin.readline
    N,M=map(int,input().split())
    closed=[False]*(N+6)
    if M:
        for x in map(int,input().split()):
            closed[x]=True

    INF=10**18
    dist=[[INF]*(N+6) for _ in range(N+6)]
    pq=[]
    dist[1][0]=0
    pq.append((0,1,0))
    while pq:
        cost,i,c=heapq.heappop(pq)
        if cost>dist[i][c]: continue
        if i>N:
            print(cost)
            return
        if closed[i]:
            if cost<dist[i+1][c]:
                dist[i+1][c]=cost
                heapq.heappush(pq,(cost,i+1,c))
        else:
            # 하루권
            nc,ni,ncost=c,i+1,cost+10000
            if ncost<dist[ni][nc]:
                dist[ni][nc]=ncost; heapq.heappush(pq,(ncost,ni,nc))
            # 쿠폰
            if c>=3:
                nc,ni,ncost=c-3,i+1,cost
                if ncost<dist[ni][nc]:
                    dist[ni][nc]=ncost; heapq.heappush(pq,(ncost,ni,nc))
            # 3일권
            nc,ni,ncost=c+1,i+3,cost+25000
            if ncost<dist[ni][nc]:
                dist[ni][nc]=ncost; heapq.heappush(pq,(ncost,ni,nc))
            # 5일권
            nc,ni,ncost=c+2,i+5,cost+37000
            if ncost<dist[ni][nc]:
                dist[ni][nc]=ncost; heapq.heappush(pq,(ncost,ni,nc))


if __name__ == "__main__":
    solve1()
    #solve2()
