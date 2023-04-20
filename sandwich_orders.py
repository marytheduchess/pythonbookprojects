sandwich_orders = ['BLT', 'Pastrami', 'Grilled Cheese', 'Pastrami', 'Turkey Club', 'Pastrami']
finished_sandwiches = []
while 'Pastrami' in sandwich_orders:
	sandwich_orders.remove('Pastrami')
	print(sandwich_orders)
while sandwich_orders:
	current_order = sandwich_orders.pop()

	
	print("Verifying order: " + current_order.title())
	finished_sandwiches.append(current_order)
		
	print("\nThe following orders are not completed: ")
	for sandwich_order in sandwich_orders:
		print(sandwich_order.title())
