class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # TC: O(nlogn), SC: O(n)
        # Edge case:
        # if len(nums) < 2:
        #     return len(nums)

        # unique_nums = sorted(list(set(nums)))

        # count = 1
        # ans = 1
        # i = 0
        # j = 1

        # while j < len(unique_nums):
        #     if unique_nums[j] - unique_nums[i] == 1:
        #         count += 1
        #     else:
        #         ans = max(ans, count)
        #         count = 1
        #     i += 1
        #     j += 1

        # return max(ans, count)

        # TC: O(n), SC: O(n)
        set_num = set(nums)

        longest = 0

        for num in set_num:
            if num - 1 not in set_num:
                curr = num
                count = 1

                while curr + 1 in set_num:
                    curr += 1
                    count += 1

                longest = max(longest, count)

        return longest