class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = []
        for i in reversed(xrange(len(s))):
            if s[i] == '-':
                continue
            if len(result) % (k + 1) == k:
                result += '-'
            result += s[i].upper()
        return "".join(reversed(result))