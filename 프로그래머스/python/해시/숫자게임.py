from heapq import heappush, heappop, heapify

def solution(A, B):
    answer = 0
    A = [-i for i in A]
    B = [-i for i in B]
    heapify(A)
    heapify(B)
    
    while A and B:
        a = heappop(A)
        b = heappop(B)
        if -a < -b:
            answer += 1
        else:
            heappush(B, b)
        
    
    
    return answer