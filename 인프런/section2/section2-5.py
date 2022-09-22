N, M = map(int, input().split())
n_list = [i for i in range(1,N+1)]
m_list = [i for i in range(1,M+1)]

cnt = [0]*(N+M+1)

for i in n_list:
  for j in m_list:
    cnt[i+j]+=1

max_sum = max(cnt)
for i in range(0,N+M+1):
  if cnt[i] == max_sum:
    print(i, end=' ')

    
