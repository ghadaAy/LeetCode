class Solution:
   
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(haystack)
        if len(needle)>len(haystack):
            return -1
        if needle=='':
            return 0
        if needle in haystack:
            for i in range(len(haystack) - len(needle) + 1):
                s = haystack[i:i+len(needle)]
                if s == needle:
                    return i
        else: return -1