n,k = map(int, input().split())

result = []
cnt = 0
for i in range(1,n+1):
    if n % i == 0:
        cnt = cnt + 1
        result.append(i)
if cnt < k:
    print(-1)
else:
    print(result[k-1])