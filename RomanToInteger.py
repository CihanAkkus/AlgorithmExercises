s = input("Please enter a roman number = ")

values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
}

sum = 0
j = 0
for i in range(0,len(s)-1):
                if (values[s[i]] >= values[s[i+1]]):
                        sum += values[s[i]]
                else:
                        sum -= values[s[i]]

sum += values[s[-1]]

print(sum)