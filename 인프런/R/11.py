from collections import deque

n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

# 50 60 70 90 100
l = deque(l)
cnt = 0
while l:
  if len(l) == 1:
    cnt += 1
    break
  if l[0] + l[-1] > m:
    cnt += 1
    l.pop()
  else:
    cnt += 1
    l.popleft()
    l.pop()

print(cnt)