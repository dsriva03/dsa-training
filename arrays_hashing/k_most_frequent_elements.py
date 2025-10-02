import heapq

def k_most_freq(nums, k):
    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0)+1
    
    heap = []

    for num, freq in counts.items():
        heapq.heappush(heap, (freq, num))

        if len(heap) > k:
            heapq.heappop(heap)
        
    result = []

    for freq, num in heap:
        result.append(num)
    
    return result

    
