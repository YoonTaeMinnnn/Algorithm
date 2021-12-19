#collections 
#큐 구현

import time 

start_time = time.time()
from collections import deque, Counter

data = deque([2,3,4])
data.append(5)
data.popleft()

print(data)
print(list(data))

end_time = time.time()
print('time :',end_time - start_time)



#Counter
counter = Counter([1,1,2,2,2,3,4,5,5])
print(counter[3])
print(counter[2])