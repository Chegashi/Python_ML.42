from time import sleep
from loading import ft_progress
from tqdm import tqdm

test_X = {
    range(100),
    range(100000),
    range(3333),
    range(100, 200),
    range(1),
    range(4),
    range(0, -100, -1)
}

def test(X):
    ret = 0
    for elem in ft_progress(X):
        ret += (elem + 3) % 5
    # sleep(0.01)
    print()
    print(ret)

for X in test_X:
    print('\t', X)
    # for x in tqdm(X):
    #     pass
    test(X)

