class Solution:
    def longestPalindrome(self, s: str) -> str:

        def check_expand(start, end):
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1

            # start and end already expanded.    
            return s[start + 1:end]

        if len(s) < 2 or s == s[::-1]:
            return s
        else:
            result = ''

            for i in range(len(s) - 1):
                result = max(result, check_expand(i, i + 1), check_expand(i, i + 2), key=len)

        return result

