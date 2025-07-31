def remove_even(nums):
    for n in nums:
        if n % 2 == 0:
            nums.remove(n)
    return nums

print(remove_even([1, 2, 3, 4, 5, 6]))
