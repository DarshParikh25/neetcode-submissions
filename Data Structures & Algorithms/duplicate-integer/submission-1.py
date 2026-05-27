class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        
        for i in range(0, len(nums) - 1):
            j = i + 1
            if nums[i] == nums[j]:
                return True

        return False