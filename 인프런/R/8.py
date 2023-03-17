k, n = map(int, input().split())
l = []
for _ in range(k):
  l.append(int(input()))

lt = 0
rt = min(l)

def com(t):
  cnt = 0
  for i in l:
    cnt += (i // t)
  return cnt

res = 0
while lt <= rt:
  mid = (lt + rt) // 2
  if com(mid) == n:
    res = mid
    lt = mid + 1
  elif com(mid) < n:
    rt = mid - 1
  elif com(mid) > n:
    lt = mid + 1

print(res)