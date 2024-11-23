def factorial(n):
    if n == 1:  # 기본 조건
        return 1
    else:
        return n * factorial(n - 1)  # 재귀 호출

print(factorial(4))

"""
               3
            3  *   f(2)
                  2   *  f(1)
                          return 1 
"""