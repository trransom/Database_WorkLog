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
				'WORK LOG\nWhat would you like to do?\na) Add a new entry\nb) Search in existing entries\nc) Quit program', 
				'>', 
				'[AaBbCc]'
				)

if __name__ == '__main__':
	main()
