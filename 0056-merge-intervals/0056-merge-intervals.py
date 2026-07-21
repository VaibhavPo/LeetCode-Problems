class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        Ans = []
        intervals.sort(key=itemgetter(0))
        first=float('-inf')
        last=float('-inf')
        for i in intervals:
            if last < i[0]:
                first = i[0]
                last = i[1] 
                Ans.append([first,last])

            if last >= i[0] and last < i[1]:
                Ans.remove([first,last])
                last = i[1]
                Ans.append([first,last])
        return Ans
