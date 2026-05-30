class Solution:
    def isPalindrome(self, s: str) -> bool:
        # TC: O(n), SC: O(n)
        # alphanumeric = "".join(c.lower() for c in s if 97 <= ord(c) <= 122 or 65 <= ord(c) <= 90 or 48 <= ord(c) <= 57)
        # alphanumeric = "".join(c.lower() for c in s if c.isalnum())
        # print(alphanumeric)
        # i = 0
        # j = len(alphanumeric) - 1

        # while i < j:
        #     if alphanumeric[i] != alphanumeric[j]:
        #         return False
        #     i += 1
        #     j -= 1

        # return True

        # TC: O(n), SC: O(1)
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i].isalnum() and s[j].isalnum() and s[i].lower() != s[j].lower():
                return False
            elif not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                i += 1
                j -= 1

        return True