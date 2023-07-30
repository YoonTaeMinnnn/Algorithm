from collections import deque

def solution(n, wires):
    answer = -1
    result = []
    global cnt
    
    def DFS(num):
        global cnt
        for i in l[num]:
            if visited[i] == 0:
                visited[i] = 1
                DFS(i)
                cnt += 1
                
    queue = deque(wires)
    c = 0
    while c != len(wires):
        p = queue.popleft()
        l = [[] for _ in range(n+1)] 
        visited = [0] * (n+1)
        for w in queue:
            a, b = w
            l[a].append(b)
            l[b].append(a)
 
        com = []
        for i in range(1, n+1):
            if visited[i] == 0:
                visited[i] = 1
                cnt = 1
                DFS(i)
                com.append(cnt)
        result.append(abs(com[0] - com[1]))
        queue.append(p)
        c += 1
        
    return min(result)