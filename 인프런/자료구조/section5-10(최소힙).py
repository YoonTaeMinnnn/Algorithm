import heapq as hq # heapq는 default:최소힙

l = []
while True:
  a = int(input())
  if a == -1:
    break
  if a == 0:
    if len(l) == 0:
      print(-1)
    else:
      print(hq.heappop(l))
  else:
    hq.heappush(l, a)


  