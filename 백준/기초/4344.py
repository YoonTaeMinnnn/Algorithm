case = int(input())

for _ in range(case):
  grade = list(map(int, input().split()))
  n = grade[0]
  grade = grade[1:n+1]
  avg = sum(grade) / n
  count = 0
  for i in grade:
    if i > avg:
      count = count + 1
  rate = (count / n) * 100
  print("%.3f" %rate + "%")
