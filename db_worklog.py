'''Database Work Log'''
import csv
import os
import re
import sys
from peewee import *
from datetime import datetime as dt

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
	
def task_display(num1, total, list):
	'''
		Displays a single task and allows the user
		to cycle through a list of tasks.
	'''
	clear_screen()
	number = num1
	print('Employee ID: ' + str(list[number].emp_id) + '\n' +
			'Date: ' + str(list[number].date) + '\n' +
			'Title: ' + str(list[number].title) + '\n' +
			'Time Spent: ' + str(list[number].time) + '\n' +
			'Notes: ' + str(list[number].notes) + '\n\n' +
			'Result ' + str(number+1) + ' of ' + str(total) + '\n\n')
			
	ans = input('[N]ext, [B]ack, [R]eturn to search menu\n')
	if ans.lower()=='n' and number != total-1:
		task_display(number+1, total, list)
	elif ans.lower()=='b' and number !=0:
		task_display(number-1, total, list)
	elif ans.lower()=='r':
		search_screen()
	else:
		task_display(number, total, list)
	
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
		
		#Search through database and return list of tasks with employee ID
		#TODO: update database so that it returns more than one
		try:
			db.connect()
		except peewee.OperationalError:
			pass
		task_list = Task.select().where(Task.emp_id==inpt)
		db.close()
		try:
			task_display(0, len(task_list), task_list)
		except IndexError:
			i = input('No results found. Press any key to return to the search menu.')
			search_screen()
	#prompt for range of dates
	elif options.lower()=='b':
		clear_screen()
		inpt = screen_prompt('Enter the range of dates.\nPlease use MM/DD/YYYY, MM/DD/YYYY format',
							'>', '([0-1][0-9])\/([0-3][0-9])\/[0-9]{4}, ([0-1][0-9])\/([0-3][0-9])\/[0-9]{4}')
		
		#Search database for tasks with dates between range of dates.
		inpt = inpt.split(', ')
		time1 = dt.strptime(inpt[0], '%m/%d/%Y')
		time2 = dt.strptime(inpt[1], '%m/%d/%Y')
		try:
			db.connect()
		except OperationalError:
			pass
		task_list = Task.select().where(Task.date >= time1 and Task.date <= time2)
		db.close()
		try:
			task_display(0, len(task_list), task_list)
		except IndexError:
			i = input('No results found. Press any key to return to the search menu.')
			search_screen()
	#prompt for time search
	elif options.lower()=='c':
		clear_screen()
		inpt = screen_prompt('Enter the amount of time:\n', '>', '\d*')
		#Search database for tasks that match time input
		try:
			db.connect()
		except OperationalError:
			pass
		task_list = Task.select().where(Task.time==inpt)
		db.close()
		try:
			task_display(0, len(task_list), task_list)
		except IndexError:
			i = input('No results found. Press any key to return to the search menu.')
			search_screen()
			
	elif options.lower()=='d':
		clear_screen()
		inpt = screen_prompt('Enter your search term:\n', '>', '.*')
		
		#Search database for tasks where either the task name or notes
		#match the input
		try:
			db.connect()
		except OperationalError:
			pass
		task_list = Task.select().where((Task.title or Task.notes)==inpt)
		db.close()
		try:
			task_display(0, len(task_list), task_list)
		except IndexError:
			i = input('No results found. Press any key to return to the search menu.')
			search_screen()
		
		
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
			notes = screen_prompt('Notes: ', '>', '.*[\w\s].*')
			
			#Enter task to task database.
			#TODO:If ID input is not in employee database, handle as error
			try:
				db.connect()
			except OperationalError:
				pass
			db.create_tables([Task], safe=True)
			Task.create(emp_id=id, date=date, title=name, time=time, notes=notes)#Null pointer exception?
			db.close()
			clear_screen()
			i = input('Task successfully logged. Press any key to return.\n')
			main()
			
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
