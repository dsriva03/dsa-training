import heapq

def top_k_heap(nums: list[int], k: int) -> result[list]:
    #make a frequency map for nums
    map = {}

    for num in nums:
        map[num] = map.get(num, 0) + 1

    #make a heap
    heap = []

    #iterate over the frequency map and push key, value pairs into the heap
    for num, freq in map.items():
        #if heap size is larger than k, pop off the smallest element
        heapq.heappush(heap, (freq, num))

        if len(heap) > k:
            heapq.heappop(heap)

    #return the numbers from the heap
    return [num for freq, num in heap]

