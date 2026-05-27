class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # TC: O(n * n), SC: O(1)
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # TC: O(), SC: O(n)
        rem = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in rem:
                rem[nums[i]] = i
            else:
                return [rem[diff], i]