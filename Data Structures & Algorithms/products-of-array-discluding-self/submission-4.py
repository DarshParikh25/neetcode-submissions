class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # TC: O(n), SC: O(n)
        total = 1
        zeros = set()

        for i, num in enumerate(nums):
            if num == 0:
                zeros.add(i)
            else:
                total *= num

        if len(zeros) > 1:
            return [0] * len(nums)

        res = []

        if len(zeros) == 1:
            for i in range(len(nums)):
                # if i in zeros:
                if i == next(iter(zeros)):
                    res.append(total)
                else:
                    res.append(0)
        else:
            for num in nums:
                res.append(total // num)

        return res