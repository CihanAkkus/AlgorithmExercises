def intersection(nums1,nums2):
    list = []
    copy_nums2 = nums2[:]
    for i in nums1:
        if (i in copy_nums2):
            list.append(i)
            for j in nums2:
                if (j == i):
                    copy_nums2.remove(j)
    return list