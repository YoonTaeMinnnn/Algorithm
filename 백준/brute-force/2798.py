from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))
three_cards = list(combinations(cards,3))
sum_list = []
for i in three_cards:
  sum_list.append(sum(i))

result = []
for i in sum_list:
  if i <= m:
    result.append(i)
print(max(result))
