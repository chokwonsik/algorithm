def main():

    N = int(input("N을 입력하세요: "))
    razer = list(map(int, input("razer 리스트를 입력하세요 (공백으로 구분): ").split()))


    rezer_len = len(razer)
    top_used = [False] * rezer_len
    top = [0] * rezer_len

    for i in range(rezer_len - 1, -1, -1): # rezer_len-1부터 0까지
        print(f"현재 i: {i}")
        for j in range(i-1, -1, -1):
            print(f"  비교할 j: {j}")
            if razer[i] <= razer[j] and not top_used[j]:
                top[i] = razer[j]
                top_used[j] = True


    print("top:", top)
    print("top_used:", top_used)

if __name__ == "__main__":
    main()
