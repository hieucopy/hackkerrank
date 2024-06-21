n,m=map(int,input().split())
dict={}
string_root=input()
list_root=string_root.split(' ')
for i in range (n):
    x=list_root[i]
    if x in dict:
        temp=dict[x]
        temp=temp+1
        dict[x]=temp
    else:
        dict[x]=1
point=0
sum=0
string1=input()
list1=string1.split(' ')

for i in range(m):
    x=list1[i]
    if x in dict:
        point=point+ dict[x]
string2=input()
list2=string2.split(' ')
for i in range(m):
    x=list2[i]
    if x in dict:
        point=point- dict[x]
print(point)  
