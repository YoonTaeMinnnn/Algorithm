n = int(input())
l = [list(map(int,input().split())) for _ in range(n)]
result = []
sum_a = 0 # 대각선1
sum_b = 0 # 대각선2
sum_c = 0 # 세로

  
for i in range(n):
  sum_c = 0
  result.append(sum(l[i]))
  sum_a += l[i][n-1-i] 
  sum_b += l[i][i]
  for j in range(n):
    sum_c += l[j][i]
  result.append(sum_c)

print(max(max(result), sum_a, sum_b))



