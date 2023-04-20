from collections import deque

l = [list(map(int, input().split())) for _ in range(7)]
l[0][0] = 1
queue = deque()
queue.append((0,0))
dis = [[0] * 7 for _ in range(7)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

while queue:
  x, y = queue.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<7 and 0<=ny<7 and l[nx][ny] == 0:
      l[nx][ny] = 1
      dis[nx][ny] = dis[x][y] + 1
      queue.append((nx,ny))

print(dis[6][6])


  