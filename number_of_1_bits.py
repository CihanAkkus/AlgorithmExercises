num = int(input("Please enter a number = "))


list = []

while (True):
    remainder = num % 2
    list.append(remainder)
    num = num // 2
    if (num == 0):
        list.reverse()
        break

sum = 0

for j in list:
    sum += j

print(sum)