import time

def ft_progress(listy):
	lent = len(listy)
	old = time.time()
	t = 0
	for i in listy:
		now = time.time() - old
		prog = ((int((i/lent)*10) + 1)*'=')
		prog = prog + ' ' * (10 -len(prog))
		yield i
		if (not t):
			t = (time.time() - old ) * (lent + 1)
		print("ETA: %2.2fs [%3d%c] [%s>] %d/%d | elapsed time %2.2f"%( t, int((i/lent)*100) + 1, 37, prog, i + 1, lent, now) , end="\r")

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
time.sleep(0.01)
print()
print(ret)

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
	ret += elem
	time.sleep(0.005)
print()
print(ret)