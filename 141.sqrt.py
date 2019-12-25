class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        begin = 0
        end = x
        if x == 0:
            return 0
        if x == 1:
            return 1

        while True:
            mid = int((begin + end) / 2)
            if mid ** 2 == x:
                return mid
            # x处于[begin,end]中间的一个数
            # 如果mid**2 < x，且(mid+1) **2 >x，则mid为最接近于x的平方根
            if mid ** 2 < x < (mid + 1) ** 2:
                return mid
            elif mid ** 2 < x:
                begin = mid
                end = end
                continue
            else:
                begin = begin
                end = mid
                continue
