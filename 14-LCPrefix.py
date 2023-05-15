print("Date started: 5/14/23")
print("Date completed: 5/14/23")
print("/nObjective:/n/tWrite a function to find the longest common prefix string amongst an array of strings.")
def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    l_0=len(strs[0])
    for i in range(200):
        if i<l_0:
            c=strs[0][i]
        else:
            return strs[0][:i]
        for s in strs[1:]:
            if i<len(s):
                if s[i]!=c:
                    return strs[0][:i]
            else:
                return strs[0][:i]
