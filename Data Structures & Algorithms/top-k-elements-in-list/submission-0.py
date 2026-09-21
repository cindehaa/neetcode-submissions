class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        
        freq_arr =[[] for n in range(len(nums) + 1)]
        for key, v in freq_map.items():
            freq_arr[v].append(key)

        k_most_freq = []
        for i in range(len(nums), 0, -1):
            if freq_arr[i]:
                for j in freq_arr[i]:
                    k_most_freq.append(j)
                    if len(k_most_freq) == k: return k_most_freq
                   
    
        return k_most_freq


