def moveZeroes(nums):
    for i in range(0,len(nums)-1):
        if (nums[i] == 0):
            nums[i],nums[i+1] = nums[i+1],nums[i]
    return nums

print(moveZeroes([1,0,3,0,12]))