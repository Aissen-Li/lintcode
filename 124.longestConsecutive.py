class Solution:
    """
    @param num, a list of integer
    @return an integer
    """

    def longestConsecutive(self, num):
        nums = set(num)
        res = 0
        for currentNum in num:
            if currentNum in nums:
                tempLen = 0
                leftNum = currentNum - 1
                rightNum = currentNum + 1
                nums.remove(currentNum)
                while leftNum in nums:
                    nums.remove(leftNum)
                    tempLen += 1
                    leftNum -= 1
                while rightNum in nums:
                    nums.remove(rightNum)
                    tempLen += 1
                    rightNum += 1
                res = max(res, tempLen)
        return res


class Solution2:
    """
    @param num, a list of integer
    @return an integer
    """

    def longestConsecutive(self, num):
        res, nums = 0, set(num)
        for low in num:
            if low - 1 not in nums:
                high = low + 1
                while high in nums:
                    high += 1
                res = max(res, high - low)
        return res
