## 10-11 "Favorite Number"
# pg. 214

#write a program that prompts for the user's favorite number
#use json.dump() 
#write a seperate program that reads in this value and prints the message "I know your favorite number! It's ..."

import json
def ask_fav_number():
	"""Get stored number if available."""
	filename = 'favorite_number.json'
	try:
		with open(filename, 'w') as f_obj:
			favorite = json.load(favorite, f_obj)
	except FileNotFoundError:
		return None
	else:
		return favorite
def get_number():
	"""Get the favorite number by prompting user."""
	favorite = input("What is your favorite number?")
	filename = 'favorite_number.json'
	with open(filename, 'w') as f_obj:
		json.dump(favorite, f_obj)
		print("We'll remember your favorite number when you come back, number " + favorite + "!")
		
	
def show_favorite_number():
	"""Prompt for the user's favorite number."""
	favorite = ask_fav_number()
	if favorite:
		favorite = get_number()
		print("What is your favorite number? ")
	else:
		favorite = ask_fav_number()
		print("We'll remember your favorite number when you come back, number " + favorite + "!")
		
get_number()


