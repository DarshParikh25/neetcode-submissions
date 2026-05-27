class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # O(nlogn)
        # nums = sorted(nums)

        # for i in range(0, len(nums) - 1):
        #     j = i + 1
        #     if nums[i] == nums[j]:
        #         return True

        # return False

        # O(n)
        # hashSet = set()

        # for num in nums:
        #     if num in hashSet:
        #         return True

        #     hashSet.add(num)

        # return False

        # Alternate python-ish version
        return len(nums) != len(set(nums))