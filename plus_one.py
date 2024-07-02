num = input("Plaese enter a number = ")
list = []
for i in num:
    list.append(int(i))

if (list[-1] != 9):
    list[-1] += 1

else:
    if (num == "9"):
        list[0] = 0
        list.insert(0,0)
    for i in range(len(list)-1,0,-1):
        list[-1] = 0
        list[i - 1] += 1
        if (list[i - 1] == 10):
            if (list[i - 1] == list[0]):
                list[i - 1] = 0
                list.insert(0,1)
                break
            list[i - 1] = 0

        else:
            break
        
print(list)