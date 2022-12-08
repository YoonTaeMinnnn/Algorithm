def DFS(v):
  global cnt
  if v == m:
    print(*res)
    cnt += 1
  else:
    for i in range(1,n+1):
      res[v] = i
      DFS(v+1)
    
    
n, m = map(int, input().split())
res = [0] * m
cnt = 0
DFS(0)
print(cnt)