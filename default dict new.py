n, m = map(int, input().split())
dict={}
for i in range(n):
    x=input()
    temp=dict[x]
    temp=temp.append(i+1)
    dict[x]=temp
print(dict)