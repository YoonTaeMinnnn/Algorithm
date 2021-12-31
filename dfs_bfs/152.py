from collections import deque

def bfs(graph):
  queue = deque()
  

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int,input())))
print(graph)

cnt=0

bfs(graph)