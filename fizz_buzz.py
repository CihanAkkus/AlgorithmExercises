list = []

def fizz_buzz(num):
    for i in range(1,num+1):
        if (i % 15 == 0):
            list.append("FizzBuzz")
        elif (i % 3 == 0):
            list.append("Fizz")
        elif (i % 5 == 0):
            list.append("Buzz")
        else:
            list.append(str(i))
    return list

print(fizz_buzz(15))