class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # TC: O(nlogn), SC: O(n)
        if len(s) != len(t):
            return False

        sortedS = sorted(s)
        sortedT = sorted(t)

        for i in range(len(sortedS)):
            if sortedS[i] != sortedT[i]:
                return False

        return True