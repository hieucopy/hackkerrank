def merge_the_tools(string, k):
    # your code goes here
    list_string=[]
    for index in range(0,len(string),k):
        sub_string=''
        for i in range(0,k):
            sub_string=sub_string+ string[index+i]
        print(process(sub_string))  
    
def process(s):
    list=[]
    for charac in s:
        if charac not in list:
            list.append(charac)
    return("".join(list))
if __name__ == '__main__':
   # string, k = input(), int(input())
    k=3
    string='AABCAAADA'
    merge_the_tools(string, k)