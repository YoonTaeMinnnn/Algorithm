from collections import deque
n = int(input())
word = [input() for _ in range(n)]
wword = [input() for _ in range(n-1)]

queue = deque(word)
while queue:
  a = queue.popleft()
  if a not in wword:
    print(a)
    break

    




