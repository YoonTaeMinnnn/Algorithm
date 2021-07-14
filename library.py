#내장 함수 

a = sum([1, 2, 3, 4])
print(a)



a = sum([1, 2, 3, 4])
print(a)

a=min([1,2,3,4])
print(a)

a=max([1,2,3,1,1000,2])
print(a)

result = eval('4*3') #문자열을 수식계산
print(result)



#iterable 객체를 정렬하는 기능 (list,투플,사전..)
result = sorted([1,2,1,4,2,8,2])  #리스트로 반환
print(result)

result = sorted([1,2,1,5,2,3,3,9,0],reverse=True)
print(result)



result = sorted([(2,3),(4,5),(1,2)])
print(result)

a = sum([1, 2, 3, 4])
print(a)

a=min([1,2,3,4])
print(a)

a=max([1,2,3,1,1000,2])
print(a)

result = eval('4*3') #문자열을 수식계산
print(result)



#iterable 객체를 정렬하는 기능 (list,투플,사전..)
result = sorted([1,2,1,4,2,8,2])  #리스트로 반환
print(result)

result = sorted([1,2,1,5,2,3,3,9,0],reverse=True)
print(result)





result = sorted([(2,3),(4,5),(1,2)])
print(result)

a=[(2,3),(3,2),(4,2)]
print(a[1])


a=[1,2,1,3,0]
result = sorted(a)
print(result)

from itertools import permutations   #순서 고려

result = list(permutations(['A','B','C'],2))  
print(result)

from itertools import combinations      #순서 고려x 

result = list(combinations(['A','B','C'],3))
print(result)

from itertools import product

result = list(product(['A','B','C'],repeat=2)) #원소 중복 가능 (repeat=2 => 2개 선택)
print(result)