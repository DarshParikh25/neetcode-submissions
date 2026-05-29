class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # TC: O(nlogn), SC: O(1)
        # Edge case:
        if len(nums) < 2:
            return len(nums)

        unique_nums = sorted(list(set(nums)))

        count = 1
        ans = 1
        i = 0
        j = 1

        while j < len(unique_nums):
            if unique_nums[j] - unique_nums[i] == 1:
                count += 1
            else:
                ans = max(ans, count)
                count = 1
            i += 1
            j += 1

        return max(ans, count)