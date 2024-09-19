def commonChars(words):
    list = []
    for i in range(0,len(words)-2):

        for j in range(0,len(words[i])-1):

            if (words[i][j] in list):
                continue


            for k in range(0,len(words[i + 1])-1):

                if (words[i][j] == words[i][k]):
                    list.append(words[i][j])

    return list

print(commonChars(["bella","label","roller","lüleburgaz","lale"]))