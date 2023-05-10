class KthLargest:
    
    def __init__(self, k:int, nums:list[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
            
    def add(self, val:int)->int:
        
