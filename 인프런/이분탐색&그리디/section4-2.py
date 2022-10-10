def decision(m):
  cnt = 0
  for i in l:
    cnt += i//m
  if cnt < n:
    return False
  return True
    

k, n = map(int, input().split())
l = []
for _ in range(k):
  l.append(int(input()))
res = 0
lt = 0
rt = max(l)
while lt <= rt:
  mid = (lt + rt) // 2
  if decision(mid):
    res = mid
    lt = mid + 1
  else:
    rt = mid - 1

print(res)
    