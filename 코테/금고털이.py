import sys
input = sys.stdin.readline

W, N = map(int, input().split())
l = []
for _ in range(N):
    M, P = map(int, input().split())
    l.append((M, P))

l.sort(key = lambda x : -x[1])
result = 0
for kg, price in l:
    if W > kg:
        result += (kg * price)
        W -= kg
    else:
        result += (W * price)
        break


print(result)