#pg. 197 "Writing to a File"
#one of the simplest ways to save data is to write it to a file. When you write text to a file, the output will still be available
#after you close the terminal containing your program's output.
#to write text to a file, you need to call open() with a second argument telling Python that you want to write to the file

# ~ filename = 'programming.txt'

# ~ with open(filename, 'w') as file_object:			#w tells python to write 
	# ~ file_object.write("I love programming.\n")
	# ~ file_object.write("I love creating new games. \n")			#put the /n for the new line


#you can open a file in read mode('r'), write mode('w'), or append mode('a'). or a mode that allows you to read and write to the file('r+') 
#if you omit the mode argument, python opens the file in read-only mode by default
#the open() function automatically creates the file you're writing to if it doesn't already exist

##if you want to add content to a file instead of writing over existing content, you can open the file in 'append mode'
#any lines you write to the file will be added at the end of the file

filename = 'programming.txt'

with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets. \n")
	file_object.write("I love creating apps that can run in a browser. \n")
	file_object.write("I love creating new games. \n")
	
