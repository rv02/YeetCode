seq = input()
prev = seq[0]
curr = max = 1
for c in seq[1:]:
    if c == prev:
        curr += 1
    else:
        max = curr if curr > max else max
        curr = 1
    prev = c
print(curr if curr > max else max)
