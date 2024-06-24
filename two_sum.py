nums = [2,7,11,15]

target = 9
a = 0
for i,value1 in enumerate(nums):
    for j, value2 in enumerate(nums):
        if (value1 + value2 == target):
            print(i,end = " ")