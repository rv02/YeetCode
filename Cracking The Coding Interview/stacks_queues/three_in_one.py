from typing import List, Tuple

# Yuck
def solve(q,queries):
    stack: List[Tuple] = []
    for query in queries:
        if query[0] == 0:
            if query[1]:
                stack.append((0, query[2]))
            else:
                if stack and stack[-1][0] == 0:
                    print(stack.pop()[1])
                else:
                    print(-1)
        elif query[0] == 1:
            if query[1]:
                stack.insert(0, (1, query[2]))
            else:
                if stack and stack[0][0] == 1:
                    print(stack.pop(0)[1])
                else:
                    print(-1)
        else:
            mid_pos = 0
            for elem in stack:
                if elem[0] != 1:
                    break
                mid_pos += 1
            if query[1]:
                stack.insert(mid_pos, (2, query[2]))
            else:
                if stack and len(stack) > mid_pos and stack[mid_pos][0] == 2:
                    print(stack.pop(mid_pos)[1])
                else:
                    print(-1)

file = './small/in/input3.txt'
f = open(file, 'r')
for _ in range(int(f.readline())):
    queries = []
    for _ in range(int(f.readline())):
        query = list(map(int, f.readline().split(' ')))
        queries.append(query)
    solve(len(queries), queries)