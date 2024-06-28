row = int(input("Please enter a row = "))

list = [[1],[1,1]]
row_list = []

i = 0
j = 0
k = 0
sum = 3

while (i < row):
    row_list.clear()
    row_list.insert(0, 1)
    row_list.insert(-1, 1)

    a = 1
    while (j < row):
        row_list.insert(i , sum)
        a += 1
        j += 1

    i += 1

print(list)