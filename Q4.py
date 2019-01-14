'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

'''
Algorithm:
1) sort the list
2) loop through the list and skip the element if it is negative
3) Assume the current minimum not present in list to be 1
4) if the current element of list is equal to the curent minimun not in list
	then increment the current min not in list
5) if the case is none of the above, just exit the loop printing the
current min not in list. 
'''
lst = [0,-1,5,3]

def minPositive(lst):
	lst = sorted(lst)
	# [-1, 1, 3, 4]

	currMinNotInList = 1
	for i in lst:
		if i <= 0:
			continue

		elif i-currMinNotInList == 0:
			currMinNotInList += 1

		else:
			break

	print (currMinNotInList)


minPositive(lst)