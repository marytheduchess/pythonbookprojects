###pg. 171 PRACTICE 9-4 
#"Number Served"

#start with program from 9-1
#add an attribute called number_served with a default value of 0
#create an instance called restaurant from this class
#print the number of customers the restaurant has served, and then change this value and print it again
#add a method called set_number_served() that lets you set the number of customers that have been served
#call this method with a new number and print the value again
#add a method called increment_number_served() that lets you increment the number of customers who've been served
#call this method


#re-do 9-1 first then ^^
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


# ~ my_restaurant = Restaurant('Kalua', 'Thai')
# ~ my_restaurant.describe_restaurant()

# ~ my_restaurant.open_restaurant()

# ~ my_restaurant.customers()
# ~ my_restaurant.set_number_served(25)
# ~ my_restaurant.customers()
# ~ my_restaurant.increment_number_served(15)
# ~ my_restaurant.customers()


# ~ my_restaurant.set_number_served()
# ~ my_restaurant.customers()

##Practice pg. 171 9-5 "Login Attempts"

# ~ class User():
	# ~ def __init__(self, name, age, login):
		# ~ """Initialize username and age attributes."""
		# ~ self.username = name
		# ~ self.age = age
		# ~ self.login_attempts = 0
		
	# ~ def describe_user(self):
		# ~ """Print a summary of the user's information."""
		# ~ print(my_user.username.title() + " is the username.")
	
	# ~ def reset_login_attempts(self, login):
		# ~ """
		# ~ Set the login attempts to a the value of zero.
		# ~ Reject the login if it attempts to sign in.
		# ~ """
		# ~ if login >= self.login_attempts:
			# ~ self.login_attempts = login
		# ~ else:
			# ~ print("You have reached the maximum number of login attempts.")	
	
	# ~ def increment_login_attempts(self, logins):
		# ~ """Add the given value to the number of login attempts."""
		# ~ self.login_attempts += logins
		
			
# ~ my_user = User('marytheduchess', 25, 5)
# ~ print("The username is " + my_user.username.title() + ".")
# ~ print("The user is " + str(my_user.age) + " years old.")









