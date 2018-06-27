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
		
	def test_clear_screen(self):
		num = 0
		test = Task_Screen('display', 'input', '[A-Za-z]')
		self.assertEqual(test.clear_screen(), num)
		
	def test_clear_screen2(self):
		num = 0
		self.assertEqual(db_worklog.clear_screen(), num)
		
	def test_screen_prompt(self):
		#test = Task_Screen('TEST', 'TEST', '[A-Za-z]')
		t = 'test'
		self.assertEqual(db_worklog.screen_prompt('TEST', 'TEST', '[A-Za-z]'), t)
		
if __name__ == '__main__':
	unittest.main()

