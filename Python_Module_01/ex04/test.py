from eval import Evaluator

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(coefs, words))
print(Evaluator.enumerate_evaluate(coefs, words))

words = ["Le", "Lorem", "Ipsum", "n", "est", "pas", "simple"]
coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
print(Evaluator.zip_evaluate(coefs, words))
print(Evaluator.enumerate_evaluate(coefs, words))

print(Evaluator.zip_evaluate(None, None))
print(Evaluator.enumerate_evaluate(None, None))

print(Evaluator.zip_evaluate([1, 2, 3], []))
print(Evaluator.enumerate_evaluate([1, 2, 3], []))

print(Evaluator.zip_evaluate([1, 2, 3], ["word", 2, "wordo"]))
print(Evaluator.enumerate_evaluate([1, 2, 3], ["word", 2, "wordo"]))