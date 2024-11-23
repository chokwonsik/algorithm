from itertools import permutations, product, combinations, combinations_with_replacement

a = [1,2,3]

print(list(permutations(a,2)))
print(list(combinations(a, 2)))
print(list(combinations_with_replacement(a, 2)))
oper_product = list(product(c, repeat = 5))