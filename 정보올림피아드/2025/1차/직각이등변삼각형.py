n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

plus  = [y + x for x, y in points]
minus = [y - x for x, y in points]

max_plus  = max(plus)
min_plus  = min(plus)
max_minus = max(minus)
min_minus = min(minus)

min_y = min(y for x, y in points)
max_y = max(y for x, y in points)

length_up = max_minus + max_plus - 2 * min_y

length_down = 2 * max_y - (min_minus + min_plus)

print(min(length_up, length_down))