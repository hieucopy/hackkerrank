n = int (input())
s=input()
s_list=''

list=[]
def check_xuathien():
    if s in s_list:
        return 0
    return 1
def check():
    for x in list:
        if x=='0' :
            return 0
            break
    return 1
for i in range(n):
    list.append('0')
    num=10
    k=1
    count=0
while num==10:
    s_list=''.join(list)
    if check_xuathien()==1:
        count+=1
    for charac_id, charac in enumerate(list):
        if charac=='1':
            list[charac_id]='0'
        else:
            list[charac_id]='1'
            break
    num=num*k
    if check()==1:
        k=0
        
print(count)