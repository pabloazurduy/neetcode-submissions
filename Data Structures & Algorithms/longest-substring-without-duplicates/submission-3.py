class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest =0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if len(set(s[i:j+1])) == len(s[i:j+1]):
                    longest = max(len(s[i:j+1]), longest)
                    j +=1
                else:
                    i += 1
        return longest