from collections import deque

n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
cnt = 0 
l = deque(l)
while l:
  if len(l) == 1:
    cnt += 1
    break
  if l[0] + l[-1] > m:
    l.pop()
    cnt += 1
  else:
    l.popleft()
    l.pop()
    cnt += 1

print(cnt)
    
    
    