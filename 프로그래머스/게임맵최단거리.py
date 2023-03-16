from collections import deque

def solution(maps):
    x_size = len(maps)
    y_size = len(maps[0])
    
    queue = deque()
    queue.append((0,0))
    dis = [[0]* y_size for _ in range(x_size)]
    dis[0][0] = 1
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<= nx < x_size and 0 <= ny < y_size and maps[nx][ny] == 1:
                maps[nx][ny] = 0
                dis[nx][ny] = dis[x][y] + 1
                queue.append((nx,ny))
                
    if dis[x_size-1][y_size-1] == 0:
        return -1
    return dis[x_size-1][y_size-1]