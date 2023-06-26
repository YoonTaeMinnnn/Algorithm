import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    l = []
    s = len(progresses)
    for i in range(s):
        l.append(math.ceil((100-progresses[i]) / speeds[i]))
    
    queue = deque(l)
    first = queue.popleft()
    cnt = 1
    
    while queue:
        com = queue.popleft()
        if first >= com:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            first = com
    
    answer.append(cnt)
        
        
    return answer