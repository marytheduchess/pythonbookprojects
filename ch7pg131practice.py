#pg. 131 PRACTICE 7-8 "Deli"
#make a list called sandwich orders, fill it with the names of various sandwiches

# ~ sandwich_orders = ['BLT', 'Pastrami', 'Grilled Cheese', 'Pastrami', 'Turkey Club', 'Pastrami']
# ~ finished_sandwiches = []
# ~ while 'Pastrami' in sandwich_orders:
	# ~ sandwich_orders.remove('Pastrami')
	# ~ print(sandwich_orders)
# ~ while sandwich_orders:
	# ~ current_order = sandwich_orders.pop()

	
	# ~ print("Verifying order: " + current_order.title())
	# ~ finished_sandwiches.append(current_order)
		
	# ~ print("\nThe following orders are not completed: ")
	# ~ for sandwich_order in sandwich_orders:
		# ~ print(sandwich_order.title())

#pg. 131 PRACTICE 7-9 "No Pastrami
#make sure 'pastrami' appears in the sandwich_orders list over 3 times
#add code near beginning to print message saying deli has run out of pastrami
#then use while loop to remove all occurrences of pastrami from sandwich orders
#pg. 131 PRACTICE 7-10 "Dream Vacation"
responses = {}

polling_active = True

while polling_active:
	name = input("\nWhat is your name? ")
	response = input("What is your dream vacation? ")
	
	responses[name] = response
	
	repeat = input("Would you like to let another person respond? (yes/ no) ")
	if repeat == 'no':
		polling_active = False
		
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(name + " would like to go to " + response + "!")
	
