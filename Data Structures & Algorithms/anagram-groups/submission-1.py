from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups:Dict[str,List[str]] = defaultdict(list)
        for ss in strs:
            groups[''.join(sorted(ss))].append(ss)
        return groups.values()
