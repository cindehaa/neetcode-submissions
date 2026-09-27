class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged







'''
[1,3] [1,5] [6,7]

[1,3] [1,5] [6,7]



[1,3] [10,13] [2,4] [1,5] [2,6] [16,18]
-------------------------------
[1,3] [1,5] [2,4] [2,6] [10,13] [16,18]
[1,3] [2,4] [1,5] [2,6] [10,13] [16,18]



'''