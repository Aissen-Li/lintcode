class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        n = len(numbers)
        numbers = sorted(numbers)
        result = []
        for i in range(n - 2):
            if numbers[i] > 0:
                break
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                sums = numbers[i] + numbers[left] + numbers[right]
                if sums == 0:
                    result.append([numbers[i], numbers[left], numbers[right]])
                    left += 1
                    right -= 1
                    while numbers[left] == numbers[left + 1] and left < right:
                        left += 1
                    while numbers[right] == numbers[right - 1] and right > left:
                        right -= 1
                if sums < 0:
                    left += 1
                if sums > 0:
                    right -= 1
        return result


"""需要注意去重，因为不能出现重复的三元组，很有意义的一道题目"""