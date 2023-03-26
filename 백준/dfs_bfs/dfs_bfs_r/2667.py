import sys
read = sys.stdin.readline

def dfs(x,y):
  global cnt
  if x>=n or x<=-1 or y>=n or y<=-1:
    return
  if graph[x][y]==1:
    cnt+=1
    graph[x][y]=0
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    return True
  return False

n = int(read())
graph = [list(map(int, input())) for _ in range(n)]
count = 0
cnt_list = []

for i in range(n):
  for j in range(n):
    cnt=0
    if dfs(i,j)==True:
      count+=1
      cnt_list.append(cnt)
      
print(count)
cnt_list.sort()
for i in cnt_list:
  print(i)