class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len_sub = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                sub = s[i:j]
                if len(set(sub))==len(sub) and len(sub)>max_len_sub:
                    max_len_sub = len(sub)   
                
        return max_len_sub