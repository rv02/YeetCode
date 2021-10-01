def minion_game(string):
    sub_str = [] 
    length = len(string)
    vowels = 'AEIOU'
    vow = con = 0
    i = 0
    while i < length:
        if string[i] in vowels:
            vow += length - i
        else:
            con += length - i
        i += 1 

    if(vow > con):
        print('Kevin', vow)
    elif(con > vow):
        print('Stuart', con)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
