total, com = map(int, input().split())
list = list(map(int, input().split()))
result = []
for i in list:
  if i < com:
    result.append(i)

for i in result:
  print(i, end=" ")