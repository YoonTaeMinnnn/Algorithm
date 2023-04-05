def DFS(v):
  if v == n+1:
    for i in range(1, n+1):
      if visit[i] == 1:
        print(i, end=' ')
    print()
  else:
    visit[v] = 1
    DFS(v+1)
    visit[v] = 0
    DFS(v+1)
  
n = int(input())
visit = [0] * (n+1)
DFS(1)