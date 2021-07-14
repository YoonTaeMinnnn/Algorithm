import heapq

def heapSort(iterable):
  h=[]
  result=[]
  for value in iterable:
    heapq.heappush(h,value)
  
  for i in range(len(h)):
    result.append(heapq.heappop(h))
  
  return result

result = heapSort([1,2,3,1,4,100,50])
print(result)

