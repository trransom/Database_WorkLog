'''Database Work Log'''
import csv
import os
import re
import sys
from peewee import *
from datetime import datetime as dt

from task_screen import Task_Screen


db = SqliteDatabase('employees.db')
	
class Task(Model):
	'''
		Initializes the 'Task' relation in the 
		'employees.db' database.
	'''
	task_id = IntegerField(unique=True)
	emp_id = IntegerField()
	date = DateField()
	title = CharField(max_length=255)
	time = IntegerField()
	notes = TextField()
	class Meta:
		database = db


def clear_screen():
	'''
		Clears the console.
	'''
	os.system('cls' if os.name == 'nt' else 'clear')
	return os.system('cls' if os.name == 'nt' else 'clear')
	
def screen_prompt(display, prompt, regex):
	'''
		Displays a screen message and compares input
		against a regex pattern.
	'''
	task = Task_Screen(display, prompt, regex)
	task.display()
	return task.input()
	
def task_display(num1, total, list):
	'''
		Displays a single task and allows the user
		to cycle through a list of tasks.
	'''
	clear_screen()
	number = num1
	# Display the task ID, the employee ID, the date, title, time, and notes of the task.
	print('Task ID: ' + str(list[number].task_id) + '\n' +
			'Employee ID: ' + str(list[number].emp_id) + '\n' +
			'Date: ' + str(list[number].date) + '\n' +
			'Title: ' + str(list[number].title) + '\n' +
			'Time: ' + str(list[number].time) + '\n' +
			'Notes: ' + str(list[number].notes) + '\n\n' +
			'Result ' + str(number+1) + ' of ' + str(total) + '\n\n')
	ans = input('[N]ext, [B]ack, [R]eturn to search menu\n')
	
	# Controls IndexErrors by not allowing the user to cycle past the 
	# first or last member of the task list.
	if ans.lower()=='n' and number != total-1:
		task_display(number+1, total, list)
	elif ans.lower()=='b' and number !=0:
		task_display(number-1, total, list)
	elif ans.lower()=='r':
		search_screen()
	else:
		# Recursively calls task_display until the user breaks out of the menu.
		task_display(number, total, list)
		
def db_open(boole):
	'''
		Opens up the database and runs a query based
		on the boolean passed as the argument. Calls
		'task_display' to then display all matches.
	'''
	try:
		db.connect()
	except OperationalError:
		pass
	task_list = Task.select().where(boole)
	db.close()
	try:
		task_display(0, len(task_list), task_list)
	except IndexError:
		i = input('No results found. Press any key to return to the search menu.')
		search_screen()
	
def search_screen():
	'''
		Displays the menu for choosing which searching
		method you want to use, Exact Date, Range of Dates,
		Exact Search, Regex Pattern, or to return to the
		menu.
	'''
	clear_screen()
	options = screen_prompt('Do you want to search by:\na)Employee ID\n' +
							'b)Range of Dates\nc)Amount of Time\nd)Search Term\n' +
							'e)Return to Menu', '>', '[AaBbCcDdEe]')
	# Prompt for date search.
	if options.lower()=='a':
		clear_screen()
		visited = []
		for i in Task.select():
			if i.emp_id not in visited:
				visited.append(i.emp_id)
				print(i.emp_id)
		inpt = screen_prompt("Enter the employee ID you would like to view:", '>', '\d*')
		
		# Search through database and return list of tasks with employee ID
		test = Task.emp_id==inpt
		db_open(test)
	# Prompt for range of dates
	elif options.lower()=='b':
		clear_screen()
		inpt = screen_prompt('Enter the range of dates.\nPlease use MM/DD/YYYY, MM/DD/YYYY format',
							'>', '([0-1][0-9])\/([0-3][0-9])\/[0-9]{4}, ([0-1][0-9])\/([0-3][0-9])\/[0-9]{4}')
		
		# Search database for tasks with dates between range of dates.
		inpt = inpt.split(', ')
		time1 = dt.strptime(inpt[0], '%m/%d/%Y').date()
		time2 = dt.strptime(inpt[1], '%m/%d/%Y').date()
		
		test = (Task.date >= time1) & (Task.date <= time2)
		db_open(test)
		
	# Prompt for time search
	elif options.lower()=='c':
		clear_screen()
		inpt = screen_prompt('Enter the amount of time:\n', '>', '\d*')
		# Search database for tasks that match time input
		test = Task.time==inpt
		db_open(test)
			
	# Prompt for search term
	elif options.lower()=='d':
		clear_screen()
		inpt = screen_prompt('Enter your search term:\n', '>', '.*')
		test = Task.notes.contains(inpt) or Task.title.contains(inpt)
		db_open(test)
		
	# Return to the main menu.
	elif options.lower()=='e':
		main()
	
def main():
	'''
		Displays the main menu and prompts
		user for a choice to either add a task, 
		search for a task, or to exit the program.
	'''
	try:
		db.connect()
	except OperationalError:
		pass
	db.create_tables([Task], safe=True)
	db.close()
	
	clear_screen()
	# Display the main menu.
	inpt = screen_prompt(
				'WORK LOG\nWhat would you like to do?\na) Add a new entry\nb) Search in existing entries\n' +
				'c) Quit program', 
				'>', 
				'[AaBbCcDd]'
				)
				
	if inpt.lower()=='a':
		clear_screen()
		#Retrieve task ID
		t_id = screen_prompt('Task ID: ', '', '\d+')
		clear_screen()
		
		#Retrieve the employee id
		e_id = screen_prompt('Employee ID: ', '', '\d+')
		
		clear_screen()
		#display the date task screen and retrieve the date.
		date = screen_prompt('Date of the task\nPlease use YYYY-MM-DD: ', '', '([0-9]{4})-([0-1][0-9])-([0-3][0-9])')
		
		clear_screen()
		#Retrieve the title of the task
		name = screen_prompt('Name of the task: ', '>', '.*[\w\s].*')
		
		clear_screen()
		#Retrieve the time spent completing the task
		time = screen_prompt('Time Spent (rounded by minute): ', '>', '\d+')
		
		clear_screen()
		#Prompt for notes
		notes = screen_prompt('Notes: ', '>', '.*[\w\s].*')
		
		#Enter task to task database.
		try:
			db.connect()
		except OperationalError:
			pass
		db.create_tables([Task], safe=True)
		Task.create(task_id=t_id, emp_id=e_id, date=date, title=name, time=time, notes=notes)
		db.close()
		clear_screen()
		i = input('Task successfully logged. Press any key to return.\n')
		main()
			
	elif inpt.lower()=='b':
		search_screen()
		
	elif inpt.lower()=='c':
		clear_screen()
		print('Thanks for using the Work Log program!')
		sys.exit()

if __name__ == '__main__':
	main()
