from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Edge case
        if len(strs) < 2:
            return [strs]

        # TC: O(nklogn), SC: O(nk)
        groups = {}

        for str in strs:
            key = "".join(sorted(str))

            groups.setdefault(key, [])
            groups[key].append(str)

        return list(groups.values())

        # TC: O(nk), SC: O(n)
        # ordinals = defaultdict()

        # for i, str in enumerate(strs):
        #     ordinals[i] = sum([ord(s) for s in str])

        # segregatedDict = {}

        # for key, val in ordinals.items():
        #     segregatedDict.setdefault(val, [])
        #     segregatedDict[val].append(strs[key])

        # return list(segregatedDict.values())