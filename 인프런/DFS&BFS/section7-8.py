from collections import deque
import sys

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
center = l[n//2][n//2]
ch = [[0] * n for _ in range(n)]
queue = deque()
queue.append((n//2, n//2))
sum = center
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
L = 0

while True:
  if L == n//2:
    break
  x, y = queue.popleft()
  print(sum)
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if ch[nx][ny] == 0:
      ch[nx][ny] = 1
      sum += l[nx][ny]
      queue.append((nx,ny))
  L+=1
print(sum)
