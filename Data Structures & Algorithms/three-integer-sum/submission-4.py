class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Brute Force
        # TC: O(n * n * n), SC: O(n * n)
        # possibilities = set()

        # for index, num in enumerate(nums):
        #     for i in range(index + 1, len(nums) - 1):
        #         for j in range(i + 1, len(nums)):
        #             if num + nums[i] + nums[j] == 0:
        #                     possibilities.add(tuple(sorted([num, nums[i], nums[j]])))

        # print("possibilities", possibilities)

        # return list(possibilities)

        # Optimal Solution
        # TC: O(n * n)
        nums = sorted(nums)

        res = set()

        for index, num in enumerate(nums):
            i = index + 1
            j = len(nums) - 1

            while i < j:
                total = nums[i] + nums[j]

                if total == -num:
                    res.add(tuple([num, nums[i], nums[j]]))
                    i += 1
                    j -= 1
                elif total < -num:
                    i += 1
                else:
                    j -= 1

        print("res", res)

        return list(res)