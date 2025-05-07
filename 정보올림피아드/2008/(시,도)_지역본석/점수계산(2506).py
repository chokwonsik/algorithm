# N = int(input())
# a = list(map(int, input().split()))
N = 10
a = [1, 0, 1, 1, 0, 1]
total = 0
streak_score = 0
for score in a:
    if score == 1:
        streak_score += 1
        total += streak_score
        #print(score, streak_score, total)
    else:
        streak_score = 0
print(total)