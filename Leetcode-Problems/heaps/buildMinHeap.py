def buildMinHeap(arr):
	# Write your code here.
	# Return a list.
    for i in range(1, len(arr)):
        j = (i - 1) // 2
        while i > 0:
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                i = j
            else:
                break
            j = (j - 1) // 2
    return arr

print(buildMinHeap('9 8 7 1 -1'.split(' ')))