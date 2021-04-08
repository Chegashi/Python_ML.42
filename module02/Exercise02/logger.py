import time
from random import randint
	
def log(func):
	file = open('machine.log', 'a')
	old = time.time()
	def wrappedFunc(*args, **kward):
		string = str(func)
		start = string.find('.') + 1
		end = string[start:].find(' ')
		func_name = string[start:start + end]
		ret = func(*args, **kward)
		txt = f"""(cmaxime)Running: %20s [ exec-time = %d]\n""", func_name, time.time() - old
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

