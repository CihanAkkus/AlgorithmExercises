
"""
this question is not over yet, I will continue with the solution. 

"""



list1 = [1,2,4]
list2 = [1,3,4]

list3 = []

for i in range(0,len(list1)):
    """
    if (list1[i] <= list2[i]):
        list3.append(list1[i])
    if (list1[i] == list2[i]):
        list3.append(list2[i])
        """

    for j in range(0,len(list2)):
        if (list1[i] < list2[j]):
            list3.append(list1[i])
            if (list2[j] < list1[i + 1]):
                list3.append(list2[j])

            break
        elif (list1[i] == list1[j]):
            list3.append(list2[j])
            list3.append(list1[i])
            break
print(list3)