
#pg. 133 Chapter 8: Functions
#functions are named blocks of code that are designed to do one specific job
#when you want to perform a particular task that you've defined in a function 
#call the name of function responsible for it
#"Defining a Function"
#greeter.py

def greet_user():			#function definition
	"""Display a simple greeting."""			#body of function "display a...." is the docstring
	print("Hello!")				

greet_user()

#slight mod "Passing Info to a function
def greet_user(username): 				#the variable 'username' is called a parameter, a piece of info the function needs to do its job
	"""Display a simple greeting."""
	print("Hello, " + username.title() + "!")

greet_user('jesse')		#'jesse' is an example of an 'argument'

#pg. 135 PRACTICE 8-1 "Message"
def display_message(prompt):
	"""Display a simple message"""
	prompt = "Hi, today we've finished chapter 7, and are now working on chapter 8, where we are learning about functions."
	print(prompt.title())
display_message('prompt')


#pg. 135, "Passing Arguments" 
#because a function definition can have multiple parameters, a func. call may need multiple arguments
#you can positional arguments, which need to be the same order the parameters were written: keyword arguments
#keyword arguments where each argument consists of a variable name and a value; and lists and dictionaries 


#pg. 136, "Positional Arguments"
# When you call a function, python must match each argument in the function call with a parameter in the function definition
#the easiest way to do this is based on the order of the arguments provided
#values matched up this way are called "positional arguments" 

#pets.py pg 136
def describe_pet(animal_type, pet_name): #literally, describe pet. needs animal type and its name
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ",")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')  #modified code by adding this on

#pg. 137 "Keyword Arguments"
#a keyword argument is a name-value pair that you pass to a function
#directly associate the name and the value within the argument
#pg. 138 keyword arguments free you from having to worry about correctly ordering your arguments in the function call
#equivalents:
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')


#pg. 138 "Default Values"
# when writing a function, you can define a "default value" for each parameter.
#if an argument for a parameter is provided in the function call, Python uses the argument value.
#If not, it uses the parameter's default value.
#so when you define a default value for a parameter, you can exclude the corresponding argument youd usually write in the function call.

def describe_pet(pet_name, animal_type='dog'):
	"""Display information about a pet. """
	print("\nI have a " + animal_type + ".")
	print("\nMy " + animal_type +"'s name is " + pet_name.title() + ".")
	
describe_pet(pet_name='willie')
#^^if you notice that most of the calls to describe_pet() are being used to describe dogs, you can set the default value of 
#animal_type to 'dog.' NOW anyone calling describe_pet() for a dog can omit that info (that's why we put 'dog' in animal_type).
# pg. 139 the reason why "pet_name" has to be first in the parameters is because the default value makes it unnecessary to specify a type of animal as
#an argument, the only argument left in the function call is the pet's name.
#python still interprets this as a positional argument, so if the function is called with just a pet's name, that argument will match up with the
#first parameter listed in the fucntion's definition.
#pg. 139 NOTE: when you use default values, any parameter with a default value needs to be listed after all the parameters that don't have default values
#This allows Python to continue interpreting positional arguments correctly


