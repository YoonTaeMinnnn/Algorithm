T = int(input())
result = []

for i in range(1,T+1):
    N, s, e, k = map(int, input().split())
    l = list(map(int, input().split()))
    l = l[s-1:e]
    l.sort()
    print('#%d' %i + ' %d' %(l[k-1]))
  



  