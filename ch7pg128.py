#to keep track of many users, we'll need to use lists and dictionaries with our while loops
#a for loop is effective for looping through a list, but you shouldn't modify a list inside a for loop.
#to modify a list as you work through it use a while loop.

#cofirmed_users.py
#start w users that need to be verified 
# and an empty list to hold confirmed users
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

#verif each user until there are no more unconfirmed users.
# move each verified users into the list of confirmed users.
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	
	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)
	#display all confirmed users.
	print("\nThe following users have been confirmed:")
	for confirmed_user in confirmed_users:
		print(confirmed_user.title())
				

#pg.129 pets.py 
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')
	
print(pets)

