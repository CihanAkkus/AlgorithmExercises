num = int(input("Please enter a number = "))
num2 = num
num3 = num
Digit = 1

i = 0

while True:
    if (num == 0):
        print(num,"is armstrong number")
        break
    if (int(num / 10) == 0):
        break
    num = int(num / 10)
    Digit += 1
#print("Digit number =",Digit)

i = 0
sum = 0
while (i < Digit):
    sum += (num2 % 10) ** Digit
    #print("sum =",sum)
    num2 = int(num2 / 10)
    #print(num2)
    i += 1
if (sum == num3):
    print(num3,"is armstrong number")
else:
    print("It is not a armstrong number!")