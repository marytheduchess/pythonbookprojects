#pg. 154 "Storing your Functions in Modules"
#one advantage of functions is the way they separate blocks of code from your main program
#by using descriptive names for you r functions, your main program will be much easier to follow
#you can go a step further by storing your functions in a separate file called a 'module' and then 'importing' that module into your main program
#an 'import statement' tells python to make the code in a module available in the currently running prog. file
#there are several ways to import a module:
##pg. 154 "Importing an entire module"
#to start importing functions, we first need to create a module. a module is a file ending in .py that contains the code you want to import into your
#program. lets make a module that contains the function make_pizza(). to make this module, we'll remove everything from the file pizza.py except 
#the function make_pizza():
# ~ def make_pizza(size, *toppings):
	# ~ """Summarize the pzza we are about to make."""
	# ~ print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
	# ~ for topping in toppings:
		# ~ print("- " + topping)

#now, we'll make a separate file called making_pizzas.py in the same directory as pizza.py. this file imports the module we just created and then makes 
#two calls to make_pizza()
# ~ import pizza

# ~ pizza.make_pizza(16, 'pepperoni')
# ~ pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
###(making_pizzas.py)###
#pg. 155 the first approach to importing, in which you simply write import followed by the name of the module, makes every function from the module available in
#your program. if you use this kind of import stamtement to imort an entire module named module_name.py each funtion in the module is
##available through the following syntax: module_name.function.name()

##pg. 156 "Importing Specific Functions"
#You can also import a specific function from a module. Here's the gen. syntax for this approach:
# from module_name import function_name
#you can import as many functions as you want from a module by separating each function's name with a comma:
#from module_name import function_0, function_1, function_2
#The making_pizzas.py example would look like this if we want to import just the function we're going to use:

#from pizza import make_pizza

#make_pizza(16, 'pepperoni')
#make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#with this syntax, you don't need to use the dot notation when you call a function, bc we've explicitly imported the function make_pizza() in the import
#statement, we can call it by name when we use the function

#pg. 156 "Using as to Give a Function an Alias"
#if the name of a funct. you're importing might conflict with an existing name in your program or if the function name is long,
#you can use the short, unique alias-- an alternate name simllar to a nickname for the function. you'll give the function this special
#nickname when you import the function. here we give the function make_pizza() an alias, mp(), by importing make_pizza as mp. the as
#keyword renames a function using the alias you provide:

#from pizza import make_pizza as mp

#mp(16, 'pepperoni')
#mp(12, 'mushrooms', 'green peppers', 'extra cheese')

#the import statement shown here renames the function make_pizza() to mp() in this program. any time we want to call make_pizza() we can simply write mp() instead,
#and python will run the code in make_pizza() while avoiding any confusion with another make_pizza() function you might have written in this program file.
#the gen. syntax for providing an alias is:
#from module_name import function_namew as fn

#pg. 157 "Using as to Give a Module an Alias"
#you can also provide an alias for a module name. Giving a module a short alias, like p for pizza, allows you to call the module's functions more quickly
#calling p.make_pizza() is more concise than calling pizza.make_pizza():

#import pizza as p
#p.make_pizza(16, 'pepperoni')
#p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#the module pizza is given the alias p in the import statement, but all of the module's functions retain their original names. calling the functions by writing
#p.make_pizza() is not only more concise than writing pizza.make_pizza(), but also redirects your attention from the module name and allows you to focus on 
#the descriptive names of its functions. these function anmes, which clearly tell you what each function does, are more important
#to the readabilitiy of your code than using the full module name.
#import module_name as mn

#pg. 157 "Importing all Functions in a Module"
#you can tell python to import every function in a module by using the asterisk (*) operator

#from pizza import *

#make_pizza(16, 'pepperoni')
#make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#the asterisk in the import staement tells python to copy every function from the module pizza into this program file. 
#because every function is imported, you can call each function by name w/out using the dot notataion/ however it's best not to use this approach
#when you're working with larger modules that you didn't write: if the module has a function name that matches an existing name in your project
#you can get some unexpected results. 

#pg. 158 "Styling Functions"
#you neeed to keep a few details in mind when you're styling functions.
#functions should have descriptive names, and these names should use lowercase letters and underscores.
#descriptive names help you and others understand what your code is trying to do. Module names should use these conventions as well.
#every function should have a comment that explains concisely what the function does. this comment should appear immediately after the 
#function does. this comment should appear immediately after the function definition and use the docstring format.
#if you specify a default value for a parameter, no spaces should be used on either side of the equal sign:
#def function_name(parameter_0, parameter_1='default value')

#the same convention should be used for keyword arg. in function calls::
#function_name(value_0, parameter_1='value')

#PEP 8 rec. that you limit lines of code 79 characters so every line is visible in a reasonably sized editor window
#if a set of parameters causes a function's definition to be longer than 79 characters, press enter after opening the ( ) on the definition line. on the next
#line, press TAB twice to separate the list of arg. from the body of the function, which will only be indented one level

#most editionrs automatically line up any additional lines of parameters to match the indentation you have est. on the first line:
## def function_name(
		#parameter_0, parameter_1, parameter_2,
		#parameter_3, parameter_4, parameter_5):
	#function body...
	
#if your program or module has more than one function, you can separate each by two blank lines to make it easeier to see where one function ends
#and the next one begins
#all import statements should be written at the beginning of a file.
#the only exception is if you use comments at the beginning of your file to describe the overall program

