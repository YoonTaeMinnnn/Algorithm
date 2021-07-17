from itertools import permutations   #순서 고려

result = list(permutations(['A','B','C'],2))  
print(result)

from itertools import combinations      #순서 고려x 

result = list(combinations(['A','B','C'],3))
print(result)

from itertools import product

result = list(product(['A','B','C'],repeat=2)) #원소 중복 가능 (repeat=2 => 2개 선택)
print(result)