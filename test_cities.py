import unittest
from city_functions import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Tests for 'city_functions.py'."""
	def test_city_country_name(self):
		"""Do cities and countries like Santiago, Chile, work?"""
		city_country = get_formatted_name('Santiago', 'Chile')
		self.assertEqual(city_country, 'Santiago, Chile')

unittest.main()

