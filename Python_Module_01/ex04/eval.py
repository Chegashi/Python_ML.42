class Evaluator:
    def __init__():
        pass

    @staticmethod
    def zip_evaluate(str1, str2):
        if len(str1) != len(str2):
            return -1
        ret = 0
        for elem in zip(str1, str2):
            ret += elem[0] * len(elem[1])
        return ret

    @staticmethod
    def enumerate_evaluate(str1, str2):
        if len(str1) != len(str2):
            return -1
        ret = 0
        for elem in zip(str1, str2):
            ret += elem[0] * len(elem[1])
        return ret
