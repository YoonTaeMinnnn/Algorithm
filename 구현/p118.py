#0:북쪽, 1:동쪽, 2:남쪽, 3:서쪽 

n, m = map(int,input().split())
input_data = list(map(int, input().split()))


inital_loc = input_data[:2]   #초기 위치
direct = input_data[2]    # 초기 방향

print(inital_loc, direct)


location_map= [[0]*m for _ in range(n)]  #현재위치 체크맵
print(location_map)

location_map[input_data[0], input_data[1]]=1

dx = [-1,0,1,0]  #북 동 남 서
dy = [0,-1,0,1]  #북 동 남 서
stratify = {0:[0,-1],1:[-1,0],2:[0,1],3:[1,0]}

game_map = []
for _ in range(n):
  game_map.append(list(map(int, input().split())))

print(game_map)

while True:
  


  
