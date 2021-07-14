from bisect import bisect_left, bisect_right

a=[1,2,3,4,5,6]
print(bisect_left(a,2))  #1
print(bisect_right(a,4)) #4