l = [4,2,1,8,1,5]
v = [0] * (len(l)+1)
for i in range(1, len(v)):
  v[i] = v[i-1] + l[i-1]

# 1 4
print(v[4] - v[1])