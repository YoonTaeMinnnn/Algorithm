n, m = map(int, input().split())
l = list(map(int, input().split()))
cnt = 0 

tot = l[0]
lt = 0
rt = 1
while True:
  if tot < m:
    if rt < n:
      tot += l[rt]
      rt += 1
    else:
      break
  elif tot == m:
    tot -= l[lt]
    lt += 1
    cnt += 1
  else:
    tot -= l[lt]
    lt += 1

print(cnt)
  