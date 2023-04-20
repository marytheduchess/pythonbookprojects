#Saving and Reading User-Generated Data
#saving data wih json is useful when you're working with user-generated data, because if you don't store your user's information
#somehow, you'll lost it when the program stops running

# ~ import json
# ~ # load the username, if it has been store previously
# ~ # otherwise, prompt for the username and store it
# ~ username = input("What is your name? ")

# ~ filename = 'username.json'
# ~ with open(filename, 'w') as f_obj:
	# ~ json.dump(username, f_obj)
	# ~ print("We'll remember you when you come back, " + username + "!")



# ~ import json

# ~ # load the username, if it has been store previously
# ~ # otherwise, prompt for the username and store it
# ~ def greet_user():		#Refactoring pg. 212
	
	# ~ filename = 'username.json'

	# ~ try:
		# ~ with open(filename) as f_obj:
			# ~ username = json.load(f_obj)
	# ~ except FileNotFoundError:
		# ~ username = input("What is your name? ")
		# ~ with open(filename, 'w') as f_obj:
			# ~ json.dump(username, f_obj)
			# ~ print("We'll remember you when you come back, " + username + "!")
	# ~ else:
		# ~ print("Welcome back, " + username + "!")

# ~ greet_user()

## sometimes your code will work but you'll recognize that you need to improve your code by breaking it up into a series of functions
#that have specific jobs. This process is called "Refactoring"
## Refactoring makes your code cleaner, easier to understand and easier to extend.

import json 

def get_stored_username():
	"""Get stored username if available."""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username
		
def get_new_username():
	"""Prompt for new username."""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username
	
def greet_user():
	"""Greet the user by name."""
	username = get_stored_username()
	if username:
		print("Welcome back, " + username + "!")
	else:
		# ~ username = input("What is your name? ")
		# ~ filename = 'username.json'
		# ~ with open(filename, 'w') as f_obj:
			# ~ json.dump(username, f_obj)
		username = get_new_username()
		print("We'll remember you when you come back, " + username + "!")
greet_user()

