import sys

n, m = map(int, input().split())
act = []
test = []
s = 0
for _ in range(n):
    a, b = map(int, input().split())
    s += a
    act.append([s, b])

s = 0 
for _ in range(m):
    a, b = map(int, input().split())
    s += a
    test.append([s, b])

act_l = [0] * 101
test_l = [0] * 101

a = 1
for i in range(len(act)):
    for j in range(a, act[i][0]+1):
        act_l[j] = act[i][1]
    a = act[i][0] + 1

a = 1
for i in range(len(test)):
    for j in range(a, test[i][0] + 1):
        test_l[j] = test[i][1]
    a = test[i][0] + 1

max_r = 0
for i in range(101):
    max_r = max(max_r, test_l[i] - act_l[i])

print(max_r)


    
