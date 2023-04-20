##pg. 178 PRACTICE 
##**note pg.172 if the class you're writing is a specialized version of another class you wrote, you can use inheritance.
#when one class inherits from another, it automatically takes on all the attributes and methods of the first class.
#the original class is called the parent class and the new class is the child class.
#the child class inherits every attribute and method from its parent class, but is also free to define new attributes and methods of its own.**
##**the first task python has when creating an instance from a child class is --to assign values to all attributes in the parent class.--**
##**when inheriting we use the super(). function and the __init__ method
###9-6 "Ice Cream Stand"
#Write class called IceCreamStand that inherits from the Restaurant class
#add an attribute called flavors that stores a list of ice cream flavors 
#write a method that displays these flavors. then create an instance of IceCreamStand and call this method

		
# ~ class Restaurant():
	# ~ def __init__(self, name, cuisine):
		# ~ """Initialize name and cuisine type attributes."""
		# ~ self.name = name
		# ~ self.cuisine = cuisine
		# ~ self.number_served = 0
		
	# ~ def describe_restaurant(self):
		# ~ """Return a neatly formatted descriptive name."""
		# ~ print("My restaurant's name is " + my_restaurant.name.title() + ", we serve " + my_restaurant.cuisine.title() + " food.")
		
	# ~ def open_restaurant(self):
		# ~ print("The restaurant is open.")
		
	# ~ def customers(self):
		# ~ """Print the number of customers the restaurant has served."""
		# ~ print("This restaurant has served " + str(self.number_served) + " customers.")
	
	# ~ def set_number_served(self, set_number):
		# ~ """Set the number of customers served to a given value."""
		# ~ self.number_served = set_number
		
	# ~ def increment_number_served(self, number):
		# ~ """Add the given amount to the number of customers served."""
		# ~ self.number_served += number


# ~ class IceCreamStand(Restaurant):
	# ~ """Represent aspects of a car, specific to electric vehicles."""
	# ~ def __init__(self, name, cuisine):
		# ~ """
		# ~ Initialize attributes of the parent class.
		# ~ Then initialize attributes specific to an electric car.
		# ~ """
		# ~ super().__init__(name, cuisine)
		# ~ self.flavors = ['vanilla', 'strawberry', 'chocolate']
		
	# ~ def describe_flavors(self, flavors):
		# ~ """Print a statement describing the ice cream flavor."""
		# ~ print("This restaurant has " + str(self.flavors) + ".")
		
		
# ~ my_restaurant = Restaurant('Kalua', 'Thai')
# ~ my_restaurant.describe_restaurant()

# ~ my_restaurant.open_restaurant()

# ~ my_restaurant.customers()
# ~ my_restaurant.set_number_served(25)
# ~ my_restaurant.customers()
# ~ my_restaurant.increment_number_served(15)
# ~ my_restaurant.customers()

# ~ my_icecream = IceCreamStand('Kalua', 'Thai')
# ~ my_icecream.describe_flavors('strawberry')






###PRACTICE 9-7 "Admin"
##write a class called 'Admin' that inherits from the 'User' class from practice 9-3
##add an ATTRIBUTE called 'privileges' that stores a LIST of STRINGS like "can add post", "can ban user", and so on.
##write a METHOD called show_privileges() that lists the admin's set of privileges.
##create an INSTANCE of 'Admin' and call your METHOD
class User():
	def __init__(self, name, age, login):
		"""Initialize username and age attributes."""
		self.username = name
		self.age = age
		self.login_attempts = 0
		
	def describe_user(self):
		"""Print a summary of the user's information."""
		print(my_user.username.title() + " is the username.")
	
	def reset_login_attempts(self, login):
		"""
		Set the login attempts to a the value of zero.
		Reject the login if it attempts to sign in.
		"""
		if login >= self.login_attempts:
			self.login_attempts = login
		else:
			print("You have reached the maximum number of login attempts.")	
	
	def increment_login_attempts(self, logins):
		"""Add the given value to the number of login attempts."""
		self.login_attempts += logins
				





