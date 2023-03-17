n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

result = []
sum_a = 0
sum_b = 0
for i in range(n):
  sum_a += l[i][-1-i]
for i in range(n):
  sum_b += l[i][i]
  
result.append(sum_a)
result.append(sum_b)

for i in range(n):
  sum_c = 0
  sum_d = 0
  for j in range(n):
    sum_c += l[i][j]
    sum_d += l[j][i]
  result.append(sum_c)
  result.append(sum_d)

print(max(result))
    
    