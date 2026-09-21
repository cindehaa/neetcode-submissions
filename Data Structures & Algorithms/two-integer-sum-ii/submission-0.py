class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while True:
            num_sum = numbers[start] + numbers[end]
            if num_sum == target: return [start + 1, end + 1]
            elif num_sum < target:
                start += 1
            else:
                end -= 1
        
        print("we should never get here")
        return [0,0]