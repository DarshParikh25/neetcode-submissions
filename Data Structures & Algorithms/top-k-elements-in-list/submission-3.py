class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute force
        # TC: O(nlogn)
        count = {}

        for num in nums:
            count.setdefault(num, 0)
            count[num] += 1

        count = sorted(count.items(), key=lambda item: item[1], reverse=True)
        
        res = []

        for num in count:
            if len(res) < k:
                res.append(num[0])
            else:
                break

        return res