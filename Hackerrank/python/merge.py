import string

def merge_the_tools(string, k):
    
    groups = []
    sen = ''
    flag = 0
    
    for char in string:
        sen += char
        flag += 1
        if flag == k:     
            groups.append(sen)
            sen = ''
            flag = 0

    for group in groups:
        sen = ''
        for char in group:
            if(sen.count(char) == 0):
                sen += char
        print(sen)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    