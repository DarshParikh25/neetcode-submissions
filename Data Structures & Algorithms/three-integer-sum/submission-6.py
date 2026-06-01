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
        # TC: O(n * n), SC: O(n * n)
        # nums = sorted(nums)

        # res = set()

        # for index, num in enumerate(nums):
        #     i = index + 1
        #     j = len(nums) - 1

        #     while i < j:
        #         total = nums[i] + nums[j]

        #         if total == -num:
        #             res.add(tuple([num, nums[i], nums[j]]))
        #             i += 1
        #             j -= 1
        #         elif total < -num:
        #             i += 1
        #         else:
        #             j -= 1

        # print("res", res)

        # return list(res)

        # Avoiding set Solution
        # TC: O(n * n), SC: O(n * n)
        nums.sort()

        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total > 0:
                    r -= 1

                elif total < 0:
                    l += 1

                elif total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res