n,m = map(int,input().split())


result = 0

for _ in range(n):
  data = list(map(int,input().split()))
  min_data = min(data)
  if min_data >= result:
    result=min_data

print(result)
