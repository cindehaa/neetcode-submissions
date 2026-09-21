import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == 0 and len(self.max_heap) == 0: 
            heapq.heappush(self.max_heap, -num)
            return
        if len(self.max_heap) == 1 and len(self.min_heap) == 0:
            if num >= -self.max_heap[0]: heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.min_heap, -self.max_heap[0])
                heapq.heappop(self.max_heap)
                heapq.heappush(self.max_heap, -num)
            return

        l = -self.max_heap[0]
        r = self.min_heap[0]

        # goes into the min heap
        if num >= self.min_heap[0]:
            # case 1: can add it
            if len(self.min_heap) < len(self.max_heap):
                heapq.heappush(self.min_heap, num)
            # case 2: need to swap
            else: 
                # put r into l's heap
                heapq.heappush(self.max_heap, -self.min_heap[0])
                # get rid of r
                heapq.heappop(self.min_heap)
                # put num into r
                heapq.heappush(self.min_heap, num)
        else: # goes into the maxheap
            if len(self.max_heap) <= len(self.min_heap):
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, -self.max_heap[0])
                heapq.heappop(self.max_heap)
                heapq.heappush(self.max_heap, -num)

        return

        

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap): return (self.min_heap[0] + -self.max_heap[0])/2
        elif len(self.min_heap) > len(self.max_heap): return self.min_heap[0]
        else: return -self.max_heap[0]
        

        