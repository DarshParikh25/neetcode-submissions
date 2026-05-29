class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # TC: O(n), SC: O(n)
        total = 1
        zeros = set()
        flag = False

        for i in range(len(nums)):
            if nums[i] != 0:
                flag = True
                total *= nums[i]
            else:
                zeros.add(i)

        if len(zeros) > 1:
            return [0] * len(nums)

        res = []

        if zeros:
            for i in range(len(nums)):
                if i in zeros and flag:
                    res.append(total)
                else:
                    res.append(0)
        else:
            for num in nums:
                res.append(int(total/num))

        return res