n, m = map(int, input().split())
l = list(map(int, input().split()))
tot = l[0]
lt = 0
rt = 1
cnt = 0
while True:
  if tot < m:
    if rt < n:
      tot += l[rt]
      rt += 1
    else:
      break
  elif tot == m:
    cnt += 1
    tot -= l[lt]
    lt += 1
  else:
    tot -= l[lt]
    lt += 1
print(cnt)
    
  


# -------시간 초과 난 코드 (2중 반복문)--------
# n, m = map(int, input().split())
# l = list(map(int, input().split()))
# x = 0
# cnt = 0
# # 1 2 1 3 1 1 1 2
# for i in range(n):
#   if i == (n-1):
#     if l[i] != m:
#       break
#   x = 0 
#   x += l[i]
#   while m >= x:
#     if x == m:
#       cnt+=1
#       break
#     i+=1
#     x+=l[i]

# print(cnt)  
    