class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = defaultdict(int)

        for i, num in enumerate(nums):
            if num in complements: 
                return [complements[num], i]

            else:
                complement = target - num
                complements[complement] = i