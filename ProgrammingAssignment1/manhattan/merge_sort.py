#!/usr/bin/env python3
# merge_sort.py

# Introduction to Algorithms, Fourth edition
# Linda Xiao

#########################################################################
#                                                                       #
# Copyright 2022 Massachusetts Institute of Technology                  #
#                                                                       #
# Permission is hereby granted, free of charge, to any person obtaining #
# a copy of this software and associated documentation files (the       #
# "Software"), to deal in the Software without restriction, including   #
# without limitation the rights to use, copy, modify, merge, publish,   #
# distribute, sublicense, and/or sell copies of the Software, and to    #
# permit persons to whom the Software is furnished to do so, subject to #
# the following conditions:                                             #
#                                                                       #
# The above copyright notice and this permission notice shall be        #
# included in all copies or substantial portions of the Software.       #
#                                                                       #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,       #
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF    #
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND                 #
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS   #
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN    #
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN     #
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE      #
# SOFTWARE.                                                             #
#                                                                       #
#########################################################################

def merge(A, p, q, r):
	"""Merge two sorted sublists/subarrays to a larger sorted sublist/subarray.

	Arguments:
	A -- a list/array containing the sublists/subarrays to be merged
	p -- index of the beginning of the first sublist/subarray
	q -- index of the end of the first sublist/subarray;
	the second sublist/subarray starts at index q+1
	r -- index of the end of the second sublist/subarray
	"""
	# Copy the left and right sublists/subarrays.
	# If A is a list, slicing creates a copy.
	if type(A) is list:
		left = A[p: q+1]
		right = A[q+1: r+1]
	# Otherwise a is a np.array, so create a copy with list().
	else:
		left = list(A[p: q+1])
		right = list(A[q+1: r+1])

	i = 0    # index into left sublist/subarray
	j = 0    # index into right sublist/subarray
	k = p    # index into a[p: r+1]

	# Combine the two sorted sublists/subarrays by inserting into A
	# the lesser exposed element of the two sublists/subarrays.
	#checking is modified to suit input list structure
	while i < len(left) and j < len(right):
		if left[i][2] <= right[j][2]:
			A[k] = left[i]
			i += 1
		else:
			A[k] = right[j]
			j += 1
		k += 1

	# After going through the left or right sublist/subarray, copy the 
	# remainder of the other to the end of the list/array.
	if i < len(left):  # copy remainder of left
		A[k: r+1] = left[i:]
	if j < len(right):  # copy remainder of right
		A[k: r+1] = right[j:]


def merge_sort(A, p=0, r=None):
	"""Sort the elements in the sublist/subarray a[p:r+1].

	Arguments:
	A -- a list/array containing the sublist/subarray to be merged
	p -- index of the beginning of the sublist/subarray (default = 0)
	r -- index of the end of the sublist/subarray (default = None)
	"""
	# If r is not given, set to the index of the last element of the list/array.
	if r is None:
		r = len(A) - 1
	if p >= r:  # 0 or 1 element?
		return
	q = (p+r) // 2            # midpoint of A[p: r]
	merge_sort(A, p, q)       # recursively sort A[p: q]
	merge_sort(A, q + 1, r)   # recursively sort A[q+1: r]
	merge(A, p, q, r)         # merge A[p: q] and A[q+1: r] into A[p: r]


# Testing
if __name__ == "__main__":
	
	test1 = [4,3,7,5,67]
	merge_sort(test1)
	print(test1)
	