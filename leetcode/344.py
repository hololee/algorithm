class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ldx, rdx = 0, len(s) - 1

        while (ldx < rdx):
            s[ldx], s[rdx] = s[rdx], s[ldx]
            ldx += 1
            rdx -= 1