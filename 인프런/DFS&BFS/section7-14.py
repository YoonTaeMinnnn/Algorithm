from collections import deque

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
max = 0
for i in range(n):
    for j in range(n):
        if l[i][j] > max:
            max = l[i][j]
queue = deque()
result = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for height in range(1, max):
    ch = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if l[i][j] > height and ch[i][j] == 0:
                cnt += 1
                ch[i][j] = 1
                queue.append((i, j))
                while queue:
                    x, y = queue.popleft()
                    for z in range(4):
                        nx = x + dx[z]
                        ny = y + dy[z]

                        if 0 <= nx < n and 0 <= ny < n and l[nx][
                                ny] > height and ch[nx][ny] == 0:
                            ch[nx][ny] = 1
                            queue.append((nx, ny))

    result.append(cnt)

max = 0
for i in result:
    if i > max:
        max = i
print(max)

# 68262 32346 67332 72536 89527
