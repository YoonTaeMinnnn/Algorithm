def DFS(v, s):
  global res
  if s > c:
    return
  if v == n:
    if s <= c:
      if s > res:
        res = s
  else:
    DFS(v+1, s + l[v])
    DFS(v+1, s)

res = 0
c, n = map(int, input().split())
l = []
for _ in range(n):
  l.append(int(input()))

DFS(0,0)
print(res)