from heapq import heappush, heappushpop
class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        maxheap, minheap, res = [], [], []
        for num in nums:
            if len(maxheap) == len(minheap):
                if maxheap and num > -maxheap[0]:
                    num = heappushpop(minheap, num)
                heappush(maxheap, -num)
            else:
                if num < -maxheap[0]:
                    num = -heappushpop(maxheap, -num)
                heappush(minheap, num)
            res.append(-maxheap[0])
        return res
