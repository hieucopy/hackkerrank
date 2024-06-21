if __name__ == '__main__':
    n=input()
    x=n.split()
   
    sum=0
    for i in x:
        sum=sum+int(i)
   
    sum=sum/len(x)
    print(f'{sum:.2f}')