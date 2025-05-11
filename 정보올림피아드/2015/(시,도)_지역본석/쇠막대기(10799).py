from collections import deque
# 입력 받기
sen = input()
stack = []
cnt = 0
# 문자열을 한 글자씩 순회
for i in range(len(sen)):
    if sen[i] == '(':  # 여는 괄호는 무조건 스택에 추가
        stack.append('(')
        print(f"( {stack}")
    else:  # 닫는 괄호일 경우
        stack.pop()  # 스택에서 여는 괄호 하나 제거
        if sen[i - 1] == '(':  # 바로 앞이 여는 괄호라면 레이저
            cnt += len(stack)  # 레이저가 쇠막대기만큼 잘라냄
            print(f"i-1 ( {cnt}, {stack}")
        else:  # 바로 앞이 닫는 괄호라면 쇠막대기의 끝
            cnt += 1  # 쇠막대기의 끝 부분은 하나의 조각
            print(f"i-1 ) {cnt}, {stack}")
# 결과 출력
print(cnt)