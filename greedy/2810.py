seat = int(input())
seat_cate = input()
L_count = seat_cate.count('LL')

if L_count <= 1:
  print(len(seat_cate))
else:
  print(len(seat_cate) - L_count + 1)
    
