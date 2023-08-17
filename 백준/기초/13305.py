n = int(input())
dis = list(map(int, input().split()))
city = list(map(int, input().split()))

min_price = city[0]
res = 0

for i in range(n-1):
  if city[i] < min_price:
    min_price = city[i]

  res += (min_price * dis[i])

print(res)

