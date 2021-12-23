city = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

res = distance[0]*price[0]
m = price[0]

for i in range(1,city-1):
  if m > price[i]:
    m = price[i]
  res = res + m*distance[i]

print(res)


