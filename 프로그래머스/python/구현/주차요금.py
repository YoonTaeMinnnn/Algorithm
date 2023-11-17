import math

def solution(fees, records):
    answer = []
    basic = fees[0]
    basic_fee = fees[1]
    add_time = fees[2]
    add_fee = fees[3]

    d_time = dict() # 차량별 주차시간 계산
    d = dict() # 차량별 누적 주차시간
    result = []

    for record in records:
        time = record.split(' ')[0]
        car = record.split(' ')[1]
        status = record.split(' ')[2]

        minute = int(time.split(':')[0]) * 60 + int(time.split(':')[1])

        if status == 'IN':
            d_time[car] = [minute, status]
        else:
            car_time = minute - d_time[car][0]
            d_time[car][1] = status
            d[car] = d.get(car, 0) + car_time


    for key, value in d_time.items():
        if value[1] == 'IN':
            print(key)
            last_time = 23*60 + 59
            d[key] = d.get(key, 0) + (last_time-value[0])

    result = []
    for car, minute in d.items():
        use_time = minute - basic
        if use_time <= 0:
            result.append([int(car), basic_fee])
        else:
            result.append([int(car),basic_fee + (math.ceil((use_time/add_time))*add_fee)])

    result.sort(key = lambda x : x[0])

    for i in result:
        answer.append(i[1])




    return answer