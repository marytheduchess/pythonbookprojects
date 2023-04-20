import json
#reads the list back into memory, rather than into a seperate file like json.dump()

filename = 'numbers.json'

with open(filename) as f_obj:
	numbers = json.load(f_obj)

print(numbers)

