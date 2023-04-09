n, m, k = tuple(map(int, input().split()))
sizes_desired = list(map(int, input().split()))
apartment_sizes = list(map(int, input().split()))
sizes_desired.sort()
apartment_sizes.sort()
i = j = count = 0
while i < n and j < m:
    if apartment_sizes[j] < sizes_desired[i] - k:
        j += 1
    elif apartment_sizes[j] > sizes_desired[i] + k:
        i += 1
    else:
        j += 1
        i += 1
        count += 1
print(count)