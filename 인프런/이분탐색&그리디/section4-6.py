import sys
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
  l.append(list(map(int, input().split())))

l.sort(reverse = True)
cnt = 1
top = 0
for i in range(1,n):
  if l[i][1] > l[top][1]:
    cnt += 1
    top = i
    
print(cnt)
