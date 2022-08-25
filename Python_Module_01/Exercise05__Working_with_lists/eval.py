class Evaluator:
    def __init__():
        pass

    def zip_evaluate(str1, str2):
        if len(str1) != len(str2):
            return -1
        ret = 0
        for elem in zip(str1, str2):
            ret += elem[0] * len(elem[1])
        return ret

    def enumerate_evaluate():
        pass

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(coefs, words))
