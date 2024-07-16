def intersection(nums1,nums2):
    list = []
    for i in nums1:
        for j in nums2:
            if (i == j):
                list.append(i)
                for k in nums1:
                    if (k == i):
                        nums1.remove(k)
    return list

print(intersection([1,2,2,1],[2,2]))