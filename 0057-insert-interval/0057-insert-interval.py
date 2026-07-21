class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        Ans =[]
        
        first = float('-inf')
        last = float('-inf')
        intervals.append (newInterval)
        intervals.sort(key=itemgetter(0))
     
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
