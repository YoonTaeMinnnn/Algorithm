n = int(input())
grade = list(map(int, input().split()))
new_grade=[]
max_grade = max(grade)

for i in grade:
  new = i/max_grade * 100
  new_grade.append(new)

print(sum(new_grade)/n)