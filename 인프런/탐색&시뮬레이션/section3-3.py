result = [i for i in range(1,21)]

for _ in range(10):
  a, b = map(int, input().split())
  l = result[a-1:b]
  l.reverse()
  result[a-1:b] = l
  
for i in result:
  print(i, end=' ')

# 5 10
# 9 13
# 12
# 34 56 12 34 56 1 20 1 20