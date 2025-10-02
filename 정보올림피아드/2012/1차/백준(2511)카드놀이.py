A = list(map(int, input().split()))
B = list(map(int, input().split()))

last_win = ""
a_score = 0
b_score = 0
for i in range(len(A)):
    if A[i] > B[i]:
        last_win = "A"
        a_score += 3
    elif B[i] > A[i]:
        last_win = "B"
        b_score += 3
    else:
        a_score += 1
        b_score += 1

print(a_score, b_score)
if a_score > b_score:
    print("A")
elif b_score > a_score:
    print("B")
else:
    if last_win:
        print(last_win)
    else:
        print("D")

