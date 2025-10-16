def binary_search(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        #print(f"left={left}, mid={mid}, right={right}, nums[mid] = {nums[mid]}")
        

        if nums[mid] == target:
            return mid
        
        elif target < nums[mid]:
            right = mid - 1
            #print(f"-> move right to {right}")
        else:
            left = mid + 1
            #print(f"-> move left to {left}")
    
    return - 1

nums = [-1, 0, 3, 5, 9, 12]

print(binary_search(nums, 9))   # → 4
print(binary_search(nums, 2))   # → -1
print(binary_search(nums, -1))  # → 0
print(binary_search(nums, 12))  # → 5
print(binary_search([], 5))     # → -1