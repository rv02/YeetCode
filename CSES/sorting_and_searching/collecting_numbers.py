n = int(input())
min = n + 1
count = 1
pos = [0 for _ in range(min)]
nums = list(map(int, input().split()))
for i, num in enumerate(nums):
    pos[num] = i
for i in range(n):
    if pos[i+1] < pos[i]:
        count += 1
print(count)
