class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = [] #[index, height]
        for i, height in enumerate(heights):
            index = i
        
            while len(stack) > 0 and stack[-1][1] > height:
                lastStackIndex = stack[-1][0]
                lastStackHeight = stack[-1][1]
                area = (i - lastStackIndex) * lastStackHeight
                res = max(res, area)
                stack.pop()
                index = lastStackIndex

            stack.append([index,height])

        while len(stack) > 0:
            lastStackIndex = stack[-1][0]
            lastStackHeight = stack[-1][1]
            area = (len(heights) - lastStackIndex) * lastStackHeight
            res = max(res, area)
            stack.pop()
        
        return res