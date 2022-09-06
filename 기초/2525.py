hour, min = map(int, input().split())
add = int(input())

add_min = min + add
add_hour =  add_min // 60

result_hour = hour + add_hour
result_min = add_min % 60

print(result_hour % 24,result_min)