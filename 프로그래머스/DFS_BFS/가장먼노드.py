from collections import deque

def solution(n, edge):
    answer = 0
    
    l = [[] for _ in range(n+1)]
    for i in edge:
        l[i[0]].append(i[1])
        l[i[1]].append(i[0])
    
    v = [0] * (n+1)
    visited = [0] * (n+1)
    visited[1] = 1
    
    queue = deque()
    queue.append(1)
    while queue:
        a = queue.popleft()
        for i in l[a]:
            if visited[i] == 0:
                visited[i] = 1
                v[i] = v[a] + 1
                queue.append(i)
        
    m = max(v)
    
    for i in v:
        if i == m:
            answer += 1
    
    return answer