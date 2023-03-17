n = int(input())
l = []
for _ in range(n):
  a, b = map(int, input().split())
  l.append((a,b))

l.sort(key = lambda x : x[0], reverse = True)

top = 0
cnt = 1
for i in range(1,len(l)):
  if l[i][1] > l[top][1]:
    cnt += 1
    top = i

print(cnt)


