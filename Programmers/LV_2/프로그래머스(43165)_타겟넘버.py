# 솔루션1
# from itertools import product

# def solution(numbers, target):
#     l = [(x, -x) for x in numbers]
#     s = list(map(sum, product(*l)))
#     return s.count(target)


# 솔루션2
def solution(numbers, target, current_sum=0, index=0):
    if index == len(numbers):
        return 1 if current_sum == target else 0

    # 현재 숫자를 더하거나 빼는 경우
    return (solution(numbers, target, current_sum + numbers[index]
                     , index + 1) +
            solution(numbers, target, current_sum - numbers[index]
                     , index + 1))
