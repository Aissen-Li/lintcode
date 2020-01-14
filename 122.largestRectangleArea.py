class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, heights):
        heights = [0] + heights + [0]
        res = 0
        stack = []

        for index, height in enumerate(heights):
            while stack and height < height[stack[-1]]:
                poppedIndex = stack.pop()
                leftIndex = stack[-1] + 1
                res = max(heights[poppedIndex] * (index - leftIndex))
            stack.append(index)
        return res
