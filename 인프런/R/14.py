n, c = map(int, input().split())
l=[]
for _ in range(n):
  l.append(int(input()))
l.sort()
lt = 0
rt = l[-1]
res = 0

def min_dis(m):
  cnt = 1
  a = l[0]
  for i in range(1, n):
    if l[i] - a >= m:
      cnt += 1
      a = l[i]
  return cnt
      
while lt <= rt:
  mid = (lt + rt) // 2
  if min_dis(mid) >= c:
    lt = mid + 1
    res = mid
  else:
    rt = mid - 1

print(res)