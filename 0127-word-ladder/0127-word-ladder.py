# import copy
from collections import deque
import string
# import heapq
class Solution(object):

    # NON OPTIMAL APPROACH( USING DIJKASTRA)
    # def matchChar(self,a,b):
    #     return sum(x != y for x, y in zip(a, b))
    
    # def ladderLength(self, beginWord, endWord, wordList):
    #     """
    #     :type beginWord: str
    #     :type endWord: str
    #     :type wordList: List[str]
    #     :rtype: int
    #     """
    #     w_list = copy.deepcopy(wordList)
    #     w_list.insert(0,beginWord)
    #     n = len(w_list)
    #     if endWord in w_list:
    #         ind = w_list.index(endWord)
    #     else:
    #         return 0

    #     adj_l = [[]for _ in range(n)]
    #     dis = [float('inf')]* n
    #     heap = []
    #     for i in range(n):
    #         for j in range(i+1,n):
    #             if i != j:
    #                 a,b = w_list[i], w_list[j]
    #                 x=self.matchChar(a,b)
    #                 if x == 1:
    #                     adj_l[i].append([1, j])
    #                     adj_l[j].append([1, i])
        
    #     dis[0] = 0
    #     heapq.heappush(heap, [0, 0])        
    #     while len(heap) >0:

    #         d, node =heapq.heappop(heap)
    #         if d > dis[node]:
    #             continue
    #         for i in adj_l[node]:
    #             dd, no = i
    #             if dis[no] > 1 + d:
    #                 dis[no] = 1 + d
    #                 heapq.heappush(heap,[dis[no], no])
    #     if dis[ind] == float('inf'):
    #         return 0
    #     return dis[ind] +1

    # Using BFS
    def ladderLength(self, beginWord, endWord, wordList):
        # wordList.insert( 0,beginWord)
        word_set = set(wordList)
        n= len(wordList)
        vis = set()
        n1 = len(beginWord)
        count =0
        
        if endWord not in wordList:
            return 0

        def loopAlphabets(word):            
            vis.add(word)
            ans =[]
            for i in range(n1):
                for letter in string.ascii_lowercase:
                    n_word = word[:i] + letter + word[i+1:]
                    # print ('fn called', n_word, " ", word[i],letter )
                    if n_word in word_set and n_word not in vis:
                        ans.append(n_word)
                        vis.add(n_word)
            return ans
     
        q = deque([beginWord])
        while q :
            count += 1
            for _ in range(len(q)):
                word = q.popleft()
                temp = loopAlphabets(word)
                # print(li)
                q.extend(temp)
                if endWord in temp:
                    return count +1

        return 0
    



