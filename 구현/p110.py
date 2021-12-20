n = int(input())
plan = list(input().split())
print(plan)
index=1
column = 1

for value in plan:
  if value=='R':
    column+=1
    if column>n:
      column-=1

  elif value=='L':
    column-=1
    if column<1:
      column+=1

  elif value =='U':
    index-=1
    if index<1:
      index+=1

  elif value=='D':
    index+=1
    if index>n:
      index-=1


print(index, column)
  

