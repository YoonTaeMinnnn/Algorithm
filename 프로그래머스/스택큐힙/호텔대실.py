from heapq import heappush, heappop, heapify

def solution(book_time):
    
    def getTime(t, status):
        return int(t[status].split(":")[0])*60 + int(t[status].split(":")[1])
    book_time = [(getTime(t, 0), getTime(t,1)) for t in book_time]
    
    heap = []
    last_out = [-10]
    for time in book_time:
        heappush(heap, time)
    
    
    while heap:
        now_in, now_out = heappop(heap)
        if now_in >= last_out[0]+10:
            heappop(last_out)
            heappush(last_out, now_out)
        else:
            heappush(last_out, now_out)
    
    return len(last_out)
    