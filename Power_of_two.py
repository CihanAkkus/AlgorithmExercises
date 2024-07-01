def is_power_of_two(num):
    num = abs(num)
    if num == 0:
        return False
    return (num & (num - 1)) == 0

num = int(input("Please enter a number = "))

print(is_power_of_two(num))