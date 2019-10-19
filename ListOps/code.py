'''
Task: Delete alternate elements of the given list, starting from index 0,
      print the list after each traversal.

Example: given list -> [1,2,3,4,5]
                o/p: [2, 4]
                     [4]
                     []

'''

nums = [3, 5, 2, 9, 101, 333, 4]

while nums:
	n = []
	x=len(nums)
	for i in range(x):
		if i%2!=0:
			n.append(nums[i])
	nums = n
	print(n)
