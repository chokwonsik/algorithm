def solve():
    N = int((input()))

    count = 0

    for i in range(1, N+1):
        s = str(i)
        count += s.count("3")
        count += s.count("6")
        count += s.count("9")

    print(count)

if __name__ == '__main__':
    solve()
