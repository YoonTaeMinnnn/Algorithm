n, m, k = map(int,input().split())
target = list(map(int,input().split()))
target.sort(reverse=True)

first = target[0]
second = target[1]

result=0
cnt=0
for _ in range(m):
  if cnt < k:
    result+=first
    cnt+=1
  else :
    result+=second
    cnt=0


print(result)
