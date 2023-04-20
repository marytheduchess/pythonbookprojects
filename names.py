from name_function import get_formatted_name

print("Enter 'q' to quit at any time.")
while True:
	first = input("\nPlease give me a first name: ")
	if first == 'q':
		break
	last = input("Please give me a last name: ")
	if last == 'q':
		break
	middle = input("\nIf there is a middle name, please enter it: ")
	if middle == 'q':
		break
	
	formatted_name = get_formatted_name(first, last, middle)
	print("\tNeatly formatted name: " + formatted_name + ".")
	
