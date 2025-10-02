import heapq

def topKFrequent(nums, k):
    #build frequency map
    freq_map = {}
    for n in nums: 
        freq_map[n] = freq_map.get(n, 0) + 1
    
    #step 2: push into min heap of size k
    heap = []
    for num, freq in freq_map.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
        
    #step 3: extract just the numbers
    return [num for freq, num in heap]

print(topKFrequent([1,1,1,2,2,3], 2))   # [1,2]
print(topKFrequent([5,5,6,5,6,7,7,7,7], 2))  # [5,7]
print(topKFrequent([4], 1))  # [4]


