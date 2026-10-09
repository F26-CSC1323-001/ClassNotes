

from random import randint

print("Transformations:")

nums = []

for i in range(0, 11):
	nums.append(randint(0, 99))

print(f"\tProblem 1: ")
print(f"\t\t{nums}")

# problem 1: triple the numbers in the list nums using list comprehension. -> Transformation

triples = [n*3 for n in nums]

print(f"\t\t{triples}\n")

# problem 2: Given a set of miles, convert each to kilometers (multiply by 1.609) and round to
# the nearest decimal.

print(f"\tProblem 2 (miles): ")
miles = []
for i in range(0, 6):
	miles.append(randint(1, 15))
print(f"\t\t{miles}")

kilometers = [round(n*1.609, 1) for n in miles]
print(f"\t\t{kilometers}\n")

# problem 3: Given a set of words, build a list of the word lengths
print(f"\tProblem 3 (words): ")
words = ["sun", "moon", "star", "planet", "comet"]
print(f"\t\t{words}")

word_lengths = [len(word) for word in words]
print(f"\t\t{word_lengths}\n\n")


print(f"Filters:") # the if (condition) comes after the list

# Problem 4: Given some numbers, keep only those divisble by 4 (using nums)
print(f"\tProblem 4 (number filter):")
print(f"\t\t{nums}")

div_four = [n for n in nums if n % 4 == 0]
print(f"\t\t{div_four}\n")

# Problem 5: Given a list of names, keep only those that start with a capital letter
names = ["Alice", "bob", "Cara", "dan"]
print(f"\tProblem 5 (capitals): ")
print(f"\t\t{names}")

upper_names = [n for n in names if n[0].isupper()]
print(f"\t\t{upper_names}\n")

# Problem 6: Given a list of numbers, square only the odd ones.
print(f"\tProblem 6 (square odds): ")
print(f"\t\t{nums}")

# square_odd = [n ** 2 if n % 2 != 0 else n for n in nums]
square_odd = [n ** 2 for n in nums if n % 2 != 0]
print(f"\t\t{square_odd}\n")


print("Conditionals, strings, and range: ")
# Problem 7: given a list of numbers that includes negatives, replace negative numbers with 0.
print(f"\tProblem 7 (no negatives): ")
negs = []
for i in range(0, 11):
	negs.append(randint(-50, 50))
print(f"\t\t{negs}")
no_negs = [n if n >= 0 else 0 for n in negs]
print(f"\t\t{no_negs}\n")

# Problem 8: Given a list of numbers, label each "big" if its > 50  or "small" if <= 50
print(f"\tProblem 8 (big/small): ")
print(f"\t\t{nums}")
big_small = ["big" if x > 50 else "small" for x in nums]
print(f"\t\t{big_small}\n")


# Problem 9: Given a list of strings, collect the last letter of each word.
print(f"\tProblem 9 (lastletter): ")
print(f"\t\t{names}")
last_letter = [x[-1] for x in names]
print(f"\t\t{last_letter}\n")

# Problem 10: Given a list of strings, strip any space characters from them. 
print(f"\tProblem 10 (nospaces): ")
letters = [" a ", " b", "c ", "Hello World", "    5"]
print(f"\t\t{letters}")
no_spaces = [letter.strip() for letter in letters]
print(f"\t\t{no_spaces}")

# Problem 11: Given a string of any type or contents, collect only the numbers into a list 
print(f"\tProblem 11 (get numbers):")
random_string = "aksdf 23bgas03nas3f0ad91jn"
print(f"\t\tString: {random_string}")
numbers_from_string = [int(n) for n in random_string if n.isdigit()]
print(f"\t\t{numbers_from_string}\t\t\t")







squared_numbers = [ x ** 2 for x in [randint(0,50) for i in range(10)] if x % 2 == 0]

print(f"Embeded comprehensions: {squared_numbers}")
