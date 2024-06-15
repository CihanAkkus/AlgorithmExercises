units =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
tenth = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def reading_num(num):
    for i in range(1,10):
        i *= 10
        if((num - (num % 10)) == i):
            i = int(i / 10)
            print(tenth[i], end = " ")
    for i in range(1,10):
        if(num % 10 == i):
            print(units[i])

reading_num(78)