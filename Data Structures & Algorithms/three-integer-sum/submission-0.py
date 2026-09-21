class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        inverses = defaultdict(set) # this will be the k's that we look for

        for i, num_i in enumerate(nums):
            for j, num_j in enumerate(nums[i+1:]):

                inverses[num_i + num_j].add((i, j+i+1))
        
        triplets = []
        for k, num_k in enumerate(nums):
            if -num_k not in inverses: continue

            for idx_pairs in inverses[-num_k]:
                if k in idx_pairs: continue

                triplets.append([nums[idx_pairs[0]], nums[idx_pairs[1]], nums[k]])
        
        triplets = [list(triplet_b) for triplet_b in set([tuple(sorted(triplet)) for triplet in triplets])]
        return triplets


        
