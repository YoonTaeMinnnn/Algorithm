num = int(input())
#종료시간이 이른 순으로 정렬
times = [list(map(int,input().split())) for _ in range(num)]
times.sort(key = lambda x : (x[1],x[0]))



cnt=0
end_time= 0



for i in times:
  if i[0]>=end_time:
    cnt+=1
    end_time = i[1]
  

print(cnt)



