class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        seen = set(nums)
        longest = 1
        for num in nums:
            print("current num:", num)
            print("current seen:", seen)
            seen.add(num)
            seq_len = 1
            seq_num = num
            while seq_num + 1 in seen:
                print("found in seen:", seq_num+1)
                seq_len += 1
                seq_num += 1

            # seq_num = num
            # while seq_num - 1 in seen:
            #     seq_len += 1
            #     seq_num -= 1
            longest = max(seq_len, longest)
        
            # print("longest", longest)


        return longest