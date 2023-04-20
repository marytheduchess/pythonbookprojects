##"Importing Class" pg. 179, Chapter 9
#in keeping with the overall phil. ofe python, you'll want to keep your files as uncluttered as possible
#to help, python lets you store classes in modules and then import the classes you need into your main program
##"Importing a Single Class"
# let's create a module containing just the Car class. we alr. have a file named car.py in this ch. but this module should be name car.py because
#it contains code representing a car. we'll resolve this naming issue by storing the car class in a module named car.py
#from now on, any program that uses this module will need a more specific filename, such as my_car.py
#car.py:

# ~ """A class that can be used to represent a car."""					#we include a module-level docstring that briefly describes the contents of this module.

# ~ class Car():
	# ~ """A simple attempt to represent a car."""
	
	# ~ def __init__(self, make, model, year):
		# ~ """Initialize attributes to describe a car."""
		# ~ self.make = make
		# ~ self.model = model
		# ~ self.year = year
		# ~ self.odometer_reading = 0
		
	# ~ def get_descriptive_name(self):
		# ~ """Return a neatly formatted descriptive name."""
		# ~ long_name = str(self.year) + ' ' + self.make + ' ' + self.model + ' ' 
		# ~ return long_name.title()
		
	# ~ def read_odometer(self):
		# ~ """Print a statement showing the car's mileage."""
		# ~ print("This car has " + str(self.odometer_reading) + " miles on it.")
	
	# ~ def update_odometer(self, mileage):
		# ~ """
		# ~ Set the odometer reading to the given value.
		# ~ Reject the change if it attempts to roll the odometer back.
		# ~ """
		# ~ if mileage >= self.odometer_reading:
			# ~ self.odometer_reading = mileage
		# ~ else:
			# ~ print("You can't roll back an odometer.")
		
	# ~ def increment_odometer(self, miles):
		# ~ """Add the given amount to the odometer reading."""
		# ~ self.odometer_reading += miles

##"Storing Multiple Classes in a Module"
#you can store as many classes as you need in a single module, although each class in a module should be related somehow. the classes Battery
#and ElectricCar both help represent cars, so let's add them to the module car.py
#go to car.py
