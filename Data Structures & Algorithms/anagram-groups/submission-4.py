from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # TC: O(nklogn), SC: O(nk)
        # groups = {}

        # for str in strs:
        #     key = "".join(sorted(str))

        #     groups.setdefault(key, [])
        #     groups[key].append(str)

        # return list(groups.values())

        # TC: O(nk), SC: O(nk)
        groups = defaultdict(list)

        for str in strs:
            count = [0] * 26

            for char in str:
                count[ord(char) - ord('a')] += 1

            groups[tuple(count)].append(str)

        return list(groups.values())