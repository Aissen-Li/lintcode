class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        n = len(numbers)
        numbers = sorted(numbers)
        result = numbers[0] + numbers[1] + numbers[2]
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                sums = numbers[i] + numbers[left] + numbers[right]
                if sums == target:
                    return target
                if sums < target:
                    left += 1
                if sums > target:
                    right -= 1
                if abs(sums - target) < abs(result - target):
                    result = sums
        return result


"""对于三个数的和而言是一个经典的算法"""