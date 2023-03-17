string = input()
s = ''
for i in string:
  if i.isdecimal():
    s += i

s = int(s)
cnt = 0

for i in range(1, s+1):
  if s % i == 0:
    cnt += 1

print(s)
print(cnt)