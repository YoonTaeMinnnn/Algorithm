from collections import deque
def solution(x, y, n):
    answer = 0
    queue = deque()
    queue.append(x)
    visited = [0] * 1000001
    count = [0] * 1000001
    while queue:
        a = queue.popleft()
        if a == y:
            return count[a]
        for i in (a+n, a*2, a*3):
            if i <= y:
                if visited[i] == 0:
                    visited[i] = 1
                    count[i] = count[a] + 1
                    queue.append(i)
    return -1