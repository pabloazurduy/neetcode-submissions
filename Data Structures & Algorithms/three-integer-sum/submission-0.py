import itertools as it
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets:List[List[int]] = []
        for trip in it.permutations(nums,3):
            if sum(trip)==0:
                triplets.append(trip)
        triplets = set([tuple(sorted(trip)) for trip in triplets])
        triplets = [list(trip) for trip in triplets ]
        return triplets