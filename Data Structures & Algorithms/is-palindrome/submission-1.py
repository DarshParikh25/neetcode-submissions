class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = "".join(c for c in s if 97 <= ord(c) <= 122 or 65 <= ord(c) <= 90 or 48 <= ord(c) <= 57).lower()
        print(alphanumeric)
        i = 0
        j = len(alphanumeric) - 1

        while i < j:
            if alphanumeric[i] != alphanumeric[j]:
                return False
            i += 1
            j -= 1

        return True