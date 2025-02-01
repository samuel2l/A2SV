class Solution:
    def longestCommonPrefix(self, strs):
        smallest=1000
        sm=''
        for i in strs:
            if len(i)<smallest:
                smallest=len(i)
                sm=i
        strs.remove(sm)

        k=0
        isSolved=False
        while isSolved==False:
            for i in range(len(strs)):
                if strs[i].startswith(sm):
                    strs.remove(strs[i])
                    
                    break
                else:
                    sm=sm[:len(sm)-1]

                    break
            if len(sm)<=0 or len(strs)==0:
                isSolved=True
                break
        
        return sm

        