#collections 
#큐 구현
from collections import deque, Counter

data = deque([2,3,4])
data.append(5)
data.popleft()

print(data)
print(list(data))

#스택 구현
data = deque([1,2,3,4,5])
data.append(6)
data.pop()
print(data)
print(list(data))


#Counter
counter = Counter([1,1,2,2,2,3,4,5,5])
print(counter[3])
print(counter[2])