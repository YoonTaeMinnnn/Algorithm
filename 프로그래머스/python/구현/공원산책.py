def solution(park, routes):
    answer = []
    n = len(park)
    m = len(park[0])
    start_x = 0
    start_y = 0
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                start_x = i
                start_y = j 
                break
              
    print(start_x, start_y)            
    for i in routes:
        direct = i[0]
        move = int(i[2])
        if direct == "N":
            a = start_x - move
            if 0<=a and "X" not in park[a:start_x][start_y]:
                start_x = a
        elif direct == "S":
            a = start_x + move
            if a<n and "X" not in park[start_x+1:a+1][start_y]:
                start_x = a
        elif direct == "E":
            a = start_y + move
            if a<m and "X" not in park[start_x][start_y+1:a+1]:
                start_y = a
        else:
            a = start_y - move
            if 0<=a and "X" not in park[start_x][a:start_y]:
                start_y = a
                
    answer.append(start_x)
    answer.append(start_y)
          
    return answer