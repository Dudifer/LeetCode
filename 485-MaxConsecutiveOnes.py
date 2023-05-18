def findMaxConsecutiveOnes(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    mco=0
    cco=0
    for i in nums:
        if i==1:
            cco+=1
            if cco>mco:
                mco=cco
        if i ==0:
            cco=0
    return mco