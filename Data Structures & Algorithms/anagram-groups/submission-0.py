from typing import Dict, List 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups_hash:Dict[str,List[str]] = {} #default dict 
        
        for s in strs:
            list_group = groups_hash.get(str(sorted(s)),list())
            list_group.append(s) 
            groups_hash[str(sorted(s))] = list_group
        return list(groups_hash.values())
