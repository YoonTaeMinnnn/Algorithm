import sys

N = int(input())
l = [list(map(int, input())) for _ in range(N)] 

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def DFS(x, y):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<N and 0<=ny<N and l[nx][ny] == 1:
            l[nx][ny] = 0
            cnt += 1
            DFS(nx,ny)

result = []

for i in range(N):
    for j in range(N):
        if l[i][j] == 1:
            l[i][j] = 0
            cnt = 1
            DFS(i,j)
            result.append(cnt)

result.sort()

print(len(result))
for i in result:
    print(i)