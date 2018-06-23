'''Database Work Log'''
import csv
import os
import re
import sys

from task_screen import Task_Screen


def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')
	
def screen_prompt(display, input, regex):
	'''
		Displays a screen message and compares input
		against a regex pattern.
	'''
	task = Task_Screen(display, input, regex)
	task.display()
	return task.input()
	
def main():
	'''
		Displays the main menu and prompts
		user for a choice to either add a task, 
		search for a task, or to exit the program.
	'''
	clear_screen()
	inpt = screen_prompt(
				'WORK LOG\nWhat would you like to do?\na) Add a new entry\nb) Search in existing entries\n' +
				'c) Enter new employee\nd) Quit program', 
				'>', 
				'[AaBbCcDd]'
				)
				
	if inpt.lower()=='a':
			clear_screen()
			#Retrieve the employee id
			id = screen_prompt('Employee ID: ', '', '\d*')
			
			clear_screen()
			#display the date task screen and retrieve the date.
			date = screen_prompt('Date of the task\nPlease use MM/DD/YYYY: ', '', '([0-1][0-9])\/([0-3][0-9])\/[0-9]{4}')
			
			clear_screen()
			#Retrieve the title of the task
			name = screen_prompt('Name of the task: ', '>', '.*[\w\s].*')
			
			clear_screen()
			#Retrieve the time spent completing the task
			time = screen_prompt('Time Spent (rounded by minute): ', '>', '\d+')
			
			clear_screen()
			#Prompt for notes
			notes = screen_prompt('Notes (optional, allowed to leave blank): ', '>', '.*[\w\s].*')
			
			#TODO: Enter task to task database

if __name__ == '__main__':
	main()
