 ## Pg. 222 "Testing a Class"
 ##pg. 223 "A Class to Test"
 
class AnonymousSurvey():
	 """Collect anonymous answers to a survey question."""
	 def __init__(self, question):
		 self.question = question
		 self.response = response
		 
		 
	 def store_questions(self):
		 """Show the survey question."""
		 print(self.question)
	 
	 def store_responses(self, new_response):
		 """Store a single response to the survey."""
		 self.responses.append(new_response)
		
	 def show_results(self):
		 """Show all the responses that have been given."""
		 print("Survey results:")
		 for response in self.responses:
			 print('- ' + response)
			
anonymous = AnonymousSurvey()
anonymous.response()
