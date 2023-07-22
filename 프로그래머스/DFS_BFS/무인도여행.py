import sys
sys.setrecursionlimit(10000)

def solution(maps):
    s1 = len(maps)
    s2 = len(maps[0])
    
    answer = []
    visited = [[0]*s2 for _ in range(s1)]
    global cnt
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    def DFS(x, y):
        global cnt
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0<=nx<s1 and 0<=ny<s2 and visited[nx][ny] == 0 and maps[nx][ny] != "X":
                visited[nx][ny] = 1
                cnt += int(maps[nx][ny])
                DFS(nx,ny)
    
    for i in range(s1):
        for j in range(s2):
            cnt = 0
            if maps[i][j] != "X":
                if visited[i][j] == 0:
                    visited[i][j] = 1
                    cnt += int(maps[i][j])
                    DFS(i,j)
                    answer.append(cnt)
                    
    if not answer:
        return [-1]
    
    answer.sort()
                
    return answer