n = int(input())
stu = list(map(int, input().split()))
aver = sum(stu) / n
aver = int(round(aver,0))
dif_list = []
for i in range(n):
  dif = abs(aver - stu[i])
  dif_list.append(dif)
dif_min = min(dif_list)

sno = []

for i in range(len(dif_list)):
  if dif_list[i] == dif_min:
    sno.append(i)
result = []
for i in sno:
  result.append((i,stu[i]))
result.sort(key = lambda x:(x[1],-x[0]))
print(aver, result[-1][0]+1)


