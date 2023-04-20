#pg. 139 "Equivalent Function Calls" 
#because poistional arguments, keyword arguments and default values can all be used together, often you'll have several equivalent ways to call a 
#function.

# ~ def describe_pet(pet_name, animal_type='dog'):
# ~ #with this def, an arg. always needs to be provided for pet_name, and this value can be provided using the positional, or keyword format
# ~ #all of the following calls could work for this function:
# ~ describe_pet('willie')
# ~ describe_pet(pet_name='willie')

# ~ describe_pet('harry', 'hamster')
# ~ describe_pet(pet_name='harry', animal_type='hamster')
# ~ describe_pet(animal_type='hamster', pet_name='harry')

#pg. 141 PRACTICE 8-3 "Shirt"

# ~ def make_shirt(shirt_size, shirt_text):
	# ~ """Display information about shirt."""
	# ~ print("\nThe size of the shirt is " + shirt_size + ".")
	# ~ print("\nThe text on the shirt says " + shirt_text + ".")
	
# ~ make_shirt(shirt_size='Large', shirt_text='Taco Tuesday!')
# ~ make_shirt('Large', 'Taco Tuesday!')


#pg. 141 PRACTICE 8-4 
# ~ def make_shirt(shirt_size='Large', shirt_text='i love python'):
	# ~ """Display information about shirt."""
	# ~ print("\nThe size of the shirt is " + shirt_size.title() + ".")
	# ~ print("\nThe text on the shirt is " + shirt_text + ".")
# ~ make_shirt('Large', 'I love Python')
# ~ make_shirt('medium', 'Taco Tuesday')



#pg. 141 PRACTICE 8-5 "Cities"
#write a function called describe city

# ~ def describe_city(city_name, country_name='USA'):
	# ~ """Display information about a city."""
	# ~ print("\nThe city " + city_name.title() + " is in the " + country_name.title() + ".")
	
# ~ describe_city(city_name='Minneapolis')
# ~ describe_city(city_name='New York')
# ~ describe_city(city_name='San Francisco')



def make_pants(pant_color, pant_size='5'):
	"""Display information about pants."""
	print("\nThe color of the pants are " + pant_color.title() + ".")
	print("\nThe size of the " + pant_color.title() + " pants are " + pant_size.title() + ".")
	
make_pants(pant_color='black')
make_pants(pant_color='blue')
make_pants(pant_color='acid wash')


#pg. 141 Return Values
#a function doesn't always have to display its output directly
#the value a function returns is called a 'return value'

#pg. 142 Returning a Simple Value
# ~ def get_formatted_name(first_name, last_name): #use this "get_formatted_name" to display a full name after storing first and last name seperately 
	# ~ """Return a full nam, neatly formatted."""
	# ~ full_name = first_name + ' ' + last_name
	# ~ return full_name.title()
	
# ~ musician = get_formatted_name('jimi', 'hendrix')
# ~ print(musician)

#pg. 142 Making an Argument Optional
#sometimes it makes sense to make an argument optional so that people using the function can choose to provide extra info 
#you can use default values to make an argument optional


# ~ def get_formatted_name(first_name, middle_name, last_name):
	# ~ """Return a full name, neatly formatted."""
	# ~ full_name = first_name + ' ' + middle_name + ' ' + last_name
	# ~ return full_name.title()
	
# ~ musician = get_formatted_name('john', 'lee', 'hooker')
# ~ print(musician)


#pg. 143 because middle names aren't always needed we can make it optional
#to do this we give the middle_name argument an empty default value and ignore it unless the user provides a value

# ~ def get_formatted_name(first_name, last_name, middle_name=''):
	# ~ """Return a full name, neatly formatted."""
	# ~ if middle_name:
		# ~ full_name = first_name + ' ' + middle_name + ' ' + last_name
	# ~ else:
		# ~ full_name = first_name + ' ' + last_name
	# ~ return full_name.title()

# ~ musician = get_formatted_name('john', 'hooker', 'lee')
# ~ print(musician)
# ~ musican = get_formatted_name('jimi', 'hendrix')
# ~ print(musician)


#pg. 144 "Returning a Dictionary"
#a function can return any kind of value you need it to, including more complicated data structures
#for example: lists and dictionaries.
#the following function takes in parts of a name and returns a dictionary represienting a person

# ~ def build_person(first_name, last_name): #functional dictionary basically
	# ~ """Return a dictionary of information about a person."""
	# ~ person = {'first': first_name, 'last': last_name} #key, value pairs, dictionary is called person
	# ~ return person
	
# ~ musician = build_person('jimi', 'hendrix')
# ~ print(musician)

#this function takes in simple textual info and puts it into a more meaningful data structure
#this function can accept optional values like a middle name, an age, an occupation or any other info you want to store about a person

# ~ def build_person(first_name, last_name, age=''): 	#add a new optional parameter 'age' to function definition and assign an empty default value
	# ~ """Return a dictionary of information about a person."""
	# ~ person = {'first': first_name, 'last': last_name}
	# ~ if age:
		# ~ person['age'] = age
	# ~ return person
	
# ~ musician = build_person('jimi', 'hendrix', age='27')
# ~ print(musician)

#pg. 145 "Using a Function with a While Loop 
#you can use funcctions with all the python structures we've learned about so far
#for example, let's use the get_formatted_name() function with a while loop to greet users more formally

# ~ def get_formatted_name(first_name, last_name):
	# ~ """Return a full name, neatly formatted."""
	# ~ full_name = first_name + ' ' + last_name
	# ~ return full_name.title() 
# ~ # This is an infinite loop
# ~ while True:
	# ~ print("\nPlease tell me your name:")
	# ~ f_name = input("First name: ")
	# ~ l_name = input("Last name: ")
	
	# ~ formatted_name = get_formatted_name(f_name, l_name)
	# ~ print("\nHello, " + formatted_name + "!")
	
#^^^for this we used a simple version of get_formatted_name() that doesn't involve middle names, the while loops asks the 
#user to enter their name

#pg. 145 but theres one problem with this while loop: we haven't defined a quit condition
#we want the user to be able to quite as easily as possible, so each prompt should offer a way to quit.
#the break statement offers a straight forward way to exit the loop at either prompt:

def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = first_name + ' ' + last_name
	return full_name.title()
	
while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")
	
	f_name = input("First name: ")
	if f_name == 'q':
		break
		
	l_name = input("Last name: ")
	if l_name == 'q':
		break
	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")


