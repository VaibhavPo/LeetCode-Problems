import copy
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        num = 2 * n
        result = []
        def generate(index,subset, total):
            if index >= num:
                if total == 0:
                    # print ("YO SUBSET  ", subset)
                    result.append("".join(subset))
                return
            
            if total > n:
                return
            if total < 0:
                return
            subset.append("(")
            sum = total + 1
            generate(index+1, subset, sum)
            subset.pop()
            sum = total -1
            subset.append(")")
            generate(index+1, subset, sum)
            subset.pop()
            # print (subset)
        
        generate(0,[],0)
        return result




            

        