# ~ def greet_user(username):
	# ~ """Display a simple greeting."""
	# ~ print("Hello, " + username.title() + ".")
	
# ~ greet_user(':)')


# ~ #to call a function, you write the name of the function, then any necessary information in the parentheses

# ~ def greet_user(username):
	# ~ """Display a simple greeting."""
	# ~ print("Hello, " + username.title() + "!")
	
# ~ greet_user('jesse')
# ~ #the variable 'username' in the definition of greet_user() is an ex of a 'parameter'
# ~ #the value 'jesse' in greet_user('jesse') is an example of an 'argument'

# ~ def display_message():
	# ~ print("In this chapter, we are learning about Functions.")

# ~ display_message()

# ~ def favorite_book(book_title):
	# ~ print("My favorite book is " + book_title.title() + "!")
	
# ~ favorite_book('The Sympathizer')

# ~ ##Positional Argument

# ~ def describe_pet(animal_type, pet_name):
	# ~ """Display information about a pet."""
	# ~ print("\nI have a " + animal_type + ".")
	# ~ print("My " + animal_type + "'s name is " + pet_name.title() + ".")
	
# ~ describe_pet('hamster', 'harry')
# ~ describe_pet('dog', 'willie')

# ~ def get_formatted_name(first_name, last_name):
	# ~ """Return a full name, neatly formatted."""
	# ~ full_name = first_name + ' ' + last_name
	# ~ return full_name.title()
	
# ~ musician = get_formatted_name('jimi', 'hendrix')
# ~ print(musician)
# ~ #when you call a function that returns a value, you need to provide a variable where the return value can be stored.

# ~ #to make the middle name optional, we can give the middle_name argument an empty default value and ignore the argument unless
# ~ #the user provides a value. to make get_formatted_name() work w/out a middle name, we set the def. value of middle_name to 
# ~ #an empty string and move it to the end of the list of parameters

# ~ def get_formatted_name(first_name, last_name, middle_name=''):
	# ~ """Return a full name, neatly formatted."""
	# ~ if middle_name:
		# ~ full_name = first_name + ' ' + middle_name + ' ' + last_name 
	# ~ else:
		# ~ full_name = first_name + ' ' + last_name
	# ~ return full_name.title()
	
# ~ musician = get_formatted_name('jimi', 'hendrix')
# ~ print(musician)

# ~ musician = get_formatted_name('john', 'hooker', 'lee') 
# ~ print(musician)

# ~ #returning a dictionary

# ~ def build_person(first_name, last_name):
	# ~ """Return a dictionary of information about a person."""
	# ~ person = {'first': first_name, 'last': last_name}
	# ~ return person
	
# ~ musician = build_person('jimi', 'hendrix')
# ~ print(musician)
# ~ #you can easily extend this function to accept optional values like a middle name, an age, an occupation, or any other information you want to store about a person

# ~ def build_person(first_name, last_name, age=''):
	# ~ """Return a dictionary of information about a person."""
	# ~ person = {'first': first_name, 'last': last_name}
	# ~ if age:
		# ~ person['age'] = age
	# ~ return person
	
# ~ musician = build_person('jimi', 'hendrix', age=27)
# ~ print(musician)


# ~ ##passing a list
# ~ #
# ~ def greet_users(names):
	# ~ """Print a simple greeting to each user in the list."""
	# ~ for name in names:
		# ~ msg = "Hello," + name.title() + "!"
		# ~ print(msg)
		
# ~ usernames = ['hannah', 'ty', 'margot']
# ~ greet_users(usernames)

# ~ #when you pass a list to a function, the fucntion can modify the list.
# ~ #any changes made to the list inside the functions body are permanent

# ~ #Start with some designs that need to be printed

# ~ def print_models(unprinted_designs, completed_models):
	# ~ """
	# ~ Simulate printing each design, until none are left.
	# ~ Move each design to completed_models after printing.
	# ~ """
	
	# ~ while unprinted_designs:
		# ~ current_design = unprinted_designs.pop()
		
		# ~ #Simulate creating a 3D print from the design
		# ~ print("Printing model: " + current_design)
		# ~ completed_models.append(current_design)
		
# ~ #we can re-org. by writing two functions.
# ~ def show_completed_models(completed_models):
	# ~ """Show all the models that were printed."""
	# ~ print("\nThe following models have been printed:")
	# ~ for completed_model in completed_models:
		# ~ print(completed_model)
		
# ~ unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# ~ completed_models = []
# ~ print_models(unprinted_designs, completed_models)
# ~ show_completed_models(completed_models)


class Shark():
	def __init__(self, name):
		self.name = name
	
	def swim(self):
		print(self.name + " is swimming.")
		
	def be_awesome(self):
		print(self.name + " is awesome.")
		
sammy = Shark("Sammy")
sammy.swim()
sammy.be_awesome()


##class and objects by codebasics

class Human:
	def __init__(self, n, o):
		self.name = n
		self.occupation = o
		
	def do_work(self):
		if self.occupation == "tennis player":
			print(self.name, "plays tennis")
		elif self.occupation == "actor":
			print(self.name, "shoots a film")
	
	def speaks(self):
		print(self.name, "says how are you")
		
tom = Human("tom cruise", "actor")
tom.do_work()
tom.speaks()

maria = Human("maria sharapova", "tennis player")
maria.do_work()
maria.speaks()


