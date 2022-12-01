def DFS(v):
  if v > 7:
    return
  DFS(v*2)
  DFS(v*2+1)
  print(v)
DFS(1)