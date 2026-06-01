class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # TC: O(n), SC: O(1)
        # largest = 0

        # left = 0
        # right = len(heights) - 1

        # while left < right:
        #     current = 0
        #     if heights[left] < heights[right]:
        #         current = (right - left) * heights[left]
        #         left += 1
        #     elif heights[left] > heights[right]:
        #         current = (-(left - right)) * heights[right]
        #         right -= 1
        #     else:
        #         current = (right - left) * heights[left]
        #         left += 1
        #         right -= 1
        #     largest = max(largest, current)

        # return largest

        # Ceaner Code
        # TC: O(n), SC: O(1)
        largest = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            largest = max(largest, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return largest