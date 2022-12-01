def DFS(v):
  if v > 7:
    return 
  DFS(v*2)
  print(v)
  DFS(v*2+1)

DFS(1)