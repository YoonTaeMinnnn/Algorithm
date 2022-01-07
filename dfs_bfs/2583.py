import sys
sys.setrecursionlimit(10000)
def dfs(x,y):
  global width
  if x<=-1 or x>=m or y<=-1 or y>=n:
    return 
  if graph[x][y]==0:
    graph[x][y]=1
    width+=1
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    return True
  return False


m,n,k = map(int,sys.stdin.readline().split())

graph = [[0]*n for _ in range(m)]
width_list=[]
count = 0

for _ in range(k):
  x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
  for i in range(m-y2, m-y1):
    for j in range(x1,x2):
      graph[i][j]=1


for i in range(m):
  for j in range(n):
    width=0
    if dfs(i,j)==True:
      width_list.append(width)
      count+=1

width_list.sort()
print(count)
for i in width_list:
  print(i, end=' ')

