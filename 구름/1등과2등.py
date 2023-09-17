l = int(input())
l = str(l)
l = [int(i) for i in l]
cnt_1 = 0
cnt_2 = 0
while len(l) >= 2:
	if l[-1] == 1:
		if cnt_1 > 0:
			l.pop()
			continue
		if l[-2] == 2:
			cnt_1 += 1
			l.pop()
	elif l[-1] == 2:
		if cnt_2 > 0:
			l.pop()
			continue
		if l[-2] == 1:
			cnt_2 += 1
			l.pop()
	
	l.pop()

if cnt_1 >=1 and cnt_2 >= 1:
	print("Yes")
else:
	print("No")
		

