class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute force
        # TC: O(nlogn), SC: O(n)
        # count = {}

        # for num in nums:
        #     # count.setdefault(num, 0)
        #     # count[num] += 1
        #     count[num] = count.get(num, 0) + 1

        # count = sorted(count.items(), key=lambda item: item[1], reverse=True)
        
        # res = []

        # for num in count:
        #     if len(res) < k:
        #         res.append(num[0])
        #     else:
        #         break

        # return res

        # Using Bucket Sort
        # TC: O(n), SC: O(n)
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]

        for key, c in count.items():
            freq[c].append(key)

        res = []

        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)

                if len(res) == k:
                    return res