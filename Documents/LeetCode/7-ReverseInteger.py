class Solution(object):
	"""docstring for Solution"""
	def reverseInteger(self, num):
		if num >= 0:
			numstr = str(num)
			isNegative = 1
		else:
			numstr = str(num * -1)
			isNegative = -1
		numlist = list(numstr)
		index1 = 0
		index2 = len(numstr) - 1
		while index1 < index2:
			temp = numlist[index1]
			numlist[index1] = numlist[index2]
			numlist[index2] = temp
			index1 += 1
			index2 -= 1
		numstr = ''.join(numlist)
		print int(numstr)
		if int(numstr) * isNegative < 2147483648 and int(numstr) * isNegative >= -2147483648:
			return int(numstr) * isNegative
		else:
			return 0

if __name__ == '__main__':
	num1 = 1493398
	num2 = -429345
	num3 = 2147483646
	solution = Solution()
	print solution.reverseInteger(num1)
	print solution.reverseInteger(num2)
	print solution.reverseInteger(num3)
		