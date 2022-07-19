class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        s=str1+str2
        i=min(len(str1),len(str2))
        while(i>=1):
            if(len(str1)%i==0 and len(str2)%i==0):
                t=i
                break;
            i-=1
        i=0
        j=0
        while(i<len(s)):
            if(j==t):
                j=0
            if(s[i]!=str1[j]):
                break;
            j+=1
            i+=1
        if(i==len(s)):
            return str1[:t]
        return ''