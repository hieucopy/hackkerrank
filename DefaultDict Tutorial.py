
    
n, m = map(int, input().split())
5
list_n=list_m=[]
for i in range(n):
    char_in=input()
    list_n.append(char_in)
my_dict={}
for i in range(m):
    char_in=input()
    my_dict[char_in]=[]
    
for index, charac in enumerate(list_n):
    
    temp_list=my_dict[charac]
    temp_list.append(str(index+1))
    my_dict[charac]=temp_list
for dis in my_dict.values():
    if len(dis)==0:
        print(-1)
    else:
        str_out=''
        str_out=' '.join(dis)
        print (str_out)

"""
5 2
a
a
b
a
b
a
b
"""