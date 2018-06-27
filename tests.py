'''Tests'''
import unittest

import db_worklog
from task_screen import Task_Screen


class WorklogTests(unittest.TestCase):
	def test_ts_init(self):
		d = 'display'
		i = 'input'
		r = '[A-Za-z]'
		test = Task_Screen('display', 'input', '[A-Za-z]')
		assert d == test.display_message
		assert i == test.input_prompt
		assert r == test.answers
		
	def test_display(self):
		test = Task_Screen('TEST', 'TEST', 'TEST')
		s = 'TEST'
		self.assertEqual(test.display(), s)
		
	def test_input(self):
		test = Task_Screen('display', 'input', '[A-Za-z]')
		t = 'test'
		self.assertEqual(test.input(), t)
		
if __name__ == '__main__':
	unittest.main()

