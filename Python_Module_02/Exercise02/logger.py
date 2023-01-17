import time
from random import randint

file = open('machine.log', 'w')

def log(func):
	old = time.time()
	def wrappedFunc(*args, **kward):
		ret = func(*args, **kward)
		timing = time.time() - old
		if (timing > 1):
			time_str = str(round(timing, 3)) + ' s '
		else:
			time_str = str(round(timing * 1000, +3)) + ' ms'
		if timing < 10 :
			time_str = ' ' + time_str
		string = str(func)
		start = string.find('.') + 1
		end = string[start:].find(' ')
		func_name = string[start:start + end]
		func_name += ' ' *( 25 - len(func_name))
		txt = '(cmaxime)Running: ' + func_name + '[ exec-time = '+ time_str + ' ]\n'
		file.write(str(txt))
		return ret
	return wrappedFunc

class CoffeeMachine():
	water_level = 100

	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False

	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")

	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")

if __name__ == "__main__":

    machine = CoffeeMachine()
    for i in range(0, 5):
    	machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)

file.close()class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.name = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self, data):
        with open(self.name, 'w') as f:
            str1 = self.sep.join([str(elm) for elm in data])
            f.write('\n' + str)
        f.close()

    def __exit__(self):
        return