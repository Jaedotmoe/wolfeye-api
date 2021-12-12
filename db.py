from peewee import *

database = SqliteDatabase('db/search.db')

class BaseModel(Model):
	""" Base to be used by other tables
	"""

	class Meta:
		database = database

class Search(BaseModel):
	title = CharField()
	url = CharField()
	last_fetched = DateTimeField()

class Token(BaseModel):
	token = CharField()
	expiry_date = DateTimeField()
