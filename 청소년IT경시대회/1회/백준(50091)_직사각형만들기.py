from collections import defaultdict

n = int(input())
c = list(map(int, input().split()))
c.sort()
max_area = defaultdict(int)
i = 0
while i < n:
    j = i
    while j < n and c[i] == c[j]:
        j += 1
    max_area[c[i] + c[i]] += c[i] * c[i] * ((j - i) // 2)
    paired = [False] * n
    while i < j:
        k = j
        while k < n:
            l = k
            while l < n and c[k] == c[l]:
                l += 1
            while k < l:
                if not paired[k]:
                    paired[k] = True
                    max_area[c[i] + c[k]] += c[i] * c[k]
                    break
                k += 1
            k = l
        i += 1
    i = j
print(max(max_area.values()))
