def singleNumber(nums):
    count = 0
    for i in nums:
        for j in nums:
            if (i != j):
                count += 1
        if (count == len(nums) - 1):
            print(i)
            break
        elif (count != len(nums) - 1):
            count = 0
