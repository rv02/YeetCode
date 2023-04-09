import numpy as np

t = int(input())

for _ in range(t):
    a, b = tuple(map(int, input().split()))
    eq = np.array([[1, 2],
                  [2, 1]])
    sol = np.array([a, b])
    x, y = tuple(np.linalg.solve(eq, sol))
    if x.is_integer() and y.is_integer() and x >= 0 and y >= 0:
        print('Yes')
    else:
        print('No')
    