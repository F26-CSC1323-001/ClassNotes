
class Animal:
	def __init__(self):
		""" Constructs a new animal """

	def communicate(self):
		"""How an animal communicates"""
		raise NotImplementedError("Abstract method communicate not implemented in \
subclass!")

class Bird(Animal):
	def __init__(self):
		""" Constructs a new bird """
	def communicate(self):
		""" How a bird communicates """
		print("Tweet tweet")

b = Bird() 
b.communicate()
