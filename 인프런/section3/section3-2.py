string = input()
l = ['0','1','2','3','4','5','6','7','8','9']
word=''
for i in string:
  if i in l:
    word+=i

result = int(word)
print(result)
cnt = 0
for i in range(1,result+1):
  if result % i == 0:
    cnt+=1
print(cnt)

#--------내장함수 사용------------
string = input()
word=''
for i in string:
  if i.isdecimal():
    word+=i
print(int(word))
# ---- 이하 생략 -------