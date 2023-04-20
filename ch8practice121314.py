#PRACTICE pg. 154 8-12 "Sandwiches"
#write a function that accepts a list of items a person wants on a sandwich, the funct. should have one par. that collects as many items as the func.
#call provides and should print a summary of the sand. tat's being ordered.

def make_food(topping, *sandwich):
	"""Summarize the pizza we are about to make."""
	print("\nMaking a " + str(topping) + 
	" sandwich with the following toppings:")
	for topping in sandwich:
		print("- " + topping)
		
		
make_food('BLT', 'Bacon, Lettuce, Tomatoes')

##PRACTICE pg. 154 8-13 "User Profile"

# ~ def build_profile(first, last, **user_info):
	# ~ """Build a dictionary that includes the user's first and last names."""
	# ~ profile = {}
	# ~ profile['first_name'] = first
	# ~ profile['last_name'] = last
	# ~ for key, value in user_info.items():
		# ~ profile[key] = value
		# ~ return profile
		
# ~ user_profile = build_profile('Mary', 'Onyongo',
							# ~ height='tall', 
							# ~ looks='Gorgeous')
							
# ~ print(user_profile)


##PRACTICE pg. 154 8-14 "Cars"
# ~ def car_profile(make, model, **user_info):
	# ~ """Build a dictionary that includes the vehicle's make, model, and information."""
	# ~ profile = {}
	# ~ profile['make_name'] = make
	# ~ profile['model_name'] = model
	# ~ for key, value in user_info.items():
		# ~ profile[key] = value
		# ~ return profile

# ~ user_profile = build_profile('subaru','outback')
# ~ print(car_profile)
	

						



	
