def DFS(L, period):
  global res
  if L > n:
    return
  if L == n:
    if period > res:
      res = period
  else:
    DFS(L + l[L][0], period + l[L][1])
    DFS(L + 1, period)

n = int(input())
l = []
res = -1
# (4,20), (2,10), (3,15), (3,20), (2,30), (2,20), (1,10)
for _ in range(n):
  t, p = map(int, input().split())
  l.append((t,p))
DFS(0,0)
print(res)