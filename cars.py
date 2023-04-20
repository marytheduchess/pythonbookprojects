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
			
# ~ my_new_car = Car('audi', 'a4', 2016)
# ~ print(my_new_car.get_descriptive_name())
# ~ my_new_car.odometer_reading = 23						#accessed the attribute directly through an instance
# ~ my_new_car.read_odometer()


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
		
	# ~ ##incrementing an attributes value through a method pg. 170:
	# ~ def increment_odometer(self, miles):
		# ~ """Add the given amount to the odometer reading."""
		# ~ self.odometer_reading += miles
		
# ~ my_used_car = Car('subaru', 'outback', '2013')
# ~ print(my_used_car.get_descriptive_name())

# ~ my_used_car.update_odometer(23500)
# ~ my_used_car.read_odometer()

# ~ my_used_car.increment_odometer(100)
# ~ my_used_car.read_odometer()

	
	
	
# ~ my_new_car = Car('audi', 'a4', 2016)
# ~ print(my_new_car.get_descriptive_name())

# ~ my_new_car.update_odometer(23)							#part of new method
# ~ my_new_car.read_odometer()

