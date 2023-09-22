from heapq import heappush, heappop, heapify

case = int(input())
left = []
right = []
for _ in range(case):
  n = int(input())

  if len(left) == len(right):
    heappush(left, -n)
  else:
    heappush(right, n)

  if left and right and -left[0] > right[0]:
    a = -heappop(left)
    b = heappop(right)

    heappush(left, -b)
    heappush(right, a)

  print(-left[0])
  
      
  

