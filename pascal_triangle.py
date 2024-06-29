row = int(input("Please enter a row = "))

list = [[1]]
row_list = []

sum = 0

for i in range(1,row):
    row_list.clear()
    row_list.insert(0, 1)
    row_list.insert(-1, 1)

    for j in range(1,i):
        sum = (row_list_copy[j-1] + row_list_copy[j])
        row_list.insert(j , sum)
        sum = 0

    row_list_copy = row_list.copy()
    list.append(row_list.copy())


print(list)