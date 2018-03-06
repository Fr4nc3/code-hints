# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,
# "pwke" is a subsequence and not a substring.

def lengthOfLongestSubstring( s):
    """
    :type s: str
    :rtype: int
    """
    ar = []
    for i in range(0, len(s)):
        #print(s[i])
       # for j in range(1, len(s)):
        if s[i] not in ar:
            ar.append(s[i])
        # else:
        #     ar.pop(0)
    return len(ar)


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
