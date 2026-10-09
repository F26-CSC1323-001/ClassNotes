
# A dictionary is a set of key-value pairs. A key is an unchangeable value used to reference elements. Values are said
# elements that are associated with keys

# Some langauges call this an associative array

offices = {"Morgan": 247, "Kiremire": 219, "Bob": 112, "Kennedy": 108}

print(f"offices: {offices}\n")

# Dictionary operations:

# adding an Item:
offices["Coriell"] = 232
print(f"Add: {offices}\n")

# retrieving a value from a dictionary
morgan_office = offices["Morgan"]

# modify existing pairs:
offices["Kiremire"] = 220

# to remove:
del offices["Bob"]

print(f"Modded Offices: {offices}\n")

# to iterate through keys and obtain all values:
for k in offices.keys(): # .keys() returns a list of all keys in the dictionary
	print(offices[k])
print()

# print all key-value pairs in a key -> value format, one per line
for k in offices.keys():
	print(f"{k} -> {offices[k]}")

for k, v in offices.items():	# .items() returns a list of tuples (v1, v2) -> (key, value) -> 
				# [(key1, val1), (key2, val2), (key3, val3)]
 	print(f"{k} -> {v}")
