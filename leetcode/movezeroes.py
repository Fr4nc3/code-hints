# Python implementation to move all zeroes at
# the end of array

# function to move all zeroes at
# the end of array
def moveZerosToEnd (arr, n):

	# Count of non-zero elements
	count = 0;


	# Traverse the array. If arr[i] is non-zero, then
	# update the value of arr at index count to arr[i]
	for i in range(0, n):
		if (arr[i] != 0):
			arr[count] = arr[i]
			count+=1
	
	# Update all elements at index >=count with value 0
	for i in range(count, n):
		arr[i] = 0



# function to print the array elements
def printArray(arr, n):

	for i in range(0, n):
		print(arr[i],end=" ")


# Driver program to test above
arr = [ 0, 1, 9, 8, 4, 0, 0, 2,
	7, 0, 6, 0, 9 ]
n = len(arr)

print("Original array:", end=" ")
printArray(arr, n)

moveZerosToEnd(arr, n)

print("\nModified array: ", end=" ")
printArray(arr, n)


