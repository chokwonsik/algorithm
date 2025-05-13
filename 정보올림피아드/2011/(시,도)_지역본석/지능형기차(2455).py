max_p = 0
people = 0
for _ in range(4):
    out_p, in_p  = map(int, input().split())
    people += in_p - out_p
    if max_p < people:
        max_p = people
        #print("if")
print(max_p)