prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
	city = input(prompt)
	
	if city == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() + "!")
#pg. 125		
#we can stop the WHILE loop in this program by calling BREAK as soon as the user enters the 'QUIT' value =>
#tthe break statement directs the flow of your program; you can use it to control which lines of code are executed and which aren't
#so the program ONLY executes code that you want it to, when you want it to.

#pg. 126 counting.py (more)
#rather than breaking out of a loop entirely without executing the rest of its code =>
#you can use the continue statement to return to the beginning of the loop 
#based on the result of a conditional test. (+= means IS/goes up by)
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	print(current_number)
	
x = 1
while x <= 5:
	print(x)
	x += 1 #if you actually omit this line, the loop will run forever

x = 1
while x <= 5:
	print(x)
	#doing this makes '1' go on FOREVER

