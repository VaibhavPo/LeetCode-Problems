class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = []
        dic = {
            2: ["a", "b", "c"],    3: ["d", "e", "f"],
            4: ["g", "h", "i"],    5: ["j", "k", "l"],
            6: ["m", "n", "o"],    7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],    9: ["w", "x", "y", "z"]
        }
        def iterate(ind, subset):
            if ind >= len(digits):
                ans.append("".join(subset[:]))
                # print("YO   ",subset)
                return
            
            
            digit = int(digits[ind])
            
            for i in dic.get(digit):
                subset.append(i)
                # print(subset)
                iterate(ind + 1, subset)
                subset.pop()

        iterate(0, [])
        # print(ans)
        return ans


            
