from collections import deque

d = deque()
commands = [input().split() for _ in range(int(input()))]
for command in commands:
    if command[0] == 'pop':
        d.pop()
    elif command[0] == 'popleft':
        d.popleft()
    elif command[0] == 'append':
        d.append(command[1])
    else:
        d.appendleft(command[1])

for elements in d:
    print(elements, end=" ")
