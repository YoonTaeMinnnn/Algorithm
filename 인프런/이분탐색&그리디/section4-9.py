n = int(input())
l = list(map(int, input().split()))
a = [0]
b = []
while l:
    if len(l) == 1:
        if l[0] > a[-1]:
            a.append(l.pop())
            b.append('L')
        else:
            break
    if l[0] > l[-1]:
        if a[-1] < l[-1]:
            a.append(l.pop())
            b.append('R')
            continue
        else:
          if a[-1] < l[0]:
            a.append(l.pop(0))
            b.append('L')
          else:
            break
    else:
        if a[-1] < l[0]:
            a.append(l.pop(0))
            b.append('L')
        else:
            if a[-1] < l[-1]:
              a.append(l.pop())
              b.append('R')
            else:
              break
              
print(len(a)-1)
for i in b:
  print(i, sep='', end='')
# 3 2 10 1 5 4 7 8 9 6
