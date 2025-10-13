import heapq

def k_largest(nums, k):
    heap = []

    for num in nums:
        heap.heappush(num)

        if len(heap) > k:
            heapq.heappop(heap)
    
    return heapq.heappop(heap)