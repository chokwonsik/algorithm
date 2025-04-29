# 볼 모으기
# https://www.acmicpc.net/problem/17615

N = input()
a = input()

# 우측 R제거 우측 R 모으기
rstrip_r = a.rstrip("R").count("R")

# 우측 B제거 우측 B 모으기
rstrip_b = a.rstrip("B").count("B")

# 좌측 R제거 좌측 R 모으기
lstrip_r = a.lstrip("R").count("R")

# 좌측 B제거 좌측 B모으기
lstrip_b = a.lstrip("B").count("B")
print(min(rstrip_r, lstrip_r, rstrip_b, lstrip_b))
