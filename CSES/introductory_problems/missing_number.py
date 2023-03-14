n = int(input())
nums = {i for i in range(1, n + 1)}
exc = list(map(int, input().split()))
for num in exc:
    nums.remove(num)
print(nums.pop())

