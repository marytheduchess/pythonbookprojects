##PRACTICE 11-1 "City, Country"
from city_functions import get_formatted_name

while True:
	city = input("\nPlease enter a city name: ")
	if city == 'q':
		break
	country = input("\nPlease enter a country name: ")
	if country == 'q':
		break
	
	city_country = get_formatted_name(city, country)
	print("\tNeatly formatted city, country name: " + city_country + ".")
