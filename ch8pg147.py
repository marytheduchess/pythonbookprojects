#pg. 147 "Passing a List"
#its useful to pass a list to a function whether its a list of names, numbers, or more complex objects
#such as dictionaries
#when you pass a list to a function, the function gets direct access to the content of the list
def greet_users(names):
	"""Print a simple greeting to each user in the list."""
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#pg. 147 "Modifying a List in a Function"
#When you pass a list to a a function, the function can modify the list. any changes made to thte list inside the functions
#body are permanent, allowing you to work efficiently even when you're dealing with large amounts of data.

#printing_models.py practice

#Start with some designs that need to be printed.

# ~ unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# ~ completed_models = [] 

#Simulate printing with design, until none are left.
#Move each design to completed_models after printing.
# ~ while unprinted_designs:
	# ~ current_design = unprinted_designs.pop()		#simulate creating a 3d print from the design
	# ~ print("Printing model: " + current_design)
	# ~ completed_models.append(current_design)

# ~ #display all completed models.
# ~ print("\nThe following models have been printed:")
# ~ for completed_model in completed_models:
	# ~ print(completed_model)

#As long as designs remain in unprinted_designs, the while loop simulates printing each design by removing
#a design from the end of the list, storing it in current_design

# pg. 148 We can reorganize this code by writing two functions, each of which does one specific job.
#first function will handle printing the designs and the second will summarize the prints

# ~ def print_models(unprinted_designs, completed_models):
	# ~ """

	# ~ Simulate printing each design, until none are left. 
	# ~ Move each design to completed_modes after printing.
	# ~ """
	
	# ~ while unprinted_designs:
		# ~ current_design = unprinted_designs.pop()
		
		# ~ #Simulate creating 3D print from the design.
		# ~ print("Printing model: " + current_design)
		# ~ completed_models.append(current_design)
		
# ~ def show_completed_models(completed_models):
	# ~ """Show all the models that wer printed."""
	# ~ print("\nThe following models have been printed:")
	# ~ for completed_model in completed_models:
		# ~ print(completed_model)

# ~ unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# ~ completed_models = []
# ~ print_models(unprinted_designs, completed_models)
# ~ show_completed_models(completed_models)

#pg. 149 Given the two lists (compl. and uncompl.), the function simulates printing each design by emptying the list of unprinted designs and
#filling up the lists of completed models. This program has the same output as the previous one but it's much neater and more organized
#The code that does most of the work has been moved to two separate functions, which makes the main part of the program easier to understand. 

#We set up a list of unprint. des. and an empty list that will hold the compl. models. Then, because we've already defined our 
#two functions, all we have to do is call them and pass them the right arguments. We called print_models and passed it to 
#the right lists it needs
#This program is easier to extend and maintain than the version without function. If we need to print more dssigns later, we can just
#call print_models again. If you're writing a function and notice the function is doing too many diff. tasks, try to split the code into two functions.

#pg. 149 "Preventing a Function from Modifying a List"
#sometimes you'll want to prevent a function from modifying a list. For example, say that you start with a list of unprinted designs and write a 
#function to move them to a list of completed models, like in the previous example.
##you may decide that even though you've printed all the designs, you want to keep the original list of unprinted_design for your records. that
##because you moved all the design names out of unprinted designs, the list is now empty and the empty list is the only version you have
##the original is gone!

##in this case, you can address this issue by passing the function a copy of the list, not the original. any changes the function makes to the list
##will affect only the copy, leaving the original list intact
##you can send a copy of a list to a function like this:
###  function_name(list_name[:])
#the slice notation [:] makes a copy of the list to send to the function. if we didn't want to empty the list of unprinted designs in print_models.py
#we could call print models() like this:
### print_models(unprinted_designs[:], completed_models)


#even though you can preserve the contents of a list by passing a copy of it to your functions, you should pass the original list to functions
#unless you have a specific reason to pass a copy.
#it's more efficient for a function to work with an existing list to avoid using the time and memory needed to make a separate copy
#especially when you're working with large lists



#PRACTICE pg. 150  8-9 "Magicians"
#make a list of magician's names, then pass the list to a function called show_magicians(), which prints the name of magician in the list

# ~ def show_orders(orders, completed_orders):
	# ~ """
	
	# ~ Simulate printing each food, until none are left.
	# ~ Move each food to completed_orders after printing.
	# ~ """
	# ~ while orders:
		# ~ current_order = orders.pop()
		
		# ~ #Simulate creating an order from the food.
		# ~ print("Printing order: " + current_order)
		# ~ completed_orders.append(current_order)
		
# ~ def show_completed_orders(completed_orders):
	# ~ """Show all the orders that were printed."""
	# ~ print("\nThe following orders have been completed:")
	# ~ for completed_order in completed_orders:
		# ~ print(completed_orders)

# ~ orders = ['BLT', 'Turkey', 'Grilled Cheeze', 'Reuben']
# ~ completed_orders = []
# ~ show_orders(orders, completed_orders)
# ~ show_completed_orders(completed_orders)


#PRACTICE pg.150 8-10 "Great Orders"
#start with a copy of your program from 8-9, write a function called make_great() that mods the list by adding the phrase "the Great"
#to each magician's name. call show_magicians to see that the list has actually been modified

# ~ def show_orders(orders, completed_orders):
	# ~ """
	
	# ~ Simulate printing each food, until none are left.
	# ~ Move each food to completed_orders after printing.
	# ~ """
	# ~ while orders:
		# ~ current_order = orders.pop()
		
		# ~ #Simulate creating an order from the food.
		# ~ print("Printing order: " + current_order)
		# ~ completed_orders.append(current_order)
		
# ~ def show_completed_orders(completed_orders):
	# ~ """Show all the orders that were printed."""
	# ~ print("\nThe following orders have been completed:")
	# ~ for completed_order in completed_orders:
		# ~ print(completed_orders)

# ~ orders = ['BLT', 'Turkey', 'Grilled Cheeze', 'Reuben']
# ~ completed_orders = []
# ~ show_orders(orders, completed_orders)
# ~ show_completed_orders(completed_orders)

##Passing and Arbitrary Number of Arguments pg. 151
#sometimes you won't know ahead of time how many arguments a function needs to accept
#fortunately, python allows a function to collect an arbitrary number of arguments from the calling statement

##pizza.py pg 151
def make_pizza(*toppings):				#the * tells python to make an empty tuple called toppings and pack whatever val. it receives into this tuple 
	"""Print the list of toppings that have been requested."""
	print(toppings)	#this produces output showing that python can handle a function call with one value and a call with three values

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
#it (print statement with diff. written 'topping'), treats the diff. calls similarily. Note that python packs the args into a tuple even if the 
#function only receives one val.


def make_pizza(*toppings):
	"""Summarize the pizza we are about to make."""
	print("\nMaking a pizza with the fullowing toppings:")
	for topping in toppings:
		print("-" + topping)		#this makes it a bulleted list

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
#this syntax works no matter how many arguments the function receives

#Mixing Positional and Arbitrary Arguments pg. 152
#if you want a funct. to accept several diff. kids of args., the parameter that accepts an arbitrary number of arguments must be placed last in the
#function definition
#python matches positional and keyword argumetns first and THEN collects any remaining arguments in the final parameter

def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make."""
	print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
	
	for topping in toppings:
		print("-" + topping)
		
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#in the function definition, python stores the first value it receives in the parameter 'size', all other val. that come after are 
#store in the tuple 'toppings.' The function calls include an argument for the size first, followed by as many toppings as needed
#now each pizza has a size and a number of toppings and each piece of info is printed in the proper place

#pg. 152 "Using Arbitrary Keyword Arguments"
#sometimes you'll want to accept an arbitrary number of arguments, but you won't know ahead of time what kind of info will be passed to the funct.
#in this case you can write functions that accept as many key-value pairs as the calling statement provides.
#an example involves building user profiles: you'll get info about a user, but you're not sure what kind of info you'll receive
#the function build_profile() in the ex. always takes in a first and last name, but it takes an arbitrary ## of arguments as well

def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	profile = {}
	profile['first name'] = first
	profile['last name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
	
user_profile = build_profile('albert', 'einstein',
							location='princeton',
							field='physics')

print(user_profile)
#the definition of build_profile() expects a first and last name, and then it allows the user to pass in as many name-value pairs as they want
##the double asterisks before the parameter user_info (on line206) cause pyth. to create an empty dictionary (called user_info) and pack
##whatever name-value pairs it receives into this dictionary
##within the function, you can access the name-value pairs just as you would for any dictionary




	
		
		







 

	
	

		
