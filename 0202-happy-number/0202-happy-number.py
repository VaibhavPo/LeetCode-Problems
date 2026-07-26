class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        loop = [n]
        
        while True:
            total = 0
            # for di in (str(n)):
            #     d= int(di)
            #     total += (d*d)
            while n > 0:
                d = n % 10
                total += (d*d)
                n //= 10
            print(total)
            
            if total == 1:
                return True
            elif total in loop:
                return False
            else:
                loop.append(total)
                n = total
            



        