def solution(n, computers):
    def DFS(v):
        visited[v] = 1
        for i in l[v]:
            if visited[i] == 0:
                DFS(i)
    
    l = [[] for _ in range(n)]
    visited = [0] * n
    print(l)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                l[i].append(j)
                
    cnt = 0   
    
    for i in range(n):
        if visited[i] == 0:
            DFS(i)
            cnt += 1
            
    return cnt