def solve():
    for n in range(1000, 10000):  # 네 자리 수 범위
        reverse_n = int(str(n)[::-1])  # 문자열 뒤집어서 정수로 변환
        if 9 * n == reverse_n:
            print(n)
            return  # 문제 조건상 답은 하나뿐이므로 찾자마자 종료

if __name__ == '__main__':
    solve()
