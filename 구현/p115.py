location = input()
index = int(location[1])
column = int(ord(location[0])) - int(ord('a')) + 1

steps = [(1,-2),(-1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1),(-2,-1)]
cnt = 0

start_loc = (index, column)

for step in steps:
  after_loc = (step[0]+start_loc[0], step[1]+start_loc[1])
  print(after_loc)
  if after_loc[0]>0 and after_loc[1]>0:
    cnt+=1
  

print(cnt)



