from collections import deque
def solution(priorities, location):
    answer = 0
    l = [(index, val) for index, val in enumerate(priorities)]
  
    queue = deque(l)
    while queue:
        a = queue.popleft()
        if any(a[1] < x[1] for x in queue):
            queue.append(a)
        else:
            answer += 1
            if a[0] == location:
                return answer
                
    return answer