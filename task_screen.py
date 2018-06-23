'''Task Screen'''
import os
import re

class Task_Screen:

	def __init__(self, display_message, input_prompt, answers):
		'''
			Initializes a Task_Screen object by setting
			a display message, an input prompt, and a regex
			pattern to compare answers against.
		'''
		self.display_message = display_message
		self.input_prompt = input_prompt
		self.answers = answers
		
	def clear_screen(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		
	def display(self):
		'''
			Displays the message of the object.
		'''
		self.clear_screen()
		print(self.display_message)
		

	def input(self):
		'''
			Continues to prompt user for input until
			the input matches the regex pattern.
		'''
		while True:
			ans = input(self.input_prompt)
			if not re.match(self.answers, ans):
				print('Please enter a valid entry.')
				continue
			else:
				return ans
				