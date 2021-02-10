from datetime import datetime


class User:
	def __init__(self, username, email, password, date_created=datetime.utcnow()):
		self.username = username
		self.email = email
		self.passsword = password
		self.date_created = date_created

	def __str__(self):
		return f'{self.username}, {self.email}, {self.passsword}'

