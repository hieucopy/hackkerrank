def minion_game(string):
    count_conso=count_vowel=0
    for i in range(1,len(string)):
        number_split=i
        string1=string
        while number_split>0 :
            list_string=(tach_chuoi(i, string1))
            number_split=number_split-1
            string1=string1[1:]
            for string_need_check in list_string:
                if check(string_need_check)==1:
                    count_conso=count_conso+1
                else :
                    count_vowel=count_vowel+1
    if check(s)==1 :
        count_conso=count_conso+1
    else :
        count_vowel=count_vowel+1
        
    if (count_conso>count_vowel):
        print('Keivin '+str(count_conso))
    else:
        print('Stuart '+str(count_vowel))
def tach_chuoi(n, s):
    pairs=[]
    for i in range(0, len(s), n):
        pair=s[i:i+n]
        if len(pair)==n:
            pairs.append(pair)
    return pairs
def check(s):
    vowels=['A','E','O','I','U']
    if s[0] in vowels:
        return 1
    else:
        return 0


if __name__ == '__main__':
    s = input()
    minion_game(s)