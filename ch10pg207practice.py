##Chapter 10, pg. 207-8 PRACTICE
##10-6 "Addition" and 10-7 "Addition Calculator"

# ~ print("Give me two numbers and I'll add them.")
# ~ print("Enter 'q' to quit.")

# ~ while True:
	# ~ try:
		# ~ first_number = input("\nFirst number: ")
		# ~ if first_number == 'q':
			# ~ break
		# ~ second_number = input("Second number: ")
		# ~ if second_number == 'q':
			# ~ break
		# ~ addition = int(first_number)+ int(second_number)
		
	# ~ except ValueError:
		# ~ print("Please try again.")
		# ~ print("Give me two numbers and I'll add them.")

	# ~ else:
		# ~ print(addition)

##Practice 10-8 "Cats and Dogs
# ~ #make 2 files called cats.tx t and dogs.tx t
# ~ class Pets():
	# ~ def cat_names(filename):
		# ~ try:
			# ~ with open(filename, 'w') as file_object:			#store at least 3 names
				# ~ file_object.write('oscar')
				# ~ file_object.write('\ntommy')
				# ~ file_object.write('\nlea')

		# ~ except FileNotFoundError:
			# ~ msg = "Sorry, the file " + filename + " does not exist."
			# ~ print(msg)
	
		# ~ else:
			# ~ print(filename)
	
	# ~ def dog_names(filename):
		# ~ try:
			# ~ with open(filename, 'w') as file_object:			#store at least 3 names
				# ~ file_object.write('hank')
				# ~ file_object.write('\ncheese')
				# ~ file_object.write('\nkobe')
		# ~ except FileNotFoundError:
			# ~ msg = "Sorry, the file " + filename + " does not exist."
			# ~ print(msg)
		
		# ~ else:
			# ~ print(filename)

# ~ #write a program that tries to read these files and print the contents of the file
# ~ #wrap your code in a try except block to catch the FileNotFound error, and print a friendly message if 
# ~ #a file is missing 
# ~ #move one of the files to a different location on your system 
# ~ #and make sure the code in the except block executes properly

##skipped 10-9 "Silent Cats and Dogs"

###PRACTICE CHAPTER 10
###10-10 "Common Words"

def counting_wrds(filename):

	try:
		with open(filename, 'r', encoding='utf-8') as file_object:
			contents = file_object.read()
			
	except FileNotFoundError:
		print("Sorry, the file " + filename + " does not exist.")
	
	else:
		#count words
		words = contents.count('the')
		
		print("The file " + filename + " says the word " + words.lower.count('the') + " times.")
		
filename = 'villetept1.txt'
contents.count("the")
filename = 'villetept2.txt'
contents.count("the")







	
