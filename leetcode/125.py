class Solution:
    def isPalindrome(self, s: str) -> bool:
        sen = []
        for c in s:
            if c.isalnum():
                sen.append(c.lower())
        while (len(sen) > 1):
            if sen.pop(0) != sen.pop():
                return False

        return True

