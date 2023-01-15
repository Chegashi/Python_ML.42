import time
import math


def ft_progress(listy):
    lent = len(listy)
    old = time.time()
    eta = 0
    for i in listy:
        now = time.time() - old
        _prog = math.ceil(((abs(i - listy[0]) + 1) / lent) * 100)
        prog_s = math.ceil(_prog / 2) * '='
        prog_s += ' ' * (50 - len(prog_s))
        yield i
        if (not eta):
            eta = (time.time() - old) * (lent - i + 1)
        msg = "ETA: %2.2fs [%3d%c] [%s>] %d/%d | elapsed time %2.2f" % \
            (eta, _prog, 37, prog_s, i + 1, lent, now)
        print(msg, end='\r')
    old = time.time()

