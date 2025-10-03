def product_of_arr(nums: list[int]) -> list[int]:
    result = [1] * len(nums)

    prefix = 1

    for i in range(len(nums)):
        result[i] = prefix
        prefix = prefix * nums[i]

    suffix = 1

    for i in range(len(nums) - 1, -1, -1):
        result[i] = suffix * result[i]
        suffix = suffix * nums[i]

    return result

print(product_of_arr([2,3,5]))