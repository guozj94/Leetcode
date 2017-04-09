class Solution_Hash(object):
	"""docstring for Solution"""
	def twoSum(self, nums, target):
		hashTable = {}
		for i in range(0, len(nums)):
			x = nums[i]
			if target - x in hashTable:
				return [i, hashTable[target - x]]
			hashTable[x] = i

class Solution_DualIndice(object):
	"""docstring for ClassName"""
	def twoSum(self, nums, target):
		array = nums[:len(nums)]
		array.sort()
		index1 = 0
		index2 = len(array) - 1
		while array[index1] + array[index2] != target and index1 < index2:
			if array[index1] + array[index2] > target:
				index2 -= 1
			elif array[index1] + array[index2] < target:
				index1 += 1
		index1_origin = 0
		index2_origin = 0
		for i in range(len(nums)):
			if nums[i] == array[index1]:
				index1_origin = i
			elif nums[i] == array[index2]:
				index2_origin = i
		return [index1_origin, index2_origin]




if __name__ == '__main__':
    nums = [3,4,3,90]
    target = 6
    solution = Solution_Hash()
    print solution.twoSum(nums,target)
    solution1 = Solution_DualIndice()
    print solution1.twoSum(nums, target)


# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].