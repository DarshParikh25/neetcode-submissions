from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Edge case:
        if len(s) != len(t):
            return False

        # TC: O(nlogn), SC: O(n)
        # sortedS = sorted(s)
        # sortedT = sorted(t)

        # for i in range(len(sortedS)):
        #     if sortedS[i] != sortedT[i]:
        #         return False

        # return True

        count = defaultdict(int)

        for i in range(len(s)):
            # count.setdefault(s[i], 0)
            # count[s[i]] += 1
            # count.setdefault(t[i], 0)
            # count[t[i]] -= 1

            # if s[i] not in count:
            #     count[s[i]] = 1
            # else:
            #     count[s[i]] += 1

            # if t[i] not in count:
            #     count[t[i]] = -1
            # else:
            #     count[t[i]] -= 1

            # For defaultdict only,
            count[s[i]] += 1
            count[t[i]] -= 1

        for val in count.values():
            if val != 0:
                return False

        return True