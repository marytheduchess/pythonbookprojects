##PRACTICE pg. 166
# "Admin"

#make a class called User
class User():
	def __init__(self, first_name, last_name, user_name, email):
		self.first_name = first_name
		self.last_name = last_name
		self.user_name = user_name
		self.email = email
		
#create 2 attributes called first name and last name
	def describe_user(self):
		"""Return a neatly formatted description of the user."""
		print(f"\n{self.first_name} {self.last_name}")
		print(f" Username: {self.user_name}")
		print(f" Email: {self.email}")
		
		
#then create several other attributes that are typically stored in a user profile
#make a method called describe user that prints a summary of the users info
	def greet_user(self):
		print("\nWelcome back, {self.user_name}!")
		
		
#make another method called greet user that prints a pers. greeting
user1 = User('mary', 'onyongo', 'marytheduchess', 'mo1232@email.com')
user1.describe_user()
user1.greet_user()








