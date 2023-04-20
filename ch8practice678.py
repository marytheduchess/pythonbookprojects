#pg. 146 PRACTICE 8-6, 8-7, 8-8

#PRACTICE 8-6 "City Names"
#write a function called city_country() takes in the name of a city and its country 
def city_country(city_name, country_name):
	"""Return the city and country, neatly formatted."""
	city_country = city_name + ', ' + country_name
	return city_country.title()
	
location = city_country('Santiago', 'Chile')
print(location)
location = city_country('Paris', 'France')
print(location)
location = city_country('Luxembourg', 'Belgium')
print(location)


#PRACTICE 8-7 "Album"
#write a function called make_album, that takes in an artist name and album title and returns a dictionary containing these infos

def make_albums(artist_name, album_title):
	"""Return the artist name and album title, neatly formatted."""
	make_albums = artist_name + ' ' + '"' + album_title + '"'
	return make_albums.title()

discography = make_albums('Beyonce', 'Renaissance')
print(discography)
discography = make_albums('Greenday', 'Dookie')
print(discography)
discography = make_albums('Iron Maiden', 'Powerslave')
print(discography)


#Practice 8-8 "User Albums"
def make_albums(artist_name, album_title, tracks=''):
	"""Return a dictionary of information about an artist's music, neatly formatted."""
	make_albums = {'artist': artist_name, 'album': album_title}
	if tracks:
		make_albums['tracks'] = tracks
	return make_albums

discography = make_albums('Beyonce', 'Renaissance', tracks='16')
print(discography)
discography = make_albums('Greenday', 'Dookie', tracks='15')
print(discography)
discography = make_albums('Iron Maiden', 'Powerslave', tracks='8')
print(discography)


def make_albums(artist_name, album_title, tracks=''):
	"""Return a dictionary of information about an artists albums."""
	make_albums = artist_name + ' ' + album_title + ' '
	return make_albums.title()
	
while True:
	print("\nArtist name: ")
	print("\nAlbum name: ")
	print("(enter 'q' at any time to exit)")
	
	a_name = input("Artist name: ")
	if a_name == 'q':
		break
	
	a_title = input("Album name: ")
	if a_title == 'q':
		break
		
	formatted_artist = make_albums('Beyonce', 'Renaissance')

	print(formatted_artist)


	
	

	
