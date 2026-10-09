

dictionary1 = {x:x**3 for x in range(1, 6)}

print(f"Cubes: {dictionary1}\n")


# Challenge 1: modify the above comprehension so the values are stored as strings instead of integers

print(f"Challenges: ")
print(f"\t1: ")
stringcubes = {x:str(x**3) for x in range(1, 6)}
print(f"\tStringCubes: {stringcubes}\n")



letters = ['a', 'b', 'c', 'z']
letterorder = {c: ord(c)-96 for c in letters}
print(letterorder)
