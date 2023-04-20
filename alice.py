# ~ filename = 'alice.txt'
# ~ with open('path', 'w', encoding='utf-8') as f:
	# ~ open(filename)
		
# ~ try:
	# ~ with open(filename) as f_obj:
		# ~ contents = f_obj.read()
    
# ~ except FileNotFoundError:
	# ~ msg = "Sorry, the file " + filename + " does not exist."
	# ~ print(msg)
# ~ else:
	# ~ # Count the approximate number of words in the file.
	# ~ words = contents.split()
	# ~ num_words = len(words)
	# ~ print("The file " + filename + " has about " + str(num_words) + " words.")



def count_words(filename):
	"""Count the approximate number of words in a file."""
		
	try:
		with open(filename, 'r', encoding='utf-8') as f_obj:
			contents = f_obj.read()
			print(contents)
		
	except FileNotFoundError:
		msg = "Sorry, the file " + filename + " does not exist."
		print(msg)
		# pass (erase above)
		
	else:
		# Count approximate number of words in the file.
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)
	
