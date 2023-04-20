import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""Tests for the class anonymous survey."""
	
	def setUp(self):
		"""
		Create a survey and a set of responses for use in all test methods.
		"""
		question = "What language did you first learn to speak?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['English', 'Spanish', 'Mandarin']
		
	def test_store_single_response(self):
		"""Test that a single response is stored properly."""
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)
			
		# ~ self.assertIn('English', my_survey.responses)
	def test_store_three_responses(self):
		"""Test that three individual responses are stored properly."""
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)
			
		# ~ question = "What language did you first learn to speak?"
		# ~ my_survey = AnonymousSurvey(question)
		# ~ responses = ['English', 'Spanish', 'Mandarin']
		# ~ for response in responses:
			# ~ my_survey.store_response(response)
		
		# ~ for response in responses:
			# ~ self.assertIn(response, my_survey.responses)
				
unittest.main()
