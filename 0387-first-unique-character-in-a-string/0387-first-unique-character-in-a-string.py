class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashMap ={}
        for i in s:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1
        print (hashMap)
        for i,ch in enumerate(s):
            if hashMap[ch] == 1:
                return i
        return -1

       