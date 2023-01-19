from collections import deque

# def BFS(x,y):
#   l[x][y] = 0
#   queue.append((x,y))
#   while queue:
#     mx, my = queue.popleft()
#     for i in range(8):
#       nx = mx + dx[i]
#       ny = my + dy[i]

#       if 0<=nx<n and 0<=ny<n and l[nx][ny] == 1:
#         l[nx][ny] == 0
#         queue.append((nx,ny))

dx = [1,-1,0,0,-1,1,-1,1]
dy = [0,0,1,-1,1,1,-1,-1]

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
queue = deque()
for i in range(n):
  for j in range(n):
    if l[i][j] == 1:
      queue.append((i,j))
      while queue:
        x, y = queue.popleft()
        for r in range(8):
          nx = x + dx[r]
          ny = y + dy[r]

          if 0<=nx<n and 0<=ny<n and l[nx][ny] == 1:
            l[nx][ny] = 0
            queue.append((nx,ny))

      cnt += 1

print(cnt)











  
