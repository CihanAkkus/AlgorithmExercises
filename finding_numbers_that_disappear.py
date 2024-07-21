def findDisappearedNumbers(nums):
    list = []
    for i in range(1,len(nums)+1):
        if (not(i in nums)):
            list.append(i)
    return list







