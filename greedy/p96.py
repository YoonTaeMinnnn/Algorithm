n, m = map(int,input().split())

result = 0

for i in range(n):
  cards = list(map(int, input().split()))
  card_min = min(cards)
  result = max(result,card_min)

print(result)
