class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map:Dict[int, int] = {}
        for n in nums:
            freq_map[n] = freq_map.get(n,0) +1

        freqs = sorted(freq_map.values())[-k:]
        min_threshold = min(freqs)
        return [k for k,v in freq_map.items() if v>=min_threshold]

