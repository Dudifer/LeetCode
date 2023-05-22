print("Date started: 5/18/23")
print("Date completed: 5/18/23")
def threeConsecutiveOdds(self, arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    oddcounter=0
    for n in arr:
        if (n//2)*2==n:
            oddcounter=0
        else: 
            oddcounter+=1
            if oddcounter==3:
                return True
    return False