class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = -float('inf')
        monotonic_stack = [] # num(index, height)
        
        for i in range(len(heights)):
            start = i
            largest = max(largest, heights[i])

            while monotonic_stack and heights[i] <= monotonic_stack[-1][1]:
                idx, height = monotonic_stack.pop()
                largest = max(largest,((i - idx) * height))
                start = idx
            
            monotonic_stack.append((start, heights[i]))
        
        for idx, height in monotonic_stack:
            largest = max(largest,((len(heights) - idx) * height))
        return largest