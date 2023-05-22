class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n==1:
            return [-1,2]
        else:
            return [n-1,1]