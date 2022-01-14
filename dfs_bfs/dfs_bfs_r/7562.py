from collections import deque

dx = [-2,-1,-1,-2,2,1,2,1]
dy = [-1,-2,2,1,1,2,-1,-2]

def bfs(x,y,x2,y2):
  queue = deque()
  queue.append((x,y))
  while queue:
    x, y = queue.popleft()
    if x == x2 and y == y2:
      return                 #도착지에 왔을때는 종료해야된다!!
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx>=n or nx<=-1 or ny>=n or ny<=-1:
        continue
      if graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx,ny))

case = int(input())
target = []
for _ in range(case):
  n = int(input())
  graph = [[0]*n for _ in range(n)]
  start_x, start_y = map(int,input().split())
  end_x, end_y = map(int, input().split())
    
  bfs(start_x,start_y,end_x,end_y)
  target.append(graph[end_x][end_y])

for i in target:
  print(i)


  
  