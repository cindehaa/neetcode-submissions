class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[] for _ in range(2 ** len(nums))]

        for i, num in enumerate(nums):
            freq = 2**(len(nums)-1-i)
            for j, subset in enumerate(subsets):
                if (j // freq) % 2 == 0:
                    subset.append(num)
        
        return subsets



            