'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the 
original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected 
output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

import numpy as np
lst = [1,2,3,4,5]

'''
Algorithm:
1) Construct a temporary list left[] such that left[i] contains product of all elements on left of lst[i] excluding lst[i].
2) Construct another temporary list right[] such that right[i] contains product of all elements on on right of lst[i] excluding lst[i].
3) To get product, multiply left[] with right[].
'''
# 1)
ProductLeft = 1
left = []

for i in range(len(lst)):
	left.append(ProductLeft)
	ProductLeft *= lst[i]

# 2)
ProductRight = 1
right = []

for i in range(len(lst)-1,-1,-1):
	right.append(ProductRight)
	ProductRight *= lst[i]

right.reverse()

# 3)
final = np.multiply(left,right)
print (final)