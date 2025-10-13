import heapq

def k_largest_element(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)
    
    return heapq.heappop(heap)