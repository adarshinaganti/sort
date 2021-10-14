from helpers import *
import numpy as np
import time

def main():
	N = int(input("Enter number of array elements: "))
	arr = np.round(np.linspace(10, 1000, N), 0)
	np.random.shuffle(arr)
	print("")

	print("Unsorted array: ")
	printArray(arr)
	print("")

	choice = input("Enter sorting algorithm of choice (selection, bubble, insertion, merge, quick): ")
	print("")

	if "selection" in choice.lower():
		t = time.perf_counter()
		selectionSort(arr)
		f = time.perf_counter() - t
		print("Sorted array: ")
		printArray(arr)
		print(f"{choice.lower()} sort: finished in {f * 1E3:.1f} ms")

	elif "bubble" in choice.lower():
		t = time.perf_counter()
		bubbleSort(arr)
		f = time.perf_counter() - t
		print("Sorted array: ")
		printArray(arr)
		print(f"{choice.lower()} sort: finished in {f * 1E3:.1f} ms")
	
	elif "insertion" in choice.lower():
		t = time.perf_counter()
		insertionSort(arr)
		f = time.perf_counter() - t
		print("Sorted array: ")
		printArray(arr)
		print(f"{choice.lower()} sort: finished in {f * 1E3:.1f} ms")
	
	elif "merge" in choice.lower():
		t = time.perf_counter()
		mergeSort(arr)
		f = time.perf_counter() - t
		print("Sorted array: ")
		printArray(arr)
		print(f"{choice.lower()} sort: finished in {f * 1E3:.1f} ms")
	
	elif "quick" in choice.lower():
		t = time.perf_counter()
		quickSort(0, len(arr) - 1, arr)
		f = time.perf_counter() - t
		print("Sorted array: ")
		printArray(arr)
		print(f"{choice.lower()} sort: finished in {f * 1E3:.1f} ms")
	
	else: print("Invalid input. Available inputs: selection, bubble, insertion, merge, quick")

if __name__ == "__main__": main()