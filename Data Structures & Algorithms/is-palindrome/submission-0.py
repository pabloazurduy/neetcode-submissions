class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = ''.join([c for c in s[::-1].lower() if c.isalnum()])
        org = ''.join([c for c in s.lower() if c.isalnum()])
        return rev == org