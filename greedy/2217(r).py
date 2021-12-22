n = int(input())
lof_w = []

for _ in range(n):
  lof_w.append(int(input()))

lof_w.sort(reverse=True)
compare_list=[]

cnt=1
for i in lof_w:
  compare_list.append(i*cnt)
  cnt+=1

print(max(compare_list))