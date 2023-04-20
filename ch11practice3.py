class Employee():
	"""Store a first name, last name and an annual salary."""
	def __init__(self, f_name, l_name, salary):
		self.first_name = f_name.title
		self.last_name = l_name.title
		self.salary = salary
		
	def give_raise(self):
		"""Give the employee a raise."""
		self.salary += amount
		
