

# List Comprehension allows programmers to create complex lists in one line, as long as a pattern can be defined.

# General Structure:
# list_name = [action for something in iterable]


print("Squares: ")
# for loop equiv.
nums = list(range(1, 6))

squares = []
for n in nums:
	squares.append(n ** 2)

print(squares)

# comprehension
squares2 = [n ** 2 for n in range(1, 6)]
print(squares2)


# evens for loop
print(f"\nEvens: ")
evens = []
for i in nums:
	if i % 2 == 0:
		evens.append(i)
print(evens)

# evens list comp
evens2 = [n for n in range(1,6) if n % 2 == 0]
print(evens2)

print(f"\nUppercase: ")
#for loop:
words = ["cat", "python", "dog", "list", "a"]

newwords = []
for word in words:
	if len(word) > 3:
		newwords.append(word.upper())
	else:
		newwords.append(word)
print(newwords)

# list comp:
newwords2 = [word.upper() if len(word) > 3 else word for word in words]
print(newwords2)
