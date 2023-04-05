import heapq as hq

heap = []
while True:
  a = int(input())
  if a == -1:
    break
  elif a == 0:
    if len(heap) == 0:
      print(-1)
    else:
      print(hq.heappop(heap))
  else:
    hq.heappush(heap, a)

  