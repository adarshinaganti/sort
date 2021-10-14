def selectionSort(A):
	for i in range(len(A)):
		min_idx = 1
		for j in range(i + 1, len(A)):
			if A[min_idx] > A[j]: min_idx = j
		A[i], A[min_idx] = A[min_idx], A[i]

def bubbleSort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(0, n - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertionSort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1

		while j >= 0 and key < arr[j]:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key

def mergeSort(arr):
	if len(arr) > 1:
		mid = len(arr) // 2
		L = arr[mid:]
		R = arr[:mid]
		mergeSort(L)
		mergeSort(R)

		i = j = k = 0

		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1
		
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1
		
		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

def partition(start, end, arr):
	idx = start
	pivot = arr[idx]

	while start < end:
		while start < len(arr) and arr[start] <= pivot: start += 1
		while arr[end] > pivot: end -= 1
		if start < end: arr[start], arr[end] = arr[end], arr[start]

	arr[end], arr[idx] = arr[idx], arr[end]
	return end

def quickSort(start, end, arr):
	if start < end:
		p = partition(start, end, arr)
		quickSort(start, p - 1, arr)
		quickSort(p + 1, end, arr)

def printArray(arr):
	for i in range(len(arr)):
		print(arr[i], end = ' ')
	print()