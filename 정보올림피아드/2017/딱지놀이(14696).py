from collections import Counter

def determine_winner(a_counts, b_counts):
    # 카드의 우선순위: ★(4), ◻(3), ●(2), ▲(1)

    for card_type in range(4, 0, -1):
        a = a_counts.get(card_type, 0)
        b = b_counts.get(card_type, 0)
        if a > b:
            return 'A'
        if a < b:
            return 'B'
    return 'D'  # 모든 카드가 동일한 경우


def main():
    N = int(input())
    results = []

    for _ in range(N):
        # A 플레이어의 카드 입력 처리
        a_input = list(map(int, input().split()))
        a_cards = a_input[1:]
        a_counter = Counter(a_cards)


        # B 플레이어의 카드 입력 처리
        b_input = list(map(int, input().split()))
        b_cards = b_input[1:]
        b_counter = Counter(b_cards)


        # 승자 결정 및 결과 저장
        results.append(determine_winner(a_counter, b_counter))

    # 모든 결과를 한 번에 출력
    print('\n'.join(results))


if __name__ == "__main__":
    main()
