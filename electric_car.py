##pg.172 "the __init__ method for a child class"
##pg.183
"""A set of classes that can be used to represent electric cars."""
from car import Car

class Car():
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
		
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")
		
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
			
	def increment_odometer(self, miles):
		self.odometer_reading += miles
		
class Battery():
	"""A simple attempt to model a battery for an electric car."""
	
	def __init__(self, battery_size=70):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size
	
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
	
	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 70:
			range = 240
		elif self.batter_size == 85:
			range = 270
		
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)
			
class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an electric car.
		"""
		super().__init__(make, model, year)			#helps python make connections between the parent and child class
		self.battery = Battery()
		
		
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
	
	##how to override a method:
	def fill_gas_tank(self):
		"""Electric cars don't have gas tanks."""
		print("This car doesn't need a gas tank!")
	#now if someone tries to call fill_gas_tank, it won't work/will print message
		
my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()				
#this line (line 63) tells Python to look at the 'instance' my_tesla, find its battery attribute and-
#call the method describe_battery() that's associated with the Battery instance stored in the attribute.
my_tesla.battery.get_range()







