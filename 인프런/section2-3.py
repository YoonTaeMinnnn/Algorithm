from itertools import combinations

n, k = map(int, input().split())
a = list(map(int, input().split()))
com = list(combinations(a,3))
result = []
for i in com:
  sum = i[0] + i[1] + i[2]
  result.append(sum)
result = set(result)
result = list(result)
result.sort(reverse=True)
print(result[k-1])