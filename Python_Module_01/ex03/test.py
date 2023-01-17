from generator import generator

# text = "Le Lorem Ipsum est simplement du faux texte."
# for word in generator(text, sep=" "):
#     print(word)

# for word in generator(text, sep=" ", option="shuffle"):
#     print(word)

# for word in generator(text, sep=" ", option="ordered"):
#     print(word)

# text = "Lorem Ipsum Lorem Ipsum"
# for word in generator(text, sep=" ", option="unique"):
#     print(word)

# text = ""
# for word in generator("4", sep=" ", option='sss'):
#     print(word)

# text = 1.0
# for word in generator(text, sep="."):
#     print(word)

# text="This is a simple string for a basic test. Very simple."


# for word in generator(text, sep=" "):
#     print(word)

# for word in generator(text, sep="."):
#     print(word)

# for word in generator(text, sep="i"):
#     print(word)

# for word in generator(text, sep="si"):
    # print(word)

text="0 1 2 3 4 5 6 7 8 9"
for word in generator(text, sep=" ", option='shuffle'):
    print(word)
