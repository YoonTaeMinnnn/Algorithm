n,k = map(int, input().split())
coins = []
for _ in range(n):
  coins.append(int(input()))

coins.sort(reverse=True)
cnt =0 

for i in coins:
  cnt+=k//i
  k%=i
  
print(cnt)
  
