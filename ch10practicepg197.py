# ~ filename = 'learning_python.txt'

# ~ with open(filename) as file_object:
	# ~ lines = file_object.readlines()
	
# ~ learning_python = ''
# ~ for line in lines:
	# ~ learning_python += line.rstrip()

# ~ message = input("Which sentence are you trying to replace?")

# ~ if message in learning_python:
	# ~ print(message.replace('in', 'using'))
	# ~ print(message.replace('you can', 'you are able'))
# ~ else:
	# ~ print("There is no sentence to replace.")
	

#pg. 199 PRACTICE
#10-3 "Guest"

filename = 'guest.txt'
message = input("What is your name?")

with open(filename, 'a') as file_object:
	file_object.write("Hello, " + message.title() + "!")
	

#10-4 "Guest Book"
#Write a while loop that prompts users for their name. When they enter their name, print a greeting to the screen.
# ~ f = open("guest_boook.txt")
# ~ f1 = f.readlines()

# ~ def get_formatted_name(first_name, last_name):
	# ~ """Return a full name, neatly formatted."""
	# ~ full_name = first_name + ' ' + last_name
	# ~ return full_name.title()
	# ~ f = open("guest_book.txt", "r+")
	
# ~ while True:
	# ~ print("\nPlease tell me your name:")
	# ~ print("(enter 'q' at any time to quit)")
	
	# ~ f_name = input("First name: ")
	# ~ if f_name == 'q':
		# ~ break
		
	# ~ l_name = input("Last name: ")
	# ~ if f_name == 'q':
		# ~ break
	
	# ~ formatted_name = get_formatted_name(f_name, l_name)
	# ~ print("\nThank you, " + formatted_name + ".")
	
# ~ for get_formatted_name in f1:
	# ~ print(get_formatted_name, file=open('guest_boook.txt', 'a'))
	
# ~ #Add a line recording their visit in a file called guest_book.txt. 
# ~ #Make sure each entry appears on a new line in the file.

filename = "guest_boook.txt"

prompt = input("What is your name?")

with open(filename) as file_object:
	lines = file_object.readlines()




