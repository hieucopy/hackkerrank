n=int(input())
for i in range(n):
    
    string_pos=input()
    string_now=input()
    list_pos=string_pos.split(' ')
    list_now=string_now.split(' ')
    time=list_pos[5]
    hour=int(time[0:3])
    min=int(time[3:])
    time_need=hour*3600+min*60
    time=list_now[5]
    hour=int(time[0:3])
    min=int(time[3:])
    
    time=list_pos[4]
    hour=int(time[0:2])
    min=int(time[3:5])
    second=int(time[6:8])
    time_need1=hour*3600+min*60+second
    time=list_now[4]
    hour=int(time[0:2])
    min=int(time[3:5])
    second=int(time[6:8])
    time_need1=time_need1-(hour*3600+min*60+second)
    
    time_need=time_need+hour*3600+min*60
    time=3600*(int(list_pos[1])-int(list_now[1]))-time_need+time_need1
    print(time, time_need)