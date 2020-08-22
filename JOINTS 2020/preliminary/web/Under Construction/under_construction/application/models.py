from . import db
from sqlalchemy.orm import relationship
from flask_login import UserMixin



class User(UserMixin, db.Model):

	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(30), index=False,
										unique=True,
										nullable=False)
	password = db.Column(db.String(128), nullable=False)
	bio = db.Column(db.String(100), nullable=False, unique=False)
	admin = db.Column(db.Boolean, index=False,
									unique=False,
									nullable=False)

	def __repr__(self):
		return '<User {}>'.format(self.username)