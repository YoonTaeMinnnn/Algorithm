from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    queue = deque(truck_weights)
    bridge_queue = deque(bridge)
    s = 0
    
    while bridge_queue:
        s -= bridge_queue.popleft()
        answer += 1
        if queue:
            if s + queue[0] <= weight:
                a = queue.popleft()
                bridge_queue.append(a)
                s += a
            else:
                bridge_queue.append(0)
        
    return answer