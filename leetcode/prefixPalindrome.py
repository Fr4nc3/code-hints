def solution(s):
    n = len(s)
    maxLen = 0
    for i in range (n+1):
        temp = s[0:i]
        m = len(temp)
        print(temp)
        print(temp[::-1])
        if temp == temp[::-1] and m>=2:
            maxLen = i
            s = s.lstrip(temp)
    return s[0:maxLen] if maxLen >1 else s
# You are given a string s. Consider the following algorithm applied to this string:

# Take all the prefixes of the string, and choose the longest palindrome between them.
# If this chosen prefix contains at least two characters, cut this prefix from s and go back to the first step with the updated string. Otherwise, end the algorithm with the current string s as a result.
# Your task is to implement the above algorithm and return its result when applied to string s.

# Note: you can click on the prefixes and palindrome words to see the definition of the terms if you're not familiar with them.

# Example

# For s = "aaacodedoc", the output should be solution(s) = "".

# The initial string s = "aaacodedoc" contains only three prefixes which are also palindromes - "a", "aa", "aaa". The longest one between them is "aaa", so we cut if from s.
# Now we have string "codedoc". It contains two prefixes which are also palindromes - "c" and "codedoc". The longest one between them is "codedoc", so we cut if from the current string and obtain the empty string.
# Finally the algorithm ends on the empty string, so the answer is "".
# For s = "codesignal", the output should be solution(s) = "codesignal".
# The initial string s = "codesignal" contains the only prefix, which is also palindrome - "c". This prefix is the longest, but doesn't contain two characters, so the algorithm ends with string "codesignal" as a result.

# For s = "", the output should be solution(s) = "".


def checkPalindrome(prefix):
      prefArr = [c.lower() for c in prefix if c.isalnum()]
  return prefArr == prefArr[::-1]

def prefixPalindrome(s):
  arr1 = []
  arr2 = []
  i = 0
  j = 1
  while j <= len(s):
    arr1.append(s[i:j])
    j += 1
  arr1.sort(key=len)
  for item in arr1:
    if checkPalindrome(item) == True and len(item) >= 2:
      arr2.append(item)
  if len(arr2) == 0:
    return s
  else:
    woi = s.strip(arr2[-1])
    if woi != None:
      prefixPalindrome(woi)
    return ''

if __name__ == '__main__':
  s1 = 'aaacodedoc'
  s2 = 'codesignal'
  s3 = ''
  print(prefixPalindrome(s1))  output- ''
  print(prefixPalindrome(s2))  output- codesignal
  print(prefixPalindrome(s3))  output- ''