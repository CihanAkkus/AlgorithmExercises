s = input("Please enter a sentence = ")

length = 0
last_length = 0

for i in s:
    if (i != " "):
        length += 1
        last_length = length
    elif (i == " "):
        length = 0

print(last_length)