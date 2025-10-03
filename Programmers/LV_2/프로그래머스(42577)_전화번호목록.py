#1
def solution(phone_book):
    phone_book.sort()  # 전화번호 정렬
    for i in range(len(phone_book) - 1):  # 옆에 있는 번호끼리 비교
        if phone_book[i + 1].startswith(phone_book[i]):  # 접두사 확인
            return False
    return True

#2
def solution(phone_book):
    hash_map = {}
    for number in phone_book:  # 번호를 해시에 저장
        hash_map[number] = True

    for number in phone_book:  # 각 번호를 확인
        for i in range(1, len(number)):  # 접두사를 잘라서 해시에 있는지 확인
            if number[:i] in hash_map:
                return False
    return True

#3
def solution(phone_book):
    phone_book.sort()  # 정렬
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):  # 접두사 확인
            return False
    return True

#4 (시간초과)
def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i != j and phone_book[j].startswith(phone_book[i]):  # 서로 다른 번호를 비교
                return False
    return True
