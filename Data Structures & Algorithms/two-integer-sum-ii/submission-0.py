class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i,n in enumerate(numbers):
            for j in range(i,len(numbers)):
                if n+numbers[j]==target:
                    return [i+1,j+1]
                 