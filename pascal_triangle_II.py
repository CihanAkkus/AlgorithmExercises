row = int(input("Please enter a index of row = "))

list = [[1]]

for i in range(1,row+1):
    row_list = [1]
    for j in range(1,i):
        row_list.append(row_list_copy[j-1] + row_list_copy[j])
    row_list.append(1)

    row_list_copy = row_list.copy()
    list.append(row_list)

print(list[row])