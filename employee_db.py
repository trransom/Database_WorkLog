'''employee database'''
from peewee import *

class Database():

	db = SqliteDatabase('employees.db')

	class Employee(Model):
		emp_id = IntegerField(unique=True)
		first_name = CharField(max_length=255)
		last_name = CharField(max_length=255)
		class Meta:
			database = db
		
	class Task(Model):
		emp_id = IntegerField(unique=True)
		date = DateTimeField()
		title = CharField(max_length=255)
		time = IntegerField()
		notes = TextField()
		class Meta:
			database = db
			
	def add_task(task):
		Task.create(emp_id=task.id, date=task.date,
					title=task.title, time=task.time_spent,
					notes=task.notes)