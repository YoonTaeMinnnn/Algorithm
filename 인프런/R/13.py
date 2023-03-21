n, m = map(int, input().split())
l = list(map(int, input().split()))
lt = 1
rt = sum(l)
res = 0

def divide(c):
  cnt = 0
  sum = 0
  for i in l:
    sum += i
    if sum >= c:
      cnt += 1
      sum = i
  return cnt 


while lt <= rt:
  mid = (lt+rt) // 2
  if divide(mid) >= m:
    lt = mid + 1
    res = mid
  else:
    rt = mid - 1

print(res)