word = input()
com = input()

str1 = dict()
str2 = dict()

for i in word:
  str1[i] = str1.get(i,0) + 1
for i in com:
  str2[i] = str2.get(i,0) + 1
for key, value in str2.items():
  if str1[key] != value or str1.get(key,0) == 0:
    print("NO")
    break
else:
  print("YES")


# 딕셔너리.get(key, 0) : key값의 value가 있으면, value반환 | 없으면 0 반환