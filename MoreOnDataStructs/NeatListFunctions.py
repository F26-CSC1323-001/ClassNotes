

# Filter, Map, and Reduce

# Map -> take in a list, perform some action to every item in the list, and return a new list

# Filter -> take in a list, "Keep only the items that pass some test", also returns a new list

# Reduce -> use some calculation, to boil everything down to one value, returns one value

# analogy: on a conveyer belt: Map is like a guy that stamps every item, filter removes anything that's defective,
# and reduce packs everything into boxes.


# map: map(function, iterable) -> iterables: list, strings, dictionaries, sets, ...

nums = [1, 2, 3, 4]

squared = list(map(lambda x: x * x, nums))

print(squared)

# as a for loop:

squared = []
for i in nums:
	squared.append(i * i)



# filter: filter(function, iterable) -> returns iterable like map, typecast into list.


nums = [1, 2, 3, 4, 5, 6]

def is_even(x):
	if x % 2 == 0:
		return True

evens = list(filter(is_even, nums))
print(evens)

# as lambda: evens = list(filter(lambda x: x % 2 == 0, nums))

# as a for loop:
'''
evens = []
for i in nums:
	if i % 2 == 0:
		evens.append(i)
'''


# reduce: This function is not built in, it must be imported:
from functools import reduce

# usage: reduce(function, iterable, initial)

def calc_total(acc, x):
	acc += x
	return acc

nums = [1, 2, 3, 4]
total = reduce(calc_total, nums, 0)
print(total)

# total = reduce(lambda acc, x: acc+x, nums, 0)


# all together now!
nums = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x%2==0, nums))
squares = list(map(lambda x: x * x, evens))
total = reduce(lambda a, b: a+b, squares, 0)
print(nums)
print(evens)
print(squares)
print(total)
