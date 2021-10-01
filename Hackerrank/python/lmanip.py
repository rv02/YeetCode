if __name__ == '__main__':
    n = int(input())
    f_me = []
    for i in range(n):
        command = list(map(str, input().strip().split()))
        if command[0] == 'insert':
            f_me.insert(int(command[1]), int(command[2]))
        elif command[0] == 'remove':
            f_me.remove(int(command[1]))
        elif command[0] == 'print':
            print(f_me)
        elif command[0] == 'append':
            f_me.append(int(command[1]))
        elif command[0] == 'sort':
            f_me.sort()
        elif command[0] == 'pop':
            f_me.pop()
        else:
            f_me.reverse()

