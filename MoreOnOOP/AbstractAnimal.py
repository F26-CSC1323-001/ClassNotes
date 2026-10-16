import abc #abstract base class

class Animal(metaclass = abc.ABCMeta):
	def __init__(self):
		""" Constructs a new animal """

	@abc.abstractmethod # abstract method decorator
	def communicate(self):
		""" How an animal Communicates """

class Bird(Animal):
	def __init__(self):
		""" Constructs a new bird """
	def communicate(self):
		""" How a Bird communicates """
		print("Tweet Tweet")

b = Bird()
b.communicate()

a = Animal()
