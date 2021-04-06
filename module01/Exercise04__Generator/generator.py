import random

def generator(text, sep , option=None):
    li = text.split(sep)
    if (not isinstance(text, str)):
        print("ERROR")
        quit()
    elif (option == None):
        return li
    elif (option == "shuffle"):
        li_int = []
        liste = []
        i = 0
        while  i < len(li):
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

text = "Le Lorem Ipsum est simplement du Le faux texte."

for word in generator(text, sep=" ", option="unique"):
    print(word)