def solution(wallpaper):
    max_row = 0
    min_row = 1470000
    max_col = 0
    min_col = 1470000

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                if i > max_row:
                    max_row = i
                if i < min_row:
                    min_row = i
                if j > max_col:
                    max_col = j
                if j < min_col:
                    min_col = j
                    
    print(max_row+1, min_row, max_col+1, min_col)
    answer = []
    answer.append(min_row)
    answer.append(min_col)
    answer.append(max_row+1)
    answer.append(max_col+1)
    return answer