"""
https://leetcode.com/problems/reverse-integer/description/
문제 이름: Reverse Integer
출처:
알고리즘 분류: Math
"""


def reverse(self, x: int) -> int:
    if x < 0:
        abs_x = abs(x)
        reverse_x = int(str(abs_x)[::-1])
        reverse_x *= -1

    else:
        reverse_x = int(str(x)[::-1])

    if reverse_x < -2**31 or reverse_x > 2**31 - 1:
        return 0
    return reverse_x

print(reverse("ㅁ", 1235427892345789))