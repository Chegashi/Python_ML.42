import random


def generator(text, sep, option=None):
    if (not isinstance(text, str)):
        print("ERROR")
        li = []
        exit(1)
    li = text.split(sep)
    if (not option):
        return li
    elif (option == "shuffle"):
        li_int = []
        liste = []
        i = 0
        while i < len(li):
            nbr = random.randint(0, len(li) - 1)
            if nbr not in li_int:
                li_int.append(nbr)
                i += 1
        for index in li_int:
            liste.append(li[index])
        return liste
    elif (option == "ordered"):
        return sorted(li)
    elif (option == "unique"):
        liste = []
        for word in li:
            if word not in liste:
                liste.append(word)
        return liste
