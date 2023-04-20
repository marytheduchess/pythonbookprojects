#Storing Data pg. 208

#when users close a program, you'll almost always want to save the info they entered. A simple way to do this involves
#storing your data using the 'json' module
#the json module allows you to dump simple python data structures into a file and load the data from that file the next
#time the program runs. You can also use json to share data between diff python programs

# USING json.dump() and json.load() pg. 209
#write a short program that stores a set of numbers and another program that reads these numbers back into memory
#first program will use json.dump() to store the set of numbers 
import json 

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
	json.dump(numbers, f_obj)
	
