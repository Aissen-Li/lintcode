class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 1

        n = len(nums)
        hashed = [0] * n
        for i in range(n):
            if nums[i] > 0 and nums[i] <= n:
                hashed[nums[i] - 1] += 1

        for i in range(n):
            if hashed[i] == 0:
                return i + 1
        return n + 1


"""哈希表来存储1到n的内容。先遍历一遍原数组，将原数组中的1-n的整数存入哈希表对应0到n-1的位置。
再对哈希表进行遍历，遍历到存储内容为空的，则返回遍历到整数的索引值，即为第一个丢失的正整数"""


def first_missing_number(li):
    size = len(li)
    li.insert(0, None)  # 为了方便从1开始数，在数组前面添加None占位
    i = 1
    while i <= size:
        if li[i] < i or li[i] > size:
            li[i] = li[size]
            size -= 1
        elif li[i] > i:
            # 交换
            temp = li[i]
            li[i] = li[temp]
            li[temp] = temp
        else:
            i += 1
    return i


"""
假定前i-1个数已经找到，并且依次存放在A[1,2,…,i-1]中，继续考察A[i]： 
若A[i]＜i且A[i]≥1，则A[i]在A[1,2,…,i-1]中已经出现过，可以直接丢弃。 
若A[i]为负，则更应该丢弃它。 
若A[i]＞i且A[i]≤N，则A[i]应该位于后面的位置上，则将A[A[i]]和A[i]交换。 
若A[i]≥N，由于缺失数据一定小于N，则A[i]丢弃。 
若A[i]＝i，则A[i]位于正确的位置上，则i加1，循环不变式扩大，继续比较后面的元素
"""