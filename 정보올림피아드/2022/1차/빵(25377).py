N = int(input())
cnt = 0
time_l = []
for i in range(N):
    time_to_bakery, bread_ready_time = list(map(int, input().split()))
    if time_to_bakery <= bread_ready_time:
        time_l.append(bread_ready_time)

if time_l:
    print(min(time_l))
else:
    print("-1")