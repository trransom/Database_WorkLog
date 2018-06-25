'''employee database'''
from peewee import *

edb = SqliteDatabase('employees.db')

class Employee(Model):
	emp_id = IntegerField(unique=True)
	first_name = CharField(max_length=255)
	last_name = CharField(max_length=255)
	class Meta:
		database = edb
	
class Task(Model):
	emp_id = IntegerField(unique=True)
	date = DateTimeField()
	title = CharField(max_length=255)
	time = IntegerField()
	notes = TextField()
	class Meta:
		database = edb