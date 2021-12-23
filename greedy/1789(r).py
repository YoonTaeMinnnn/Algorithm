s = int(input())

n=1
cnt=0
while (n*(n+1)//2) <= s:
  n+=1
  cnt+=1

print(cnt)