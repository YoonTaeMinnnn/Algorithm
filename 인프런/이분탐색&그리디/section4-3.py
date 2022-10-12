def dvd(a):
  sum = 0
  cnt = 0
  for i in l:
    sum += i
    if sum >= a:
      cnt += 1
      sum = i
  if cnt < m:
    return -1
  return 0
  

n, m = map(int, input().split())
l = list(map(int, input().split()))

lt = 0
rt = sum(l)
res = 0
while lt <= rt:
  mid = (lt + rt) // 2
  if dvd(mid) == -1:
    rt = mid - 1
  else:
    res = mid
    lt = mid + 1

print(res)