from heapq import heappush, heappop
def solution(n, works):
    answer = 0
    
    heap = []
    for i in works:
        heappush(heap, -i)
    
    while n > 0:
        p = heappop(heap)
        if p == 0:
            break
        p = -p
        p -= 1
        heappush(heap, -p)
        n -= 1
    
    for i in heap:
        answer += i**2
    
    return answer
