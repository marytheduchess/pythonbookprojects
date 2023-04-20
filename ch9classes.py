###pg. 162 chapter 9 "Classes" 
#object-oriented programming is one of the most effective approaches to writing software.
#in object-oriented programming you write 'classes' that represent real-world things and situations 
#you create 'objects' based on these classes. when you write a class, you define the general behavior that a whole category of objects can have
#when you create individual objects from the class, each object is automatically equipped with the general behavior; you can then give each object
#whatever unique traits you desire. you'll be amazed how well real-world situations can be modeled with object-oriented programming
#making an object from a class is called 'instantiation', and you work with 'instances' of those classes.


##understanding object-oriented programming will help you see the world as a programmer does. it'll help you really know your code, not just
##what's happening line by line, but also the bigger concepts behind it. Knowing the logic behind classes will train you to think logically so you
##can write programs that effectively address almost any problem you encounter

#classes also make life easier for you and the other programmers you'll need to work with as you take on increasingly complex challenges.
#when you and other programmers write code based on teh same kind of logic, you'll be able to understand each other's work. your programs will make sense
#to many collaborators, allowing everyone to accomplish more.

#"Creating and Using a Class"
#you can model almost anything using classes. let's start by writing a simple class, 'dog', that represents a dog-not one dog in particular,
#but any dog. What do we know about most pet dogs? well they all have a name and age. we also know that most dogs sit and roll over. those two
#pieces of information (name and age) and those two behaviors (sit and roll over) will go in our 'dog' class because they're common to most dogs. 
#this class will tell python how to make an object representing a dog. after our class is written, we'll use it to make individual instances, each of which
#represents one specific dog

##"Creating the Dog Class" pg. 162
#each instance created from teh dog class will store a name and an age and we'll give each dog the ability to sit() and roll_over()

##DOG.PY###
# ~ class Dog():			#1
	# ~ """A simple attempt to model a dog."""			#2
	# ~ def __init__(self, name, age):
		# ~ """Initialize naem and attributes."""			#3
		# ~ self.name = name							#4
		# ~ self.age = age
		
	# ~ def sit(self):							#5
		# ~ """Simulate a dog sitting in response to a command."""
		# ~ print(self.name.title() + " is now sitting.")
		
	# ~ def roll_over(self):
		# ~ """Simulate rolling over in response to a command."""
		# ~ print(self.name.title() + " rolled over!")
	
	
##1 : here we define a class called 'dog' by conv. capitalized names refer to classes in python, the parentheses in the class def. are empty because we're creating
#this class from scratch
##2 : at 2 we write a docstring describing what this class does.
##3 : the __init__() method is a special method python runs automatically whenever we create a new instance based on the dog class
### this method has two leading underscores and two trailing underscores, a convention that helps prevent python's default method names from conflicting with 
###your method names.
##4 : any variable frefixed with self is available to every method in the class, and we'll also be able to access these variables through any instance created 
##from the class, self.name = name takes the value stored in the parameter name and stores it in the variable name, which is then attached to the instance
##being created. the same process happens with self.age = age. variables that are accessible through instances like this are called 'attributes'
##5 : bc these methods don't need additional information like a name or age, we just define them to have one parameter,, self. the instances we create later will have
# access to these method. in other words, they'll be able to sit and roll over.



##pg. 163 "The __init__() Method"
#a function that's part of a class is a 'method.' everything you learned about functions applies to methods as well; the only practical difference for now
#is the way we'll call methods. the __init__() method at #3 (read)...is a special method python runs automatically whenever we create a new instance
#base on the dog class. this method has two leading underscores and two trailing underscores, a convention that helps prevent python's def. method
#names from conflicting with your method names.

#we define the __init__() method to have three parameters: self, name and age. the self parameter is required in the method defition, and it must come
#first before other parameters. it must be incl. int he def. because wehn python calls this __init__() method laster (to create an instance of dog
#the method call will auto matically pass the self argument. Every method call associated with a class automiatically passes self,
#which is a reference to the instance itself; it gives the individual instance access to the attributes and methods in the class. When we make an instance 
#of Dog, Python will call the __init__() method from the dog class. we'll pass dog() a name an an age as arguments; self is passed automatically so we don't
#need to pass it. Whenever we want to make an instance from the dog class, we'll need to provide values for only the last two parameters, name and age.

##pg. 164 "Creating Classes in Python 2.7/3"
#when you create a class in python 2.7 you need to make one  minor change. you incl. the term 'object' in parentheses when you create a class:

# ~ class ClassName(object):
	# ~ --snip-- 
#this makes python 2.7 classes behave more like python 3 classes, which makes your work easier overall
#the dog class would be defined like this in python 2.7:
# ~ class Dog(object):
	# ~ --snip--

##"making an instance from a class"
#think of a class as a set of instructions for how to make an instance. the class dog is a set of instructions that tells python how to make 
#individual instances representing specific dogs.

#####	PG. 167 "wORKING WTIH cLASSES AND iNSTANCES"
#Once you write a class, you'll spend most of your time working with instances created from that class. One of the first tasks you'll want to do 
#is modify the attributes associated w/ a particular instances. You can modify the attributes of an instance directly or write methods that
#update attributes in specific ways
#"The Car Class" pg. 167
#our class will store information about the kind of car we're working with and it will have a method that summarizes this info

##cars.py
#"Setting a Default Value for an Attribute" pg. 168
#Every attribute in a class needs an initial value, even if that value is 0 or an empty string. In some cases such as when setting a default value
##it makes sense to specify this initial value in the body of the init() method, if you do this for an attribute, you don't have to include a parameter
#for that ttribute.
#let's add an attribute called odometer_reading that always starts with a value of - 
##--back to cars.py
#this time when python calls the __init__() method to create a new instance, it stores the make, model, and year values as attributes like it did in the
#previous example. 

##not all cars are sold with exactly 0 miles so we need a way to change the value of this attribute
#pg. 168 "Modifying Attribute Values"
#you can change an attribute's value in 3 ways: you can change the value directly through an instance, set the value through a method, or
#increment the value (adda certain amount to it) through a methdo.
#pg. 169 "Modifiying an Attribute's Value Directly"
#the simplest way to modify a value of an attribute is to access the attribute directly through an instance

###Modifying an Attribute's Value Through a Method pg. 169
#it can be helpful to have methods that update certain attributes for you. Instead of accessing the attribute directly, you pass the new
#value to a method that handles the updating internatlly. Heres an ex. showing a method update_odometer():
# ~ class Car():
	# ~ """A simple attempt to represent a car."""
	
	# ~ def __init__(self, make, model, year):
		# ~ """Initialize attributes to describe a car."""
		# ~ self.make = make 
		# ~ self.model = model
		# ~ self.year = year
		# ~ self.odometer_reading = 0									#odometer reading in dot notation
	
	# ~ def get_descriptive_name(self):
		# ~ """Return a neatly formatted descriptive name."""
		# ~ long_name = str(self.year) + ' ' + self.make + ' ' + self.model		#written this way to show '2016 Audi A4'
		# ~ return long_name.title()
		
	# ~ def read_odometer(self):
		# ~ """Print a statement showing the car's mileage."""
		# ~ print("This car has " + str(self.odometer_reading) + " miles on it.")
	
	# ~ def update_odometer(self, mileage):							#new method called update_odometer
		# ~ """Set the odometer reading to the given value."""
		# ~ self.odometer_reading = mileage
		
		
# ~ my_new_car = Car('audi', 'a4', 2016)
# ~ print(my_new_car.get_descriptive_name())

# ~ my_new_car.update_odometer(23)							#part of new method
# ~ my_new_car.read_odometer()

####pg.170 we can extend the method update_odometer() to do additional work every time the odometer reading is modified:

# ~ class Car():
	# ~ """A simple attempt to represent a car."""
	
	# ~ def __init__(self, make, model, year):
		# ~ """Initialize attributes to describe a car."""
		# ~ self.make = make 
		# ~ self.model = model
		# ~ self.year = year
		# ~ self.odometer_reading = 0									#odometer reading in dot notation
	
	# ~ def get_descriptive_name(self):
		# ~ """Return a neatly formatted descriptive name."""
		# ~ long_name = str(self.year) + ' ' + self.make + ' ' + self.model		#written this way to show '2016 Audi A4'
		# ~ return long_name.title()
		
	# ~ def read_odometer(self):
		# ~ """Print a statement showing the car's mileage."""
		# ~ print("This car has " + str(self.odometer_reading) + " miles on it.")
	
	# ~ def update_odometer(self, mileage):							#new method called update_odometer == then updated again to this
		# ~ """
		# ~ Set the odometer reading to the given value.
		# ~ Reject the change if it attempts to roll the odometer back.
		# ~ """
		
		# ~ if mileage >= self.odometer_reading:
			# ~ self.odometer_reading = mileage
		
		# ~ else:
			# ~ print("You can't roll back an odometer.")
			
		
# ~ my_new_car = Car('audi', 'a4', 2016)
# ~ print(my_new_car.get_descriptive_name())

# ~ my_new_car.update_odometer(23)							#part of new method
# ~ my_new_car.read_odometer()

###pg. 170 "INCREMENTING AN ATTRIBUTE'S VALUE THROUGH A METHOD."
#sometimes you'll want to increment an attributes value by a certain amount, rather than set an entirely new value.
#say we buy a used car and put 100 miles on it between the time we buy it and the time we register it.
#here's a method that allows us to pass this incremental amount and add that value to the odometer reading: 
###cars.py



