#큰수법칙
n,m,k=map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()
cnt=0
result = 0
first = arr[n-1]
second = arr[n-2]


for _ in range(m):
  cnt+=1
  if cnt <= k:
    result+=first
    continue
  result+=second
  cnt=0

print(result)