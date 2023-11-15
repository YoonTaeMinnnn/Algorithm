from heapq import heappush, heappop
def solution(operations):
    min_heap = []
    max_heap = []
    for operation in operations:
        op = operation.split(' ')[0]
        num = int(operation.split(' ')[1])
        if op == 'I':
            heappush(min_heap, num)
            heappush(max_heap, -num)
        elif min_heap and op == 'D' and num == -1:
            a = heappop(min_heap)
            max_heap.remove(-a)
        elif min_heap and op == 'D' and num == 1:
            a = -heappop(max_heap)
            min_heap.remove(a)
        
    if not min_heap:
        return [0,0]
    else:
        return [-heappop(max_heap), heappop(min_heap)]