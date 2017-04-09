class Solution(object):
    def isPalindrome(self, x):
        isNegative = 1
        if x < 0:
            isNegative = -1
        old = x * isNegative
        new = 0
        while old != 0:
            new = new * 10 + old % 10
            old = int(old / 10)
        if x == new * isNegative and new * isNegative < 2147483648 and new * isNegative >= -2147483648:
            return True
        else:
            return False

if __name__ == '__main__':
    x1 = 1234321
    x2 = 2147483649
    solution = Solution()
    print solution.isPalindrome(x1)
    print solution.isPalindrome(x2)