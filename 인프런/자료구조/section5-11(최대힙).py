import heapq as hq

l = []
while True:
  a = int(input())
  if a == -1:
    break
  if a == 0:
    if len(l) == 0:
      print(-1)
    else:
      print(abs(hq.heappop(l)))
  else:
    hq.heappush(l, -a)