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
"""Solution (Java)
class Solution {
    public String longestCommonPrefix(String[] strs) {
        Arrays.sort(strs);
        String s1 = strs[0];
        String s2 = strs[strs.length-1];
        int idx = 0;
        while(idx < s1.length() && idx < s2.length()){
            if(s1.charAt(idx) == s2.charAt(idx)){
                idx++;
            } else {
                break;
            }
        }
        return s1.substring(0, idx);
    }
    
    The reason why we sort the input array of strings and compare the first and last strings is 
    that the longest common prefix of all the strings must be a prefix of the first string 
    and a prefix of the last string in the sorted array. This is because strings are ordered 
    based on their alphabetical order (Lexicographical order).
    
    By first sorting, then comparing only the first and last strings of the sorted array, 
    we can easily find the longest common prefix.

}"""