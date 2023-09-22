from heapq import heappush, heappop, heapify

case = int(input())
for _ in range(case):
  n = int(input())
  l = list(map(int, input().split()))
  heap = []
  for i in range(n):
    if i % 2 == 0: #홀수
      heappush(heap,l[i])
    else:
      heappush(heap,l[i])
      
  

