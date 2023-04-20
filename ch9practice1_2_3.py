#pg. 166 PRACTICE 9-1 "Restaurant"
#make a class called 'restaurant.' the __init__() method for restaurant should store two attributes: a rest._name and a cuisine_type
#make a method called desc_rest. that prints these two pieces of info, and a method called open_restaurant that prints a message indicating that the rest. is open
#make an instance called rest. from your class, print the two attr. individually, and then call both methods


# ~ class Restaurant():
	# ~ """An attempt at building a restaurant."""
	
	# ~ def __init__(self, name, cuisine):
		# ~ """Initialize name and cuisine."""
		# ~ self.name = 'Kaluaa'
		# ~ self.cuisine = 'Thai'
	
	# ~ def describe_restaurant(self):
		# ~ """Describe the name and cuisine of the restaurant."""
		# ~ print("The name of the restaurant is " + self.name.title())
		# ~ print("The cuisine type of the restaurant is " + self.cuisine())		

	# ~ def open_restaurant(self):
		# ~ """Print a message stating that the restaurant is open."""
		# ~ print(self.name.title() + " is open.")


class Cat():
	"""A simple attempt to model a cat."""
	
	def __init__(self, name, age):
		"""Initialize name and age."""
		self.name = name
		self.age = age
	
	def eat(self):
		"""Simulate a cat eating in response to a command."""
		print(self.name.title() + " is now eating.")
		
	def sleeping(self):
		"""Simulate a cat sleeping."""
		print(self.name.title() + " is now sleeping!")
		
my_cat = Cat('lea', 5)
my_cat.eat()
my_cat.sleeping()

print("My cat's name is " + my_cat.name.title() + "!")
print("My cat is " + str(my_cat.age) + " years old!")



