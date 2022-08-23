import sys

def text_analyzer(texts = ""):
    """    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    if not isinstance(texts, str):
        print("AssertionError: argument is not a string")
    else:
        if len(texts) == 0:
            print("What is the text to analyze?")
            texts = sys.stdin.readline()
        nbr_upper = 0
        nbr_lower = 0
        nbr_space = 0
        nbr_ponctuation = 0
        for c in texts:
            if c.isupper():
                nbr_upper += 1
            elif c.islower():
                nbr_lower += 1
            elif c.isspace():
                nbr_space += 1
            elif not c.isdigit():
                nbr_ponctuation += 1
        print('The text contains characters:', len(texts))
        print("- ", nbr_upper, " upper letters")
        print("- ", nbr_lower, " lower letters")
        print("- ", nbr_ponctuation," punctuation marks")
        print("- ", nbr_space," spaces")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error")
    else :
        text_analyzer("Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles.")
        text_analyzer("Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.")
        text_analyzer()
        text_analyzer(42)
        print(text_analyzer.__doc__)