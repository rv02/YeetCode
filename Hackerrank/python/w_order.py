from collections import OrderedDict

len = int(input())
arr = []
unique = OrderedDict()
l = 0
for i in range(len):
    arr.append(input())
for word in arr:
    if word not in unique.keys():
        unique[word] = 1
        l += 1
    else:
        unique[word] += 1

print(l)
for i in unique.values():
    print(i, end = ' ')


