if __name__ == '__main__':
    n, m = map(int,input().split(' '))
    arr = list(map(int,input().split(' ')))
    A = set(map(int,input().split(' ')))
    B = set(map(int,input().split(' ')))
    sum = 0
    for i in arr:
        if i in A:
            sum += 1
        elif i in B:
            sum -= 1
    print(sum)
