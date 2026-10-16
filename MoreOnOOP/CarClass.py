

# Goal: Make a Car class. Track number of tires, If it has an engine, and the owner's name
# When printed (i.e. print(car1)), we should see: Car; owner={}, tires={}, engine={}

class Vehicle:
	def __init__(self, name):
		self.tires = None
		self.engine = None
		self.name = name
	def __str__(self):
		return f"owner={self.name}, tires={self.tires}, engine={self.engine}"

class Cycle(Vehicle):
	def __init__(self, name):
		super().__init__(name)
		self.tires = 2

#	def __str__(self):
#		return super().__str__() # Method lookup: A subclass will look to its superclass for a function, if the superclass
					 # Doesn't have that function, it looks in the next higher superclass.

# Polymorphism: When you have multiple functions with the same name in different classes.
class Car(Vehicle):
	def __init__(self, name):
		super().__init__(name)
		self.engine = True
		self.tires = 4
	def __str__(self):
		return f"Car; {super().__str__()}"
class Bicycle(Cycle):
	def __init__(self, name):
		super().__init__(name)
		self.engine = False
	def __str__(self):
		return f"Bicycle; {super().__str__()}"

class Motorcycle(Cycle):
	def __init__(self, name):
		super().__init__(name)
		self.engine = True
	def __str__(self):
		return f"Motorcycle; {super().__str__()}"




car1 = Car("Oliver")
print(car1)

bike1 = Bicycle("Hazel")
print(bike1)

moto1 = Motorcycle("Alec")
print(moto1)
