# a = 'the bear'
# print(a.find('B'))
# print(a.count('B'))
# # A~Z : 65~90 (대문자)

# a = 'AZ'
# for i in a:
#     print(ord(i), end=' ')

# a = [1, 2, 3, 4, 5]
# a.append(6)
# print(a)
# a.pop()
# print(a)
# a.pop(1)
# print(a)
# a.remove(3)
# print(a)

# a = []
# for i in range(1, 11):
#     a.append(i)
# # a -> 1~10

# b = [i**2 for i in a if i % 2 == 1]
# print(b)

# a = (1, 23, 4)
# print(a[2])

# a = [1, 2, 3, 4, 5, 6, 6]
# for i in enumerate(a):
#     print(i)
# if all(60>x for x in a): #모두 충족 시, 참
#   print("true")
# else:
#   print("false")

# if any(5<x for x in a):  # 하나라도 참이면 참
#   print("true")
# else:
#   print("false")

a = [0]*10
print(a)
a=[list(map(int, input().split())) for _ in range(2)]
print(a)


def add(a,b):
  result = a+b
  return result, a, b

a, b, c = add(3,2)

print(a)
print(b)
print(c)