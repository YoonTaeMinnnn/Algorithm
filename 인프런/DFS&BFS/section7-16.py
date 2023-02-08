def DFS(x, y):
  if x == 0:
    print(y)
  else:
    if y-1>=0 and l[x][y-1] == 1 and ch[x][y-1] == 0:
      ch[x][y-1] = 1
      DFS(x, y-1)
    elif y+1<10 and l[x][y+1] == 1 and ch[x][y+1] == 0:
      ch[x][y+1] = 1
      DFS(x, y+1)
    else:
      DFS(x-1, y)
    

l = [list(map(int, input().split())) for _ in range(10)]
ch = [[0]*10 for _ in range(10)]
for i in range(10):
  if l[9][i] == 2:
    ch[9][i] = 1
    DFS(9, i)

  
  

  