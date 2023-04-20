#pg. 200 Chapter 10 "Exceptions"
#python uses special objects called 'exceptions' to manage errors that arise during a program's execution
#whenever an error occurs that makes python unsure what to do next, it creates an exception object
#if you write code that handles the exception, the program will continue running. If you don't handle the exception,
#the program will halt and show a 'traceback', which includes a report of the exception that was raised.
#exceptions are handled with 'try-except' blocks. a 'try-except' block asks Python to do something, but it also tells Python 
#what to do if an exception is raised. When you use try-except blocks, your programs will continue running even if things start to go wrong.
#Instead of tracebacks, which can be confusing for users to read, users will see friendly error messages that you write.

# ~ print(5/0)
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	if second_number =='q':
		break
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0!")
	else:
		print(answer)
	

