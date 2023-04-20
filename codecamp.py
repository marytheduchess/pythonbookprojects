#MADLIBS PROJECT FROM 12 BEG. PYTHON PROJECTS VIDEO
#string concatenation
#aka how to put strings together 
#lets say the string says subscribe to....
#youtuber = some string variable
# ~ youtuber = "marytheduchess"
# ~ print("subscribe to " + youtuber)		#all different ways of doing this
# ~ print("subscribe to {}".format(youtuber))
# ~ print("subscribe to {youtuber}")
# ~ #works
#use the last one (f string) cleanest way

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because\
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
	
print(madlib)

