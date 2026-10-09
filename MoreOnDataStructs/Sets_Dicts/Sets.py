from random import randint

nums = []
for i in range(100):
	nums.append(randint(1,50))

print(f"Nums: {nums}\n")
# Typecasting a list into a set gets rid of any repeating values
print(f"set(Nums): {set(nums)}\n")

# creating a set
set1 = {1, 5, 4, 18, 32, 3, 3, 3} # the last two 3s will be removed by default
print(f"set1: {set1}\n")

# sets of strings

word = "ambrosia is neat"
print(f"Word: {word}\n")
print(f"SetWord: {set(word)}\n")
print(f"StringSetWord: {str(set(word))}\n")
