class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        notebook = [0]*(n+1)
        def climb(n, total, notebook):
            if n== 1:
                a = 1
                total += a
            elif n == 2:
                a =2
                total += a
            else:
                x,y = notebook[n-1], notebook[n-2]
                if x != 0:
                    total = notebook[n-1] + climb(n-2, total, notebook)
                elif y != 0:
                    total += notebook[n-2] + climb(n-1, total, notebook)
                else:
                    total = climb(n-1, total, notebook) + climb(n-2, total, notebook)
            notebook[n] = total
            return total

        return climb(n, 0, notebook)

            
