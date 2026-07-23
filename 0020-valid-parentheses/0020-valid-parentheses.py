class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for i in s:

            if i == "(" or i =="{" or i=="[":
                if i =="(" :
                    stack.append(1)
                elif i == "{" :
                    stack.append(2)
                elif i== "[":
                    stack.append(3)
                
                
            
            elif (i== ")" or i =="}" or i == "]") and stack:
                #Closing bracket
                if stack[-1] ==1 and i ==")":
                    stack.pop()
                elif stack[-1] ==2 and i =="}":
                    stack.pop()
                elif stack[-1] ==3 and i =="]":
                    stack.pop()
                else:
                    return False
            else:
                return False 

        if not stack:
            return True
        else:
            return False

