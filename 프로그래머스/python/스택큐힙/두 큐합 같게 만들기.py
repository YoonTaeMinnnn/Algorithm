from collections import deque
def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    q1 = sum(queue1)
    q2 = sum(queue2)
    total = q1 + q2
    result = total // 2
    limit = len(queue1) + len(queue2)
    if result * 2 != total:
        return -1
    while q1 != q2:
        if answer > limit:
            return -1
        while queue1 and q1 > q2:
            out = queue1.popleft()
            queue2.append(out)
            q1 -= out
            q2 += out
            answer += 1
        while queue2 and q2 > q1:
            out = queue2.popleft()
            queue1.append(out)
            q2 -= out
            q1 += out
            answer += 1
        
    
    return answer