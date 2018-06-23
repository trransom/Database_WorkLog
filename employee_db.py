'''employee database'''
from peewee import *

edb = SqliteDatabase('employees.db')
tdb = SqliteDatabase('tasks.db')

class Employee(Model):
	emp_id = IntegerField
	first_name = CharField(max_length=255)
	last_name = CharField(max_length=255)
	class Meta:
		database = edb
	
class Task(Model):
	emp_id = IntegerField()
	date = DateTimeField()
	title = CharField(max_length=255)
	time = IntegerField()
	notes = TextField()
	class Meta:
		database = tdb