def moveZeroes(nums):
    a = 0
    for k in nums:
        if (k == 0):
            a += 1
    for j in range(0,a):
        for i in range(0, len(nums) - 1):
            if (nums[i] == 0):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums
