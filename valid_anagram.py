def isAnagram(s,t):
    if (len(s) == len(t)):
        for i in s:
            for j in t:
                if (i == j):
                    character_to_remove = j
                    t = t.replace(character_to_remove, "")
        if (t == ""):
            return True
        else:
            return False
    else:
        return False