def DFS(L, b):
  global cnt
  if L == m:
    print(*res)
    cnt += 1
  else:
    for i in range(1, n+1):
      if i > b:
        res[L] = i
        DFS(L+1, i)
        
  
cnt = 0
n, m = map(int, input().split())
res = [0] * m
DFS(0, 0)
print(cnt)