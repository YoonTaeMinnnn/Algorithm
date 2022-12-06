def DFS(v, s):
  global result
  if s > c:
    return 
  if v == n:
    if s <= c:
      result = s
  else:
    DFS(v+1, s+w[v])
    DFS(v+1, s)

c, n = map(int, input().split())
w = [int(input()) for _ in range(n)]
DFS(0,0)
print(result)


  