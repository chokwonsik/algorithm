def solve1():
    n = int(input())
    a = list(map(int, input().split()))  # 첫 번째 행
    b = list(map(int, input().split()))  # 두 번째 행
    
    # 1단계: 이미 막혀있는 경우 확인 (답: 0)
    for i in range(1, n):
        # 같은 열이 모두 0인 경우
        if a[i] == 0 and b[i] == 0:
            print(0)
            return
        
        # 대각선으로 막힌 경우 1: 위쪽 현재열, 아래쪽 이전열
        if a[i] == 0 and b[i-1] == 0:
            print(0)
            return
        
        # 대각선으로 막힌 경우 2: 위쪽 이전열, 아래쪽 현재열  
        if a[i-1] == 0 and b[i] == 0:
            print(0)
            return
    
    # 2단계: 1개만 막으면 되는 경우 확인 (답: 1)
    for i in range(n):
        # 한 열에 0이 하나라도 있으면 1개만 막으면 됨
        if a[i] == 0 or b[i] == 0:
            print(1)
            return
    
    # 3단계: 그 외 모든 경우 (답: 2)
    # 모든 칸이 1이면 2개 막아야 함
    print(2)

def solve2():
    n = int(input())
    floor = [list(map(int, input().split())) for _ in range(2)]
    updown = [floor[0][i] + floor[1][i] for i in range(n)]


    def changeNum():
        if (n * 2) == (sum(floor[0]) + sum(floor[1])):
            return 2
        if 0 in updown:
            return 0
        for i in range(1, n):
            if floor[0][i] == 0 and (floor[1][i - 1] == 0 or floor[1][min(i + 1, n - 1)] == 0):
                return 0
        return 1


    print(changeNum())

if __name__ == '__main__':
    solve1()