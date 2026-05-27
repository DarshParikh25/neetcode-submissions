class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # TC: O(n*n), SC: O(n)
        # TC: O(nlogn), SC: O(n)
        # nums = sorted(nums)

        # for i in range(0, len(nums) - 1):
        #     j = i + 1
        #     if nums[i] == nums[j]:
        #         return True

        # return False


        # TC: O(n), SC: O(n)
        hashSet = set()

        for num in nums:
            if num in hashSet:
                return True

            hashSet.add(num)

        return False

        # Alternate python-ish version
        # TC: O(n), SC: O(n)
        # return len(nums) != len(set(nums))