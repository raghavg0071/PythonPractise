'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

# harcoding the list 
lst = [10, 15, 3, 7]
k = 16

'''
Algorithm that is applied is as follows:
sorting the array and starting the addition from the extreme ends
if the sum is greater than k then move one step left from the extreme right
else if the sum is less than k then move one step right from the extreme left
keep repeating this until you reach the middle.
'''
lst = sorted(lst)
LeftIndex = 0
RightIndex = len(lst)-1

for i in range(len(lst)):
	'''
	the first if statement is cleverly choosen to be at first so that other cases are not checked and directly
	breakout from the loop
	'''
	if RightIndex <= LeftIndex :
		print ("No Luck This Time")
		break

	elif lst[LeftIndex]+lst[RightIndex] > k:
		RightIndex -=1

	elif lst[LeftIndex]+lst[RightIndex] < k:
		LeftIndex +=1

	elif lst[LeftIndex]+lst[RightIndex] == k:
		print ("The Number exists as sum of Two elements in the given List")
		break