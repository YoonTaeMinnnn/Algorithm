import heapq as hq

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        a = hq.heappop(scoville)
        b = hq.heappop(scoville)
        hq.heappush(scoville, a + b*2)
        answer += 1
        
            
    return answer