'''Database Work Log'''
import csv
import os
import re
import sys
from peewee import *

from task_screen import Task_Screen
#from employee_db import Database
from task import Task

db = SqliteDatabase('employees.db')

#class Employee(Model):
#	emp_id = IntegerField(unique=True)
#	first_name = CharField(max_length=255)
#	last_name = CharField(max_length=255)
#	class Meta:
#		database = db
#	
class Task(Model):
	emp_id = IntegerField(unique=True)
	date = DateTimeField()
	title = CharField(max_length=255)
	time = IntegerField()
	notes = TextField()
	class Meta:
		database = db


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
	#Prompt for date search.
	if options.lower()=='a':
		clear_screen()
		inpt = screen_prompt("Enter the employee ID:", '>', '\d*')
		
		#TODO: Search through database and return list of tasks with employee ID
		
	#prompt for range of dates
	elif options.lower()=='b':
		clear_screen()
		inpt = screen_prompt('Enter the range of dates.\nPlease use MM/DD/YYYY, MM/DD/YYYY format',
							'>', '([0-1][0-9])\/([0-3][0-9])\/[0-9]{4}, ([0-1][0-9])\/([0-3][0-9])\/[0-9]{4}')
		
		#TODO: Search database for tasks with dates between range of dates.
			
	#prompt for exact search
	elif options.lower()=='c':
		clear_screen()
		inpt = screen_prompt('Enter the amount of time:\n', '>', '\d*')
		#TODO: Search database for tasks that match time input
			
	elif options.lower()=='d':
		clear_screen()
		inpt = screen_prompt('Enter your search term:\n', '>', '.*')
		
		#TODO: Search database for tasks where either the task name or notes
		#match the input
		
		
	elif options.lower()=='e':
		main()
	
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
			id = screen_prompt('Employee ID: ', '', '\d+')
			
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
			
			#TODO: Enter task to task database.
			#If ID input is not in employee database, handle as error
			db.connect()
			db.create_tables([Task], safe=True)
			Task.create(emp_id=id, date=date, title=name, time=time, notes=notes)#Null pointer exception?
			
			
	elif inpt.lower()=='b':
		search_screen()
			
	elif inpt.lower()=='c':
		clear_screen()
		#Create employee id
		id = screen_prompt('Enter the new employee ID: ', '>', '\d+')
		
		clear_screen()
		#Create employee first name
		first = screen_prompt('Enter the employee\'s first name', '>', '\w+')
		
		clear_screen()
		#Create employee last name
		last = screen_prompt('Enter the employee\'s last name', '>', '\w+')
		
		#TODO: Enter the new employee into the employee database
		
	elif inpt.lower()=='d':
		clear_screen()
		print('Thanks for using the Work Log program!')
		sys.exit()

if __name__ == '__main__':
	main()
