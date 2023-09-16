import math 

def DFS(N):
	if N == 1:
		return 1
	else:
		return N * DFS(N-1)

	
N = int(input())
n = str(math.factorial(N))

while True:
	s = 0
	for i in n:
		s += int(i)
	if s >= 10:
		n = str(s)
	else:
		break

print(s)