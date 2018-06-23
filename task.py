'''Task'''
class Task:

	def __init__(self, id, date, title, time_spent, notes):
		'''
			Initializes the Task object by setting the
			values for the date, title, time spent, and
			notes.
		'''
		self.id = id
		self.date = date
		self.title = title
		self.time_spent = time_spent
		self.notes = notes