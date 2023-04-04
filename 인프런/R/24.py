str_1 = input()
d_1 = dict()
for i in str_1:
  d_1[i] = d_1.get(i, 0) + 1
str_2 = input()


d_2 = dict()
for i in str_2:
  d_2[i] = d_2.get(i, 0) + 1

if d_1 == d_2:
  print("YES")
else:
  print("NO")