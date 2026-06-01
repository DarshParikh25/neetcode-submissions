class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            current = 0
            if heights[left] < heights[right]:
                current = (right - left) * heights[left]
                left += 1
            elif heights[left] > heights[right]:
                current = (-(left - right)) * heights[right]
                right -= 1
            else:
                current = (right - left) * heights[left]
                left += 1
                right -= 1
            largest = max(largest, current)

        return largest