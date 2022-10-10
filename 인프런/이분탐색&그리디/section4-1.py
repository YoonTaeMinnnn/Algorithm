n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
lt = 0
rt = n - 1
while lt <= rt:
  mid = (lt+rt) // 2
  if l[mid] == m:
    print(mid+1)
    break
  elif l[mid] > m:
    rt = mid - 1
  elif l[mid] < m:
    lt = mid + 1
    
  