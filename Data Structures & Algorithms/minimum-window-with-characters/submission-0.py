from collections import Counter 
class Solution:
    def contains(self, s:str, t:str) -> bool:
        hash_s = Counter(s)
        hash_t = Counter(t)
        return all([hash_s[char]>=hash_t[char] for char in hash_t])

    def minWindow(self, s: str, t: str) -> str:
        substring = ''
        substring_inc = 0 
        for window_size in range(len(t), len(s)+1):
            for i in range(0, len(s)-window_size+1):
                if self.contains(s[i:i+window_size], t):
                    return s[i:i+window_size]
        return substring
