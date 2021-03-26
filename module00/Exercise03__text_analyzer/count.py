def text_analyzer(*texts):
    """    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    if len(texts) != 1:
        print("ERROR")
    elif len(texts) == 0 and len(texts[1]) == 0:
        print("What is the text to analyse?")
    else:
        nbr_upper = 0
        nbr_lower = 0
        nbr_space = 0
        nbr_ponctuation = 0
        for c in texts[0]:
            if c.isupper():
                nbr_upper += 1
            elif c.islower():
                nbr_lower += 1
            elif c.isspace():
                nbr_space += 1
            elif not c.isdigit():
                nbr_ponctuation += 1
        print('The text contains characters:', len(texts[0]))
        print("- ", nbr_upper, " upper letters")
        print("- ", nbr_lower, " lower letters")
        print("- ", nbr_ponctuation," punctuation marks")
        print("- ", nbr_space," spaces")