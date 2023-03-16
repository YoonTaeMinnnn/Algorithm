from collections import deque

l = [list(map(int, input().split())) for _ in range(7)]

result = [[0]*7 for _ in range(7)]

queue = deque()
queue.append((0,0))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

while queue:
  x, y = queue.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<=6 and 0<=ny<=6 and l[nx][ny] == 0:
      l[nx][ny] = 1
      result[nx][ny] = result[x][y] + 1
      queue.append((nx,ny))
      
if result[6][6] == 0:
  print(-1)
else:
  print(result[6][6])


      

