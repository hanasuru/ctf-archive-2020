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
	motto = db.Column(db.String(130), nullable=True)
	bio = db.Column(db.String(130), nullable=True)
	admin = db.Column(db.Boolean, index=False,
								  unique=False,
								  nullable=False)

	def __repr__(self):
		return '<User {}>'.format(self.username)


class Curhat(db.Model):	
	
	__tablename__ = 'curhat'
	id = db.Column(db.Integer, primary_key=True)
	created = db.Column(db.DateTime, index=False,
									 unique=False,
									 nullable=False)
	body = db.Column(db.String(130), nullable=False)
	user_id = db.Column(db.ForeignKey("users.id"), nullable=False)
	user = relationship("User")

